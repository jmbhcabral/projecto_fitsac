''' Physical Evaluations form views. '''
from django.contrib import messages
from django.shortcuts import (
    get_object_or_404, redirect
)
from django.views.generic import FormView, UpdateView, CreateView
from physical_evaluations.forms import (
    PhysicalEvaluationForm, PhysicalEvaluationImagesForm,
    EatingHabitsAnswersForm, HealthStateAnswersForm
)
from physical_evaluations.models import (
    PhysicalEvaluation, PhysicalEvaluationImages, EatingHabitsAnswers,
    EatingHabitsQuestions, HealthStateAnswers, HealthStateQuestions
)
from scheduling.models import Instructor
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PhysicalEvaluationFormView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    FormView
):
    ''' Physical Evaluation form view. '''
    template_name = (
        'physical_evaluations/pages/physical-evaluations-body-composition-create.html'
    )
    form_class = PhysicalEvaluationForm

    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        ''' Check if user is instructor and set self.user '''

        # Get the user model
        User = get_user_model()

        # Get the user from the URL parameter pk
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])

        # Check if the request.user is an instructor
        instructor_exists = Instructor.objects.filter(
            instructor_id=request.user).exists()

        # If the user is not an instructor, show an error message
        # and redirect to the body composition assessment page
        if not instructor_exists:
            messages.error(request, 'Não é instrutor.')

            return redirect(
                'physical_evaluations:body_composition_assessment',
                self.user.pk
            )

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ''' Add extra context. '''
        context = super().get_context_data(**kwargs)
        context['user'] = self.user

        return context

    def form_valid(self, form):
        ''' Handle form validation. '''

        # Set the user and instructor in the form
        form.instance.user = self.user
        form.instance.instructor = Instructor.objects.get(
            instructor_id=self.request.user)
        form.save()

        messages.success(
            self.request,
            'Avaliação física criada com sucesso.'
        )

        return redirect(
            'physical_evaluations:body_composition_assessment',
            self.user.pk
        )

    def form_invalid(self, form):
        ''' Handle form invalidation. '''
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{field}: {error}')
        return self.render_to_response(self.get_context_data(form=form))


class BodyCompositionUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    ''' Body Composition update view. '''

    model = PhysicalEvaluation
    form_class = PhysicalEvaluationForm
    template_name = (
        'physical_evaluations/pages/physical-evaluations-body-composition-update.html'
    )
    context_object_name = 'body_composition_instance'
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        '''
        Checks if the user is an instructor and
        sets self.user and self.instructor
        '''
        self.object = self.get_object()
        self.student = self.object.user
        self.instructor = self.object.instructor

        if not Instructor.objects\
                .filter(instructor_id=request.user).exists():
            messages.error(request, 'Não é instrutor.')
            return redirect(
                'physical_evaluations:body_composition_assessment',
                self.student.pk
            )

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ''' Adds extra context data '''
        context = super().get_context_data(**kwargs)
        context['student'] = self.student
        context['instructor'] = self.instructor
        context['age'] = self.student.profile.get_age()

        return context

    def form_valid(self, form):
        ''' Handles form validation '''
        evaluation = form.save(commit=False)
        evaluation.user = self.student
        evaluation.instructor = Instructor.objects.get(
            instructor_id=self.request.user)
        evaluation.save()
        messages.success(
            self.request, 'Avaliação física atualizada com sucesso.'
        )
        return redirect(
            'physical_evaluations:body_composition_single',
            evaluation.pk
        )

    def form_invalid(self, form):
        ''' Handles form invalidation '''
        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")
        return self.render_to_response(self.get_context_data(form=form))


class PhysicalEvaluationImagesFormView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    '''Physical Evaluation Images Create view.'''
    form_class = PhysicalEvaluationImagesForm
    template_name = (
        'physical_evaluations/pages/physical-evaluations-images-create.html'
    )
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        '''Retrieve the evaluation instance before handling the request.'''

        # Get the evaluation instance using the primary key from URL kwargs
        self.evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])

        # Continue with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        '''Add additional context variables to the template.'''

        # Get the existing context data from the superclass method
        context = super().get_context_data(**kwargs)

        # Add the evaluation instance to the context
        context['evaluation'] = self.evaluation

        return context

    def form_valid(self, form):
        '''Handle a valid form submission.'''

        # Create a new instance from the form data without
        # saving to the database yet
        evaluation_image = form.save(commit=False)

        # Associate the image with the retrieved evaluation
        evaluation_image.evaluation = self.evaluation
        # Save the image instance to the database

        evaluation_image.save()
        # Display a success message to the user

        messages.success(self.request, 'Images adicionadas com sucesso.')
        # Redirect to the evaluation images page
        return redirect(
            'physical_evaluations:evaluation_images',
            self.evaluation.pk
        )

    def form_invalid(self, form):
        '''Handle an invalid form submission.'''

        # Iterate over the form errors
        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        # Re-render the page with the existing form and error messages
        return self.render_to_response(self.get_context_data(form=form))


class PhysicalEvaluationImagesUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    ''' Physical Evaluation Images Update view. '''
    model = PhysicalEvaluationImages
    form_class = PhysicalEvaluationImagesForm
    template_name = (
        'physical_evaluations/pages/physical-evaluations-images-update.html'
    )
    context_object_name = 'evaluation_images_instance'
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        '''
        Check if the user is an instructor and set the evaluation instance.
        '''

        # Get the evaluation instance
        self.evaluation_images_instance = self.get_object()
        self.evaluation = self.evaluation_images_instance.evaluation

        # Continue with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ''' Add additional context variables to the template. '''

        # Get the existing context data from the superclass method
        context = super().get_context_data(**kwargs)

        # Add EvaluationImages instance to the context
        context['evaluation_images'] = self.evaluation_images_instance

        # Add the evaluation instance to the context
        context['evaluation'] = self.evaluation

        return context

    def form_valid(self, form):
        ''' Handle a valid form submission. '''

        # Save the form
        form.instance.evaluation = self.evaluation
        self.object = form.save()

        messages.success(
            self.request,
            'Imagens actualizadas com sucesso.'
        )

        return redirect(
            'physical_evaluations:evaluation_images',
            self.evaluation.pk
        )

    def form_invalid(self, form):
        ''' Handle an invalid form submission. '''
        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")
        return self.render_to_response(self.get_context_data(form=form))


class EatingHabitsAswersFormView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    FormView
):
    ''' Eating Habits Answers form view. '''
    template_name = (
        'physical_evaluations/pages/physical-evaluations-eating-habits-create.html'
    )
    form_class = EatingHabitsAnswersForm
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        '''
        Retreive evaluation and questions before handling the request.
        '''

        # Get the evaluation instance using the primary key from URL kwargs
        self.evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])

        # Retrieve all eating habits questions
        self.eating_questions = EatingHabitsQuestions.objects.all()

        # Proceed with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        ''' Add the questions to the form initialization kwargs. '''

        # Get the exixting form kwargs from the superclass
        kwargs = super().get_form_kwargs()

        # Pass the questions to the form constructor
        kwargs['questions'] = self.eating_questions

        return kwargs

    def get_context_data(self, **kwargs):
        ''' Add additional context variables to the template. '''

        # Get the existing context data from the superclass method
        context = super().get_context_data(**kwargs)

        # Add the evaluation instance to the context
        context['evaluation'] = self.evaluation

        # Add the questions to the context
        context['questions'] = self.eating_questions

        return context

    def form_valid(self, form):
        ''' Handle a valid form submission. '''

        # Iterate over the questions
        for question in self.eating_questions:
            # Get the answer text from the form
            answer_text = form.cleaned_data.get(f'answer_{question.id}')
            # Create a new EatingHabitsAnswers instance
            EatingHabitsAnswers.objects.create(
                evaluation=self.evaluation,
                question=question,
                answer=answer_text
            )

        # Display a success message to the user
        messages.success(self.request, 'Respostas adicionadas com sucesso.')

        # Redirect to the eating habits page
        return redirect(
            'physical_evaluations:eating_habits',
            self.evaluation.pk
        )

    def form_invalid(self, form):
        ''' Handle an invalid form submission. '''
        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")
        return self.render_to_response(self.get_context_data(form=form))


class EatingHabitsAnswersUpdateFormView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    FormView
):
    ''' Eating Habits Answers update view. '''

    template_name = 'physical_evaluations/pages/physical-evaluations-eating-habits-update.html'
    form_class = EatingHabitsAnswersForm
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        '''
        Retrieve the evaluation and questions before handling the request.
        '''

        # Get the evaluation instance using the primary key from URL kwargs
        self.evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])

        # Retrieve all eating habits questions
        self.eating_questions = EatingHabitsQuestions.objects.all()

        # Retrieve all eating habits answers for the evaluation
        self.answers = EatingHabitsAnswers.objects.filter(
            evaluation=self.evaluation)

        # Proceed with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        ''' Add the questions to the form initialization kwargs. '''

        # Get the existing form kwargs from the superclass
        kwargs = super().get_form_kwargs()

        # Pass the questions to the form constructor
        kwargs['questions'] = self.eating_questions

        return kwargs

    def get_initial(self):
        ''' Add the answers to the form initialization kwargs. '''
        initial = super().get_initial()

        # Iterate over the answers and add them to the initial data
        for answer in self.answers:
            initial[f'answer_{answer.question.id}'] = answer.answer
        return initial

    def form_valid(self, form):
        ''' Handle a valid form submission. '''

        # Iterate over the answers
        for answer in self.answers:
            # Get the answer text from the form
            answer_text = form.cleaned_data.get(
                f'answer_{answer.question.id}'
            )
            # Update the answer text
            answer.answer = answer_text
            answer.save()

        # Display a success message to the user
        messages.success(
            self.request,
            'Respostas actualizadas com sucesso.'
        )

        return redirect(
            'physical_evaluations:eating_habits',
            self.evaluation.pk
        )

    def form_invalid(self, form):
        ''' Handle an invalid form submission. '''
        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ''' Add additional context variables to the template. '''

        # Get the existing context data from the superclass method
        context = super().get_context_data(**kwargs)

        # Add the evaluation instance to the context
        context['evaluation'] = self.evaluation

        # Add the questions to the context
        context['questions'] = self.eating_questions

        return context


class HealthStateFormView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    FormView
):
    ''' Health State form view. '''
    template_name = (
        'physical_evaluations/pages/physical-evaluations-health-state-create.html'
    )
    form_class = HealthStateAnswersForm
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        ''' Retrieve evaluation and questions before handling the request. '''

        # Get the evaluation instance using the primary key from URL kwargs
        self.evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])

        # Retrieve all health state questions
        self.health_questions = HealthStateQuestions.objects.all()

        # Proceed with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        ''' Add the questions to the form initialization kwargs. '''

        # Get the existing form kwargs from the superclass
        kwargs = super().get_form_kwargs()

        # Pass the questions to the form constructor
        kwargs['questions'] = self.health_questions

        return kwargs

    def get_context_data(self, **kwargs):
        ''' Add additional context variables to the template. '''

        # Get the existing context data from the superclass method
        context = super().get_context_data(**kwargs)

        # Add the evaluation instance to the context
        context['evaluation'] = self.evaluation

        # Add the questions to the context
        context['questions'] = self.health_questions

        return context

    def form_valid(self, form):
        ''' Handle a valid form submission. '''

        # Iterate over the questions
        for question in self.health_questions:
            # Get the answer text from the form
            answer_text = form.cleaned_data.get(f'answer_{question.id}')

            # Create a new HealthStateAnswers instance
            HealthStateAnswers.objects.create(
                evaluation=self.evaluation,
                question=question,
                answer=answer_text
            )

        # Display a success message to the user
        messages.success(
            self.request,
            'Respostas adicionadas com sucesso.'
        )

        # Redirect to the health state page
        return redirect(
            'physical_evaluations:health_state',
            self.evaluation.pk
        )

    def form_invalid(self, form):
        ''' Handle an invalid form submission. '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))


class HealthStateAnswersUpdateFormView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    FormView
):
    ''' Health State Answers update view. '''

    template_name = 'physical_evaluations/pages/physical-evaluations-health-state-update.html'
    form_class = HealthStateAnswersForm
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def dispatch(self, request, *args, **kwargs):
        '''
        Retrieve the evaluation and questions before handling the request.
        '''

        # Get the evaluation instance using the primary key from URL kwargs
        self.evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])

        # Retrieve all health state questions
        self.health_questions = HealthStateQuestions.objects.all()

        # Retrieve all health state answers for the evaluation
        self.answers = HealthStateAnswers.objects.filter(
            evaluation=self.evaluation)

        # Proceed with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        ''' Add the questions to the form initialization kwargs. '''

        # Get the existing form kwargs from the superclass
        kwargs = super().get_form_kwargs()

        # Pass the questions to the form constructor
        kwargs['questions'] = self.health_questions

        return kwargs

    def get_initial(self):
        ''' Add the answers to the form initialization kwargs. '''
        initial = super().get_initial()

        # Iterate over the answers and add them to the initial data
        for answer in self.answers:
            initial[f'answer_{answer.question.id}'] = answer.answer
        return initial

    def form_valid(self, form):
        ''' Handle a valid form submission. '''

        # Iterate over the answers
        for answer in self.answers:
            # Get the answer text from the form
            answer_text = form.cleaned_data.get(f'answer_{answer.question.id}')
            # Update the answer text
            answer.answer = answer_text
            answer.save()

        # Display a success message to the user
        messages.success(
            self.request,
            'Respostas actualizadas com sucesso.'
        )

        return redirect(
            'physical_evaluations:health_state',
            self.evaluation.pk
        )

    def form_invalid(self, form):
        ''' Handle an invalid form submission. '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ''' Add additional context variables to the template. '''

        # Get the existing context data from the superclass method
        context = super().get_context_data(**kwargs)

        # Add the evaluation instance to the context
        context['evaluation'] = self.evaluation

        # Add the questions to the context
        context['questions'] = self.health_questions

        return context

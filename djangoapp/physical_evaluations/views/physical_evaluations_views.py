''' Physical Evaluations views. '''
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.contrib.auth import get_user_model
from physical_evaluations.models import (
    PhysicalEvaluation, PhysicalEvaluationImages, EatingHabitsAnswers,
    HealthStateAnswers
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UserSearchView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    ListView
):
    ''' Students Management view. '''

    template_name = (
        'physical_evaluations/pages/students-management-search.html'
    )
    model = get_user_model()
    context_object_name = 'users'
    success_url = reverse_lazy('physical_evaluations:students_management')
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

    def get_queryset(self):
        ''' Get queryset. '''

        # Get the user model
        User = get_user_model()

        queryset = self.request.GET.get('q')

        if queryset:
            return User.objects.filter(first_name__icontains=queryset)

        return User.objects.none()


class SingleUserView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Single User view. '''

    template_name = (
        'physical_evaluations/pages/student-management-single.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data. '''

        # Subscribe the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get the user model
        User = get_user_model()

        # Get the user from the URL parameter pk and add it
        # to the context data dictionary
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['user'] = user

        return context


class BodyCompositionView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Body Composition view. '''

    template_name = (
        'physical_evaluations/pages/physical-evaluations-body-composition-assessment.html'
    )
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def get_context_data(self, **kwargs):
        ''' Get context data. '''

        # Subscribe the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get the user model
        User = get_user_model()

        # Get the user from the URL parameter pk and add
        # it to the context data dictionary
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['user'] = user

        # Get the body composition assessments for the user and add
        # it to the context data dictionary
        body_composition_assessments = PhysicalEvaluation.objects.filter(
            user=user).order_by('-date')
        context['body_composition_assessments'] = body_composition_assessments

        return context


class BodyCompositionSingleView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Body Composition Single view. '''

    template_name = (
        'physical_evaluations/pages/physical-evaluations-body-composition-single.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data. '''

        # Subscribe the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get the evaluation from the URL parameter pk and add
        # it to the context data dictionary
        body_composition_single = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])
        context['body_composition_single'] = body_composition_single

        # Get the student from the evaluation and add
        # it to the context data dictionary
        student = body_composition_single.user
        context['student'] = student

        # Get the age of the student and add it to the context data dictionary
        age = body_composition_single.user.profile.get_age()
        context['age'] = age

        return context


class PhysicalEvaluationImagesView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Physical Evaluation Images view. '''

    template_name = (
        'physical_evaluations/pages/physical-evaluations-images.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data. '''

        # Subscribe the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get the evaluation from the URL parameter pk and add
        # it to the context data dictionary
        evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])
        context['evaluation'] = evaluation

        # Get the images for the evaluation and add
        # it to the context data dictionary
        evaluation_images = PhysicalEvaluationImages.objects.filter(
            evaluation=evaluation).first()

        context['evaluation_images'] = evaluation_images

        return context


class EatingHabitsView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Eating Habits view. '''

    template_name = (
        'physical_evaluations/pages/physical-evaluations-eating-habits.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data. '''

        # Subscribe the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get the evaluation from the URL parameter pk and add
        # it to the context data dictionary
        evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])
        context['evaluation'] = evaluation

        # Get the eating habits answers for the evaluation and add
        # it to the context data dictionary
        eating_habits = EatingHabitsAnswers.objects.filter(
            evaluation=evaluation)
        context['eating_habits'] = eating_habits

        return context


class HealthStateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Health State view. '''

    template_name = (
        'physical_evaluations/pages/physical-evaluations-health-state.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data. '''

        # Subscribe the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get the evaluation from the URL parameter pk and add
        # it to the context data dictionary
        evaluation = get_object_or_404(
            PhysicalEvaluation, pk=self.kwargs['pk'])
        context['evaluation'] = evaluation

        # Get the health state answers for the evaluation and add
        # it to the context data dictionary
        health_state = HealthStateAnswers.objects.filter(evaluation=evaluation)
        context['health_state'] = health_state

        return context

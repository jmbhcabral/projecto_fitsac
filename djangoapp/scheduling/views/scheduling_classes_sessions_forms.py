''' '''

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView
from scheduling.models import ClassSession, WeeklyClass
from scheduling.forms import ClassSessionStartForm, ClassSessionEndForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from datetime import date
from django.http import JsonResponse


class ClassSessionStartView(FormView):
    ''' View to render the class session create page '''

    form_class = ClassSessionStartForm
    template_name = 'scheduling/pages/class-session-create.html'
    success_url = reverse_lazy('scheduling:session_qrcode')

    def get_form_kwargs(self):
        ''' Method to get the form kwargs '''

        # Get the form kwargs from the parent class method
        kwargs = super().get_form_kwargs()

        # Get the class from the URL parameter class_id
        fitness_class = get_object_or_404(WeeklyClass, pk=self.kwargs['pk'])

        # Add the class to the form kwargs
        kwargs['fitness_class'] = fitness_class

        return kwargs

    def form_valid(self, form):
        ''' Method to validate the form '''

        # Get the class from the URL parameter class_id
        fitness_class = get_object_or_404(WeeklyClass, pk=self.kwargs['pk'])

        # Get the session date from the form data
        session_date = form.cleaned_data.get('date', '')
        print(f'Session date: {session_date}')

        # Check if a session already exists for the class, date and time
        if ClassSession.objects.filter(
                fitness_class=fitness_class,
                date=session_date,
                time=fitness_class.time).exists():
            messages.error(
                self.request,
                'Já existe uma sessão de aula para a data e hora selecionadas.'
            )
            return redirect(self.success_url)

        # Set the fitness class to the form instance
        form.instance.fitness_class = fitness_class

        # Get the instructor from the request user
        instructor = fitness_class.instructor

        # Set the instructor to the form instance
        form.instance.instructor = instructor

        # Save the form
        form.save()

        # Add a success message
        messages.success(self.request, 'Sessão de aula criada com sucesso.')

        return redirect('scheduling:session_qrcode', session_id=form.instance.pk)

    def form_invalid(self, form):
        ''' Method to handle the form invalid '''

        # Iterate over the form errors
        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return super().form_invalid(form)


class ClassSessionEditView(UpdateView):
    ''' View to render the class session edit page '''

    model = ClassSession
    form_class = ClassSession
    template = 'scheduling/pages/class-session-update.html'
    success_url = reverse_lazy('scheduling:classes_sessions')

    def get_context_data(self, **kwargs):
        ''' Method to get the context data '''

        # Subscribe the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get the class session from the object and add it to the
        # context data dictionary
        context['session'] = self.get_object()

        return context


class ClassSessionEndView(FormView):
    pass
    # TODO: Implementar a view de finalização de sessão de aula


class MarkAttendanceView(LoginRequiredMixin, View):
    ''' View to render the mark attendance page '''

    def post(self, request, *args, **kwargs):
        ''' Method to handle the post request '''
        try:
            qr_code = request.GET.get('code', '')

            # Get session id from the qr code
            class_session = get_object_or_404(
                ClassSession, session_identifier=qr_code)

            # Check if the user is already a participant
            if class_session.participants.filter(pk=request.user.pk).exists():

                return JsonResponse({'success': False, 'message': 'Presença já marcada.'})

            # Mark user as participant of the class session
            class_session.participants.add(request.user)

            return JsonResponse({'success': True, 'message': 'Presença marcada com sucesso.'})
        except ClassSession.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Sessão não encontrada.'})

        except Exception as e:
            print(f'Error: {str(e)}')
            return JsonResponse({'success': False, 'message': f'Erro: {str(e)}.'})

    def get(self, request, *args, **kwargs):
        ''' Method to handle the get request '''
        return JsonResponse({'success': False, 'message': 'Método não permitido.'})

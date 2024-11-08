''' This module contains the view to render the scheduling
classes and sessions page.
'''
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from scheduling.models import ClassSession
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ClassesSessionsView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' View to render the scheduling classes and sessions page '''

    template_name = 'scheduling/pages/classes-sessions.html'
    login_url = '/login/'

    def test_func(self):
        ''' Method to check if the user is in the _access_restricted group '''
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_admin').exists()
        )

    def get_context_data(self, **kwargs):
        ''' Method to get the context data '''
        context = super().get_context_data(**kwargs)

        # Get the instructor from the request user and add it
        # to the context data dictionary
        instructor = self.request.user
        context['instructor'] = instructor

        # Get all the sessions
        sessions = ClassSession\
            .objects\
            .select_related('fitness_class')\
            .order_by('-date')\
            .all()
        context['sessions'] = sessions

        # Get search query from the URL
        search_query = self.request.GET.get('date')

        if search_query:
            searched_sessions = sessions.filter(date=search_query)
            if searched_sessions.exists():
                context['searched_sessions'] = searched_sessions
            else:
                messages.error(
                    self.request, 'Não há sessões de aulas para a data selecionada.')

        return context


class QrCodeView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' View to render the QR code page '''

    template_name = 'scheduling/pages/class-session-qr-code.html'
    login_url = '/login/'

    def test_func(self):
        ''' Method to check if the user is in the _access_restricted group '''
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_admin').exists()
        )

    def get_context_data(self, **kwargs):
        ''' Method to get the context data '''
        context = super().get_context_data(**kwargs)

        # Get the session from the URL parameter session_id
        session = get_object_or_404(ClassSession, pk=self.kwargs['session_id'])

        context['session'] = session

        return context


class QrCodeScannerView(
    LoginRequiredMixin,
    TemplateView
):
    ''' View to render the QR code scanner page '''

    template_name = 'scheduling/pages/class-session-qr-code-reader.html'
    login_url = '/login/'

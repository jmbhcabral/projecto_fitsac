''' This module contains the view to render the scheduling classes and sessions page '''
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from scheduling.models import ClassSession
from django.contrib.auth.mixins import LoginRequiredMixin


class ClassesSessionsView(TemplateView):
    ''' View to render the scheduling classes and sessions page '''

    template_name = 'scheduling/pages/classes-sessions.html'

    def get_context_data(self, **kwargs):
        ''' Method to get the context data '''
        context = super().get_context_data(**kwargs)

        # Get the instructor from the request user and add it
        # to the context data dictionary
        instructor = self.request.user
        context['instructor'] = instructor

        return context


class QrCodeView(TemplateView):
    ''' View to render the QR code page '''

    template_name = 'scheduling/pages/class-session-qr-code.html'

    def get_context_data(self, **kwargs):
        ''' Method to get the context data '''
        context = super().get_context_data(**kwargs)

        # Get the session from the URL parameter session_id
        session = get_object_or_404(ClassSession, pk=self.kwargs['session_id'])

        context['session'] = session

        return context


class QrCodeScannerView(LoginRequiredMixin, TemplateView):
    ''' View to render the QR code scanner page '''

    template_name = 'scheduling/pages/class-session-qr-code-reader.html'

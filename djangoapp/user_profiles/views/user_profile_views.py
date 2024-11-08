''' This file contains the views for the user_profiles app. '''
from collections import defaultdict
from django.shortcuts import render
from django.views import View
from user_profiles.models import UserProfile
from .user_profile_forms import BaseProfile
from billing.models import Invoice
from scheduling.models import ClassSession
from django.contrib.auth.mixins import LoginRequiredMixin


class UserAccountView(LoginRequiredMixin, BaseProfile):
    ''' View for the user account page, inherited from BaseProfile. '''
    login_url = '/login/'

    def __init__(self):
        ''' Constructor method. '''
        # Calls the constructor of the parent class BaseProfile
        super().__init__()

        self.template_name = 'user_profiles/pages/user-account.html'
        self.context = {}

    def get(self, request, *args, **kwargs):
        ''' Default GET method. '''

        user = request.user

        user_with_overdue_payments = Invoice.objects.filter(
            status=False,
            user=user
        ).order_by('user__first_name', 'invoice_date')

        overdue_payments_by_user = defaultdict(list)

        for item in user_with_overdue_payments:
            overdue_payments_by_user[item.invoice_date.year].append(item)

        self.context['overdue_payments_by_user'] = overdue_payments_by_user

        # Get all classes attended by the user
        classes_attended = ClassSession.objects.filter(
            participants=user).count()

        self.context['classes_attended'] = classes_attended

        return render(request, self.template_name, self.context)


class UserAccountLogoutView(LoginRequiredMixin, BaseProfile):
    ''' View for the user account page. '''
    login_url = '/login/'

    def __init__(self):
        ''' Constructor method. '''
        self.template_name = 'user_profiles/pages/user-logout.html'

    def get(self, request, *args, **kwargs):
        ''' Default GET method. '''

        return super().get(request, *args, **kwargs)


class UserAccountProfileView(LoginRequiredMixin, View):
    ''' View for the user account page. '''
    login_url = '/login/'

    def __init__(self):
        ''' Constructor method. '''
        self.template_name = 'user_profiles/pages/user-profile.html'

    def setup(self, request, *args, **kwargs):
        ''' Retrieve BaseProfile setup method. '''
        super().setup(request, *args, **kwargs)

        self.context = {}

    def get(self, request, *args, **kwargs):
        ''' Prepare the context with common data. '''

        if request.user.is_authenticated:

            # Get the user profile
            user = request.user

            try:
                user_profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                # Handle the case where the profile does not exist
                user_profile = None

            postal_code_final = None

            if user_profile and user_profile.postal_code:
                postal_code_db = str(user_profile.postal_code)

                if len(postal_code_db) == 7:
                    postal_code_1 = postal_code_db[:4]
                    postal_code_2 = postal_code_db[4:]

                    postal_code_final = f'{postal_code_1}-{postal_code_2}'
                else:
                    postal_code_final = None
            else:
                postal_code_final = None

            self.context.update({
                'postal_code': postal_code_final,
                'user': user,
                'user_profile': user_profile
            })

        return render(request, self.template_name, self.context)

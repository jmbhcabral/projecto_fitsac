''' This file contains the views for the user_profiles app. '''
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.views import View
from user_profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .user_profile_forms import BaseProfile


class UserAccountView(BaseProfile):
    ''' View for the user account page, inherited from BaseProfile. '''

    def __init__(self):
        ''' Constructor method. '''
        # Calls the constructor of the parent class BaseProfile
        super().__init__()

        self.template_name = 'user_profiles/pages/user-account.html'

    def get(self, request, *args, **kwargs):
        ''' Default GET method. '''

        return super().get(request, *args, **kwargs)


class UserAccountLogoutView(BaseProfile):
    ''' View for the user account page. '''

    def __init__(self):
        ''' Constructor method. '''
        self.template_name = 'user_profiles/pages/user-logout.html'

    def get(self, request, *args, **kwargs):
        ''' Default GET method. '''

        return super().get(request, *args, **kwargs)


class UserAccountProfileView(View):
    ''' View for the user account page. '''

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
                user_profile = None  # Handle the case where the profile does not exist

            postal_code_final = None

            if user_profile and user_profile.postal_code:
                postal_code_db = str(user_profile.postal_code)
                print(f'Postal code: {postal_code_db}')

                if len(postal_code_db) == 7:
                    postal_code_1 = postal_code_db[:4]
                    postal_code_2 = postal_code_db[4:]

                    postal_code_final = f'{postal_code_1}-{postal_code_2}'
                    print(f'Postal code: {postal_code_final}')
                else:
                    postal_code_final = None
            else:
                postal_code_final = None

            self.context.update({
                'postal_code': postal_code_final,
                'user': user,
                'user_profile': user_profile
            })
            print(f'Context get useraccountprofileview: {self.context}')

        return render(request, self.template_name, self.context)

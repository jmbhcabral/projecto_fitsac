''' User Profile Form Views '''

from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.views.generic import FormView
from utils.email_confirmations import (
    send_confirmation_email, send_reset_password_email
)
from utils.generate_reset_password_code import (
    generate_reset_password_code
)
import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user_profiles.models import UserProfile
from user_profiles.forms import UserForm, UserProfileForm
from django.utils import timezone
from datetime import timedelta


# TODO: checar se o perfil do utilizador está completo
class BaseProfile(View):
    ''' Base profile view. '''

    def __init__(self):
        ''' Constructor method. '''
        self.template_name = None
        self.user_profile = None
        self.context = {}

    def setup(self, request, *args, **kwargs):
        ''' Prepare the context with common data. '''

        # Guarantees that the parent setup method is called
        super().setup(request, *args, **kwargs)

        if self.__class__.__name__ != 'CreateView':
            # Check if user is authenticated
            if request.user.is_authenticated:
                # Load the user's profile
                self.user_profile = UserProfile.objects.filter(
                    user=request.user).first()
                print(f'User profile: {self.user_profile}')

    def get(self, request, *args, **kwargs):
        ''' Default GET method. '''

        super().setup(request, *args, **kwargs)
        # Check if the user is authenticated
        if not request.user.is_authenticated:

            messages.error(
                request, 'Por favor, faça login ou registe-se para continuar.')

            return redirect('user_profiles:login')

        # Check if the user has a profile
        if not self.user_profile:
            messages.error(
                request,
                'Por favor, preencha o seu perfil para continuar.'
            )
            return redirect('user_profiles:update_profile')
        # Get method is responsible for initializing context variables
        self.context = ({
            'user': request.user,
            'user_profile': self.user_profile,
            'userform': UserForm(instance=request.user, data=request.POST or None),
            'profileform': UserProfileForm(
                data=request.POST or None,
                instance=self.user_profile
            )
        })

        print(f'Self context base: {self.context}')

        return render(request, self.template_name, self.context)


class CreateView(BaseProfile):
    ''' View for user registration. '''

    def __init__(self):
        super().__init__()
        self.template_name = 'user_profiles/pages/register.html'

    def setup(self, request, *args, **kwargs):
        ''' Set up the registration form. '''
        super().setup(request, *args, **kwargs)
        self.context['userform'] = UserForm(data=request.POST or None)

    def get(self, request, *args, **kwargs):
        ''' Render the registration page with the form. '''
        self.setup(request, *args, **kwargs)

        # If the user is authenticated, redirect to the user account page
        if request.user.is_authenticated:
            return redirect('user_profiles:user_account')
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        ''' Handle user registration. '''
        self.setup(request, *args, **kwargs)

        # Clean session data
        request.session.clear()

        if self.context['userform'].is_valid():
            userform = self.context['userform']
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            first_name = userform.cleaned_data['first_name']
            last_name = userform.cleaned_data['last_name']
            code = generate_reset_password_code()

            # Store the data in the session
            request.session['temp_user'] = {
                'username': username,
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'code': code
            }

            # Send confirmation email
            send_confirmation_email(request, email, username, code)
            messages.success(
                request,
                'Verifique o seu email para activar a conta.'
            )

            return redirect('user_profiles:user_verification_code')
        else:
            for field in self.context['userform'].errors:
                for error in self.context['userform'].errors[field]:
                    messages.error(request, error)
            messages.error(
                request, 'Por favor, corrija os erros no formulário.')

        return render(request, self.template_name, self.context)


class VerificationCodeView(View):
    '''View for inserting the verification code.'''

    def get(self, request):
        '''GET method.'''
        if request.user.is_authenticated:
            return redirect('user_profiles:user_account')

        return render(request, 'user_profiles/pages/user-verification-code.html')

    def post(self, request):
        '''POST method.'''

        # Get the code from the post request
        code_1 = request.POST.get('code_1')
        code_2 = request.POST.get('code_2')
        code_3 = request.POST.get('code_3')

        final_code = int(f'{code_1}{code_2}{code_3}')

        # Get the user from the session
        temp_user = request.session.get('temp_user', None)

        # Check if the user exists
        if not temp_user:
            messages.error(
                request,
                'Utilizador não encontrado! Por favor, registe-se novamente.'
            )
            return redirect('user_profiles:register')

        # Check if the code is valid
        if not final_code or str(temp_user.get('code')) != str(final_code):
            messages.error(
                request,
                'Código inválido! Por favor, insira o código correto.'
            )
            return render(request, 'user_profiles/pages/verification-code.html')

        # Create the user
        User.objects.create_user(
            username=temp_user['username'],
            email=temp_user['email'],
            password=temp_user['password'],
            first_name=temp_user['first_name'],
            last_name=temp_user['last_name'],
        )

        # Create the user profile
        UserProfile.objects.create(
            user=User.objects.get(username=temp_user['username'])
        )

        messages.success(
            request,
            'Email confirmado com sucesso! Já pode aceder á sua conta.'
        )
        return redirect('user_profiles:login')


class LoginView(FormView):
    ''' View for user login using FormView. '''

    template_name = 'user_profiles/pages/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('user_profiles:user_account')

    def form_valid(self, form):
        ''' If the form is valid, autheticate and log the user in. '''
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, 'Login efectuado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' If the form is invalid, show an error message. '''
        messages.error(
            self.request, 'Credenciais inválidas.Por favor, tente novamente.')
        return self.render_to_response(self.get_context_data(form=form))

    def get(self, request, *args, **kwargs):
        ''' Check if the user is authenticated. '''
        if request.user.is_authenticated:
            return redirect('user_profiles:user_account')
        return super().get(request, *args, **kwargs)


class LogoutView(View):
    ''' View for logging out the user. '''

    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        ''' Log the user out. '''
        if request.user.is_authenticated:
            logout(request)

            messages.success(request, 'Logout efectuado com sucesso!')

            return redirect('user_profiles:login')
        return redirect('user_profiles:login')


class UpdateProfileView(BaseProfile):
    ''' View for updating user and profile information. '''

    def __init__(self):
        super().__init__()
        self.template_name = 'user_profiles/pages/user-profile-update.html'

    def setup(self, request, *args, **kwargs):
        ''' Configure the forms for updating the user and profile. '''

        super().setup(request, *args, **kwargs)

        if request.user.is_authenticated:
            print('Updating user profile...')
            print(f'Request user: {request.user}')
            print(f'User profile: {self.user_profile}')

            self.user_profile, created = UserProfile.objects.get_or_create(
                user=request.user)
            # Verifica se o perfil está a ser recuperado/criado
            print(f'User profile: {self.user_profile}, Created: {created}')

            self.context['userform'] = UserForm(
                instance=request.user,
                data=request.POST or None,
                current_user=request.user,
                updating=True
            )
            self.context['profileform'] = UserProfileForm(
                instance=self.user_profile,
                data=request.POST or None
            )

    def post(self, request, *args, **kwargs):
        ''' Handle updating user and profile data. '''
        print('Updating user profile...(POST)')
        self.setup(request, *args, **kwargs)

        # Handling the profile form
        profile_form = self.context['profileform']

        # Get the user instance
        user_form = self.context['userform']
        print(f'User form: {user_form}')

        print('1')

        if self.context['userform'].is_valid() and self.context['profileform'].is_valid():

            # Check if profile photo is present in the request files
            if 'photo' in request.FILES:
                # Atributes the photo to the profile instance
                profile_form.instance.photo = request.FILES['photo']

            # Get postal_code_1 and postal_code_2 from the post request
            postal_code_1 = request.POST.get('postal_code_1')
            postal_code_2 = request.POST.get('postal_code_2')

            # Check if the postal codes are present in the request
            if postal_code_1 and postal_code_2:
                # Assign the postal code to the profile instance
                full_postal_code = f'{postal_code_1}{postal_code_2}'
                profile_form.instance.postal_code = full_postal_code
                print(f'Postal code: {full_postal_code}')

            profile_form.save()
            user_form.save()

            messages.success(request, 'Dados atualizados com sucesso!')
            return redirect('user_profiles:user_account')
        else:
            print('2')
            # Handling errors
            for field in self.context['userform'].errors:
                for error in self.context['userform'].errors[field]:
                    messages.error(request, error)
            for field in self.context['profileform'].errors:
                for error in self.context['profileform'].errors[field]:
                    messages.error(request, f'{field}: {error}')
            messages.error(
                request, 'Por favor, corrija os erros no formulário.'
                'Todos os campos devem ser preenchidos.'
            )

            # Get the postal code from the user profile
            postal_code = str(self.user_profile.postal_code) \
                if self.user_profile else ''

            # Check if the postal code is valid
            if len(postal_code) == 7:
                # First 4 digits
                self.context['postal_code_1'] = postal_code[:4]
                # Last 3 digits
                self.context['postal_code_2'] = postal_code[4:]
            else:
                self.context['postal_code_1'] = ''
                self.context['postal_code_2'] = ''

            return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        ''' Render the page with the forms. '''
        print('Getting user profile...(GET)')

        super().get(request, *args, **kwargs)

        if request.user.is_authenticated:
            self.setup(request, *args, **kwargs)

            self.context['userform'] = UserForm(
                instance=request.user,

            )

            self.context['profileform'] = UserProfileForm(
                instance=self.user_profile,
            )

            # Get the postal code from the user profile
            postal_code = str(self.user_profile.postal_code) \
                if self.user_profile else ''

            # Check if the postal code is valid
            if len(postal_code) == 7:
                # First 4 digits
                self.context['postal_code_1'] = postal_code[:4]
                # Last 3 digits
                self.context['postal_code_2'] = postal_code[4:]
            else:
                self.context['postal_code_1'] = ''
                self.context['postal_code_2'] = ''
            print(f'Context Update profile: {self.context}')

        return render(request, self.template_name, self.context)


# class EmailConfirmation(View):
#     '''Email confirmation view.'''

#     def get(self, request, token):
#         '''GET method.'''
#         # User recovery from the session
#         temp_user = request.session.get('temp_user', None)

#         # Ckeck if the token is valid
#         if not temp_user or str(temp_user.get('code')) != str(code):
#             messages.error(
#                 request,
#                 'Este código já foi utilizado ou está expirado!'
#             )
#             return redirect('user_profiles:register')

#         # Create the user
#         User.objects.create_user(
#             username=temp_user['username'],
#             email=temp_user['email'],
#             password=temp_user['password'],
#             first_name=temp_user['first_name'],
#             last_name=temp_user['last_name'],
#         )

#         # Create the user profile
#         UserProfile.objects.create(
#             user=User.objects.get(username=temp_user['username'])
#         )

#         # Delete the session
#         request.session.clear()

#         user_profile = UserProfile.objects.filter(
#             user=request.user).first()

#         user_profil

#         messages.success(
#             request,
#             'Email confirmado com sucesso! Já pode aceder á sua conta.'
#         )
#         return redirect('user_profiles:login')


class ChangePasswordView(BaseProfile):
    '''View for changing the user password.'''

    def __init__(self):
        super().__init__()
        self.template_name = 'user_profiles/pages/user-change-password.html'

    def setup(self, request, *args, **kwargs):
        '''Set up the context with the userform.'''
        super().setup(request, *args, **kwargs)

        if request.user.is_authenticated:
            self.context['userform'] = UserForm(
                instance=request.user,
                data=request.POST or None,
                current_user=request.user,
                updating_password_only=True
            )

    def post(self, request, *args, **kwargs):
        '''Handle the post request for changing the password.'''
        self.setup(request, *args, **kwargs)
        user = request.user

        old_password = request.POST.get('old_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Password antiga incorreta!')
            return render(request, self.template_name, self.context)

        if self.context['userform'].is_valid():

            new_password = self.context['userform'].cleaned_data.get(
                'password')

            user.set_password(new_password)

            user.save()
            logout(request)
            self.request.session.clear()

            messages.success(request, 'Password alterada com sucesso!')
            return redirect('user_profiles:user_account')
        else:
            for field_name in self.context['userform'].errors:
                form_field = self.context['userform'][field_name]

                # Verifica se o label personalizado foi atribuído corretamente
                label = form_field.label or field_name.capitalize()

                # Itera sobre os erros do campo
                for error in self.context['userform'].errors[field_name]:
                    messages.error(request, f'{label}: {error}')
            messages.error(
                request, 'Por favor, corrija os erros no formulário.'
                'Todos os campos devem ser preenchidos.'
            )
            return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        '''Render the page with the form.'''
        if request.user.is_authenticated:
            self.setup(request, *args, **kwargs)

        return super().get(request, *args, **kwargs)


class ResetPasswordView(View):
    '''View for resetting the user password.'''

    def get(self, request):
        '''GET method.'''
        return render(request, 'user_profiles/pages/user-reset-password.html')

    def post(self, request):
        '''POST method.'''

        # Get the email from the post request
        email = request.POST.get('email')

        # Check if the email exists
        user = User.objects.filter(email=email).first()

        # Check if the user exists
        if not user:
            messages.error(request, 'Email não encontrado!')
            return render(
                request,
                'user_profiles/pages/user-reset-password.html'
            )

        # Store the email in the session
        request.session['reset_email'] = email

        reset_code = generate_reset_password_code()
        user.profile.reset_password_code = reset_code

        user.profile.reset_password_code_expires = timezone.now()
        user.profile.save()

        send_reset_password_email(request, email, reset_code)

        messages.success(
            request,
            'Verifique o seu email para redefinir a password.'
        )
        return redirect('user_profiles:user_reset_code')


class ResetCodeView(View):
    '''View for resetting the user password.'''

    def __init__(self):
        super().__init__()
        self.template_name = 'user_profiles/pages/user-reset-code.html'
        self.context = {}

    def post(self, request, *args, **kwargs):
        '''Handle the post request for inserting the reset code.'''

        # Get the code from the post request
        code_1 = request.POST.get('code_1')
        code_2 = request.POST.get('code_2')
        code_3 = request.POST.get('code_3')
        final_code = int(f'{code_1}{code_2}{code_3}')

        # Find the user with the reset code
        user = UserProfile.objects.filter(
            reset_password_code=final_code).first()

        # Check if the code is valid
        if not final_code:
            messages.error(request, 'Código inválido!')
            return render(request, self.template_name, self.context)

        if user:
            # Check if the code has expired
            expiration_time = user.reset_password_code_expires + \
                timezone.timedelta(minutes=15)
            if timezone.now() > expiration_time:
                messages.error(
                    request,
                    'Código expirado! Por favor, solicite um novo.'
                )
                self.context['allow_resend'] = True
                return render(request, self.template_name, self.context)

            # Store the code in the session
            request.session['reset_code'] = final_code
            return redirect(
                'user_profiles:user_reset_change_password'
            )
        else:
            messages.error(request, 'Código inválido!')
            return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        '''Render the page with the form.'''
        if request.user.is_authenticated:
            self.setup(request, *args, **kwargs)
            return redirect('user_profiles:user_account')

        return render(request, self.template_name, self.context)


class ResetChangePasswordView(View):
    '''View for changing the user password after resetting.'''

    def __init__(self):
        super().__init__()
        self.request = None
        self.template_name = (
            'user_profiles/pages/user-reset-change-password.html'
        )
        self.context = {}

    def get_user_profile_and_form(self, request):
        ''' Auxiliary method to get the user profile and form. '''

        # Get session data
        code = request.session.get('reset_code', None)

        if not code:
            messages.error(
                self.request,
                'Código de validação não encontrado!'
            )
            return redirect('user_profiles:user_reset_code')

        # Get the user profile
        user_profile = UserProfile.objects.filter(
            reset_password_code=code).first()

        # Check if the user exists
        if not user_profile:
            messages.error(self.request, 'Código inválido!')
            return redirect('user_profiles:user_reset_code')

        # Check if the code has expired
        if user_profile.reset_password_code_expires:
            expiration_time = user_profile.reset_password_code_expires + \
                timezone.timedelta(minutes=15)

            if timezone.now() > expiration_time:
                messages.error(
                    self.request,
                    'Código expirado! Por favor, solicite um novo.'
                )
                return None

        else:
            messages.error(
                self.request, 'Código expirado! Por favor, solicite um novo.')
            return None

        # Create the user form
        user_form = UserForm(
            instance=user_profile.user,
            data=self.request.POST or None,
            current_user=user_profile.user,
            updating_password_only=True
        )

        return user_profile, user_form

    def get(self, request):
        '''GET method.'''

        # Get the user profile
        result = self.get_user_profile_and_form(request)

        # Check if the user profile and form were retrieved
        if not result:
            return redirect('user_profiles:user_reset_code')

        user_profile, user_form = result

        # Add the user form to the context
        self.context['userform'] = user_form

        return render(
            self.request,
            self.template_name,
            self.context
        )

    def post(self, request):
        '''POST method.'''

        # Get the user profile and form
        result = self.get_user_profile_and_form(request)

        # Check if the user profile and form were retrieved
        if not result:
            return redirect('user_profiles:user_reset_code')

        # Get the user profile and form
        user_profile, user_form = result

        # Add the user form to the context
        self.context['userform'] = user_form

        # Check if the form is valid
        if user_form.is_valid():
            password = request.POST.get('password')

            # Set the new password
            user_profile.user.set_password(password)
            user_profile.user.save()

            # Clear the reset password code
            user_profile.reset_password_code = None
            user_profile.reset_password_code_expires = None
            user_profile.save()

            # Clear the session data
            del request.session['reset_code']
            del request.session['reset_email']

            messages.success(request, 'Password alterada com sucesso!')
            return redirect('user_profiles:login')
        else:
            # Handling errors
            for field_name in user_form.errors:
                form_field = user_form[field_name]

                # Check if the custom label was correctly assigned
                label = form_field.label or field_name.capitalize()

                # Iterate over the field errors
                for error in user_form.errors[field_name]:
                    messages.error(request, f'{label}: {error}')

            messages.error(
                request, 'Por favor, corrija os erros no formulário.'
                'Todos os campos devem ser preenchidos.'
            )

            return render(self.request, self.template_name, self.context)


class ResendResetCodeView(View):
    '''View for resending the reset code.'''

    def post(self, request):
        '''POST method.'''

        # Get the email from the session
        email = request.session.get('reset_email', None)

        if not email:
            messages.error(
                request,
                'Não foi possível encontrar o email. '
                'Por favor, insira novamente.'
            )
            return redirect(
                'user_profiles:user_reset_password'
            )

        # Check if the email exists
        user = User.objects.filter(email=email).first()

        if not user:
            messages.error(request, 'Utilizador não encontrado!')
            return redirect(
                'user_profiles:user_reset_password'
            )

        reset_code = generate_reset_password_code()
        user.profile.reset_password_code = reset_code
        user.profile.reset_password_code_expires = timezone.now()
        user.profile.save()

        send_reset_password_email(request, email, reset_code)

        messages.success(
            request,
            'Um novo código foi enviado.'
        )
        return redirect('user_profiles:user_reset_code')

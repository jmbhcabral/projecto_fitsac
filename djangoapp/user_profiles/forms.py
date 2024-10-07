''' User profiles forms. '''
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

from datetime import datetime


class UserProfileForm(forms.ModelForm):
    ''' User profile form. '''

    class Meta:
        model = UserProfile
        fields = [
            'bio', 'phone', 'photo', 'profession', 'date_of_birth',
            'gender', 'address', 'postal_code', 'locality', 'city',
            'nif',
        ]
        labels = {
            'bio': 'Biografia',
            'phone': 'Telefone',
            'photo': 'Foto',
            'profession': 'Profissão',
            'date_of_birth': 'Data de Nascimento',
            'gender': 'Género',
            'address': 'Morada',
            'postal_code_1': 'Código Postal (Parte 1)',
            'postal_code_2': 'Código Postal (Parte 2)',
            'locality': 'Localidade',
            'city': 'Cidade',
            'nif': 'NIF',
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        # Filling the postal_code_1 and postal_code_2 fields
        #  with the user's data
        if self.instance and self.instance.postal_code:
            # converting into string
            postal_code_str = str(self.instance.postal_code)

            # Check if the postal code exists and has 7 characters
            if len(postal_code_str) == 7:
                self.fields['postal_code_1'].initial = (
                    postal_code_str[:4]
                )
                self.fields['postal_code_2'].initial = (
                    postal_code_str[5:]
                )
        else:
            self.fields['postal_code_1'].initial = ''
            self.fields['postal_code_2'].initial = ''

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Biografia',
            }
        )
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Telefone',
            }
        )
    )
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Foto',
            }
        ),
        required=False
    )
    profession = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Profissão',
            }
        )
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Data de Nascimento',
                'id': 'id_date_of_birth',
            }
        )
    )
    gender = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
        ]
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Morada',
            }
        )
    )
    postal_code_1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '1234',
            }
        ),
        max_length=4,
        min_length=4,
    )
    postal_code_2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '567',
            }
        ),
        max_length=3,
        min_length=3,
    )
    locality = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Localidade',
            }
        )
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cidade',
            }
        )
    )
    client_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Número de Cliente',
            }
        ), required=False
    )
    nif = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'NIF',
            }
        )
    )

    def clean(self):
        print('Cleaning data')
        cleaned_data = super(UserProfileForm, self).clean()
        phone = cleaned_data.get('phone')
        profession = cleaned_data.get('profession')
        date_of_birth = cleaned_data.get('date_of_birth')
        gender = cleaned_data.get('gender')
        print(f'Gender: {gender}')
        address = cleaned_data.get('address')
        postal_code_1 = cleaned_data.get('postal_code_1')
        postal_code_2 = cleaned_data.get('postal_code_2')
        locality = cleaned_data.get('locality')
        city = cleaned_data.get('city')
        bio = cleaned_data.get('bio')
        nif = cleaned_data.get('nif')

        errors = {}

        # Phone field validation
        if phone:
            if len(str(phone)) != 9:
                errors['phone'] = 'Este campo deve ter 9 números.'

            if not str(phone).isdigit():
                errors['phone'] = 'Este campo deve conter apenas números.'

        else:
            errors['phone'] = 'Este campo é obrigatório.'

        # Profession field validation
        if profession:
            if len(profession) > 100:
                errors['profession'] = (
                    'Este campo deve ter no máximo 100 caracteres.'
                )

            if len(profession) < 4:
                errors['profession'] = (
                    'Este campo deve ter no mínimo 4 caracteres.'
                )

        else:
            errors['profession'] = 'Este campo é obrigatório.'

        # Date of birth field validation
        if date_of_birth:
            current_year = datetime.now().year

            if date_of_birth.year > current_year:
                errors['date_of_birth'] = 'Ano inválido.'

            if current_year - date_of_birth.year < 8:
                errors['date_of_birth'] = 'Idade mínima: 8 anos.'

            if date_of_birth.year < 1900:
                errors['date_of_birth'] = 'Ano inválido.'

        else:
            errors['date_of_birth'] = 'Este campo é obrigatório.'

        # Address field validation
        if address:
            if len(address) > 100:
                errors['address'] = (
                    'Este campo deve ter no máximo 100 caracteres.'
                )

            if len(address) < 4:
                errors['address'] = (
                    'Este campo deve ter no mínimo 4 caracteres.'
                )

        else:
            errors['address'] = 'Este campo é obrigatório.'

        # Postal code validation
        if postal_code_1 and postal_code_2:
            # Concatenating the two parts of the postal code
            full_postal_code = f'{postal_code_1}{postal_code_2}'
            if len(full_postal_code) != 7:
                errors['postal_code'] = 'Este campo deve ter 7 números.'
            cleaned_data['postal_code'] = f'{postal_code_1}{postal_code_2}'
            print(f'Postal code: {cleaned_data["postal_code"]}')
        else:
            errors['postal_code'] = 'Este campo é obrigatório.'

        # Locality field validation
        if locality:
            if len(locality) > 100:
                errors['locality'] = (
                    'Este campo deve ter no máximo 100 caracteres.'
                )

            if len(locality) < 3:
                errors['locality'] = (
                    'Este campo deve ter no mínimo 3 caracteres.'
                )

        else:
            errors['locality'] = 'Este campo é obrigatório.'

        # City field validation
        if city:
            if len(city) > 100:
                errors['city'] = (
                    'Este campo deve ter no máximo 100 caracteres.'
                )

            if len(city) < 3:
                errors['city'] = (
                    'Este campo deve ter no mínimo 3 caracteres.'
                )

        else:
            errors['city'] = 'Este campo é obrigatório.'

        # Bio field validation
        if bio:
            if len(bio) > 500:
                errors['bio'] = (
                    'Este campo deve ter no máximo 500 caracteres.'
                )

            if len(bio) < 10:
                errors['bio'] = (
                    'Este campo deve ter no mínimo 10 caracteres.'
                )

        # NIF field validation
        if nif:
            nif_cleaned = ''.join(filter(str.isdigit, str(nif)))

            if len(nif_cleaned) != 9:
                errors['nif'] = 'Este campo deve ter 9 números.'

            if not nif_cleaned.isdigit():
                errors['nif'] = 'Este campo deve conter apenas números.'

        else:
            errors['nif'] = 'Este campo é obrigatório.'

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data


class UserForm(forms.ModelForm):
    ''' User form. '''

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'password', 'password2'
        ]
        labels = {
            'username': 'Nome de Utilizador',
            'first_name': 'Primeiro Nome',
            'last_name': 'Último Nome',
            'email': 'Email',
            'password': 'Palavra-passe',
            'password2': 'Confirmar Palavra-passe'
        }

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome de Utilizador'
            }
        ),
        max_length=50,
        required=True,
        help_text='O nome de utilizador deve ter no máximo 50 caracteres.'
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome'
            }
        ),
        max_length=30,
        required=True,
        help_text='Digite o seu nome.'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Apelido'
            }
        ),
        max_length=30,
        required=True,
        help_text='Digite o seu apelido.'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        ),
        max_length=100,
        required=True,
        help_text='Digite o seu email.'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Palavra-passe'
            }
        ),
        max_length=50,
        required=True,
        help_text='Digite a sua palavra-passe.'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar Palavra-passe'
            }
        ),
        max_length=50,
        required=False,
        help_text='Confirme a sua palavra-passe.'
    )

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        updating = kwargs.pop('updating', False)
        updating_password_only = kwargs.pop('updating_password_only', False)

        super(UserForm, self).__init__(*args, **kwargs)

        self.current_user = current_user

        print(f'Updating init form: {updating}')

        # Atribui os labels personalizados aos campos
        self.fields['username'].label = 'Nome de Utilizador'
        self.fields['first_name'].label = 'Primeiro Nome'
        self.fields['last_name'].label = 'Último Nome'
        self.fields['email'].label = 'Email'
        self.fields['password'].label = 'Palavra-passe'
        self.fields['password2'].label = 'Confirmar Palavra-passe'

        # If the user is updating his profile, the password fields
        # must be optional
        if updating:
            print('if Updating')
            self.fields.pop('password')
            self.fields.pop('password2')

            # If the user is updating his profile, the username field
            # must be readonly
            self.fields['username'].widget.attrs['readonly'] = True

        # If the user is changing only the password fields
        if updating_password_only:
            self.fields.pop('username')
            self.fields.pop('first_name')
            self.fields.pop('last_name')
            self.fields.pop('email')

    def clean(self):
        cleaned_data = super().clean()

        current_user_data = cleaned_data.get('username')
        email_data = cleaned_data.get('email')
        password_data = cleaned_data.get('password')
        password2_data = cleaned_data.get('password2')

        # Check if the username already exists
        user_db = User.objects.filter(username=current_user_data).first()

        # Check if the email already exists
        email_db = User.objects.filter(email=email_data).first()

        # Errors dictionary
        errors = {}

        error_msg_required = 'Este campo é obrigatório.'

        # Logged user is updating his profile : UPDATING
        # He must not change his username
        if self.current_user:
            # Check if the username already exists
            if user_db:
                # Check if the username is different from the current user
                if current_user_data != user_db.username:
                    errors['username'] = ('Este nome de utilizador já existe.')

            # Check if the email already exists
            if email_db:
                # Check if the email is different from the current user
                if email_data != email_db.email:
                    errors['email'] = ('Este email já está registado.')

            # Check if the password is empty
            if password_data or password2_data:
                # Check if the password is different from the password2
                if password_data != password2_data:
                    errors['password'] = ('As palavras-passe não coincidem.')
                    errors['password2'] = ('As palavras-passe não coincidem.')
                # Check if the password is less than 8 characters
                if len(password_data) < 8:
                    errors['password'] = (
                        'A palavra-passe deve ter no mínimo 8 caracteres.')

        # New user is registering : REGISTERING
        # He must provide a username
        else:
            # Check if the username is empty
            if not current_user_data:
                errors['username'] = error_msg_required
            # Check if the username already exists
            if user_db:
                errors['username'] = ('Este nome de utilizador já existe.')

            # Check if the email is empty
            if not email_data:
                errors['email'] = error_msg_required
            # Check if the email already exists
            if email_db:
                errors['email'] = ('Este email já está registado.')

            # Check if the password is empty
            if not password_data:
                print('Password is empty')
                errors['password'] = error_msg_required

            elif not password2_data:
                errors['password2'] = error_msg_required

            else:
                # Check if the password is different from the password2
                if password_data != password2_data:
                    errors['password'] = ('As palavras-passe não coincidem.')
                    errors['password2'] = ('As palavras-passe não coincidem.')
                # Check if the password is less than 8 characters
                if len(password_data) < 8:
                    errors['password'] = (
                        'A palavra-passe deve ter no mínimo 8 caracteres.')

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data

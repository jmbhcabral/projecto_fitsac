''' This file contains the forms for the fitsac app. '''

from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.ModelForm):
    ''' Form for the Contact model. '''
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Nome',
            'email': 'Email',
            'subject': 'Assunto',
            'message': 'Mensagem',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digita o nome',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digita o email',
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digita o assunto',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digita a mensagem',
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name:
            raise ValidationError('O campo nome é obrigatório.')

        if len(name) < 3:
            raise ValidationError('O nome deve ter no mínimo 3 caracteres.')

        if name.isdigit():
            raise ValidationError('O nome não pode ser um número.')

        return name

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email:
            raise ValidationError('O campo email é obrigatório.')

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValidationError('O email não é válido.')

        return email

    def clean_subject(self):
        subject = self.cleaned_data['subject']

        if not subject:
            raise ValidationError('O campo assunto é obrigatório.')

        if len(subject) < 5:
            raise ValidationError('O assunto deve ter no mínimo 5 caracteres.')

        return subject

    def clean_message(self):
        message = self.cleaned_data['message']

        if not message:
            raise ValidationError('O campo mensagem é obrigatório.')

        if len(message) < 10:
            raise ValidationError(
                'A mensagem deve ter no mínimo 10 caracteres.')

        return message

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

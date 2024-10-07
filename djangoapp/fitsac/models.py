''' This file contains the models for the fitsac app. '''
from django.db import models
from django.utils import timezone
from utils.image_validators import resize_image


class Contact(models.Model):
    ''' Model for the Contact form. '''
    name = models.CharField(
        max_length=100,
        help_text='Escreva o seu Nome.',
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=150,
        help_text='Escreva o seu Email.',
        blank=False,
        null=False,
    )
    subject = models.CharField(
        max_length=100,
        help_text='Escreva o Assunto.',
        blank=False,
        null=False,
    )
    message = models.TextField(
        help_text='Escreva a sua Mensagem.',
        blank=False,
        null=False,
        max_length=500,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

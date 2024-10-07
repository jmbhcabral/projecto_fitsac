''' Forms for the scheduling app '''
from django.contrib.auth.models import User
from utils.formatters import format_duration
from .models import (
    WeeklyClass, Booking, Instructor, ClassTimeException, ClassSession,
    InstructorSubstitution
)
from django import forms
import datetime
from datetime import timedelta
from django.utils import timezone
import re


class InstructorForm(forms.ModelForm):
    ''' Form for the Instructor model. '''
    class Meta:
        model = Instructor
        fields = ('instructor', 'bio')

    user_search = forms.CharField(
        label='Pesquisar instrutor',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Pesquise por nome ou email',
                'id': 'user_search_input',  # For the JS script
            }
        )
    )
    instructor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'user_select'}
        ),
        required=True
    )

    bio = forms.CharField(
        label='Biografia',
        # max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Biografia do instrutor',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()

        bio = cleaned_data.get('bio')

        erros = {}

        if not bio:
            erros['bio'] = 'A biografia do instrutor é obrigatória.'
        if bio:
            if len(bio) < 5:
                erros['bio'] = (
                    'A biografia do instrutor deve ter pelo menos '
                    '5 caracteres.'
                )
            if len(bio) > 500:
                excedent = len(bio) - 500
                erros['bio'] = (
                    f'A biografia do instrutor tem {len(bio)} '
                    f'caracteres. Só são permitidos 500 caracteres '
                    f'Tem {excedent} caracteres a mais.'
                )
        if erros:
            raise forms.ValidationError(erros)
        return cleaned_data


class WeeklyClassForm(forms.ModelForm):
    class Meta:
        model = WeeklyClass
        fields = ['title', 'description', 'instructor',
                  'substitute_instructor', 'duration', 'day_of_week',
                  'time', 'max_participants', 'is_visible']
    title = forms.CharField(
        label='Título',
        help_text='Escreva o tipo de aula',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Título da aula',
            }
        )
    )
    description = forms.CharField(
        label='Descrição',
        help_text='Escreva uma descrição do Tipo de aula',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da aula',
            }
        )
    )
    instructor = forms.ModelChoiceField(
        label='Instrutor',
        help_text='Selecione o instrutor padrão da aula',
        queryset=Instructor.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    substitute_instructor = forms.ModelChoiceField(
        label='Instrutor Substituto',
        help_text='Deixe em branco para usar o instrutor padrão',
        queryset=Instructor.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    duration = forms.CharField(
        label='Duração',
        help_text='Duração da aula (hh:mm:ss)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':
                'Duração da aula (ex. 1:30:00 para 1 hora e meia)',
            }
        )
    )
    day_of_week = forms.ChoiceField(
        label='Dia da semana',
        help_text='Selecione o dia da semana da aula',
        choices=WeeklyClass.DAYS_OF_WEEK,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    time = forms.TimeField(
        label='Horário',
        help_text='Hora a que começa a aula(ex. 14:30)',
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={
                'class': 'form-control',
                'placeholder': 'Horário da aula',
            }
        )
    )
    max_participants = forms.IntegerField(
        label='Participantes',
        help_text='Número máximo de participantes',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    is_visible = forms.BooleanField(
        label='Visível',
        help_text='Marque para tornar a aula visível no calendário',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        duration = cleaned_data.get('duration')
        time = cleaned_data.get('time')
        max_participants = cleaned_data.get('max_participants')
        day_of_week = cleaned_data.get('day_of_week')

        erros = {}

        if not title:
            erros['title'] = 'O título da aula é obrigatório.'
        if title:
            if len(title) < 2:
                erros['title'] = (
                    f'O título da aula deve ter pelo menos 2 '
                    f'caracteres. Tem {len(title)} caracteres.'
                )
            if len(title) > 100:
                excedent = len(title) - 100
                erros['title'] = (
                    f'O título da aula tem {len(title)} '
                    f'caracteres. Só são permitidos 100 caracteres. '
                    f'Tem {excedent} caracteres a mais.'
                )

        if not description:
            erros['description'] = 'A descrição da aula é obrigatória.'
        if description:
            if len(description) < 10:
                erros['description'] = (
                    f'A descrição da aula deve ter pelo menos '
                    f'10 caracteres. Tem {len(description)} caracteres.'
                )
            if len(description) > 500:
                excedent = len(description) - 500
                erros['description'] = (
                    f'A descrição da aula tem {len(description)} '
                    f'caracteres. Só são permitidos 500 caracteres. '
                    f'Tem {excedent} caracteres a mais.'
                )

        if not duration:
            erros['duration'] = 'A duração da aula é obrigatória.'
        else:
            # Regex para verificar o formato hh:mm:ss
            if not re.match(r'^\d{1,2}[:.,]\d{2}[:.,]\d{2}$', duration):
                erros['duration'] = 'A duração da aula deve estar no formato hh:mm:ss.'

            else:
                try:
                    # Conversão do string hh:mm:ss para timedelta
                    hours, minutes, seconds = map(
                        int, duration.replace(',', ':').split(':'))
                    duration_timedelta = datetime.timedelta(
                        hours=hours, minutes=minutes, seconds=seconds)
                except ValueError:
                    erros['duration'] = 'Formato inválido para a duração da aula. Use o formato hh:mm:ss.'
                    duration_timedelta = None

                if duration_timedelta:
                    if duration_timedelta < datetime.timedelta(0):
                        erros['duration'] = 'A duração da aula não pode ser negativa.'
                    if duration_timedelta > datetime.timedelta(hours=24):
                        erros['duration'] = 'A duração da aula não pode ser maior que 24 horas.'
                    if duration_timedelta == datetime.timedelta(0):
                        erros['duration'] = 'A duração da aula não pode ser zero.'

        if not time:
            erros['time'] = 'O horário da aula é obrigatório.'
        if time:
            # Verificação adicional para garantir que está no formato hh:mm
            if time.strftime('%H:%M') != self.data.get('time'):
                erros['time'] = (
                    'O horário da aula deve estar no formato hh:mm.'
                )

        if not max_participants:
            erros['max_participants'] = (
                'O número máximo de participantes é obrigatório.'
            )
        if max_participants:
            if max_participants < 0:
                erros['max_participants'] = (
                    'O número máximo de participantes não pode ser negativo.'
                )
            if max_participants == 0:
                erros['max_participants'] = (
                    'O número máximo de participantes não pode ser zero.'
                )
            if day_of_week and time:
                weekly_class = WeeklyClass.objects\
                    .filter(
                        day_of_week=day_of_week,
                        time=time
                    )\
                    .exclude(
                        id=self.instance.id
                    )
                if weekly_class.exists():
                    erros = {
                        'time': 'Já existe uma aula para este dia e horário.'
                    }

        if erros:
            raise forms.ValidationError(erros)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'duration' in self.initial:
            self.initial['duration'] = format_duration(
                self.initial['duration'])


class ClassTimeExceptionForm(forms.ModelForm):
    ''' Form for the ClassTimeException model. '''
    class Meta:
        model = ClassTimeException
        fields = ['fitness_class', 'date', 'new_time']

    fitness_class = forms.ModelChoiceField(
        label='Aula',
        queryset=WeeklyClass.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Aula',
            }
        )
    )
    date = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Data',
            }
        )
    )
    new_time = forms.TimeField(
        label='Novo horário',
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Novo horário',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        new_time = cleaned_data.get('new_time')

        erros = {}

        if not date:
            erros['date'] = 'A data é obrigatória.'
        if date:
            if date < datetime.date.today():
                erros['date'] = 'A data não pode ser no passado.'

        if not new_time:
            erros['new_time'] = 'O novo horário é obrigatório.'
        if new_time:
            if new_time.strftime('%H:%M') != self.data.get('new_time'):
                erros['new_time'] = (
                    'O novo horário deve estar no formato hh:mm.'
                )

        if erros:
            raise forms.ValidationError(erros)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fitness_class'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['new_time'].widget.attrs['class'] = 'form-control'


class BookingForm(forms.Form):
    ''' Formulário para o modelo Booking. '''
    class Meta:
        model = Booking
        fields = ['fitness_class']

    fitness_class = forms.ModelMultipleChoiceField(
        label='Aula',
        queryset=WeeklyClass.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-control',
                'placeholder': 'Aula',
            }
        ),
        help_text='Selecione as aulas que deseja marcar presença.',
    )

    def clean(self):
        ''' Form validation'''
        cleaned_data = super().clean()
        fitness_class = cleaned_data.get('fitness_class')
        user = cleaned_data.get('user')

        erros = {}

        if fitness_class:
            # Check if the user has already booked the class
            class_instance = Booking.objects.filter(
                fitness_class__in=fitness_class,
                user=user,

            )

            if class_instance.exists():
                erros['fitness_class'] = 'Você já marcou presença nesta aula.'

        # Ckeck if at least one class was selected
        if not fitness_class:
            erros['fitness_class'] = 'Selecione pelo menos uma aula.'

        if erros:
            raise forms.ValidationError(erros)

        return cleaned_data


class CancelBookingForm(forms.Form):
    ''' Form for canceling a booking. '''
    class Meta:
        model = Booking
        fields = ['booking_id']

    booking_ids = forms.ModelMultipleChoiceField(
        label='Aula',
        # Initializing with an empty queryset
        queryset=Booking.objects.none(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-control',
                'placeholder': 'Reserva',
            }
        ),
        help_text='Selecione a aula que deseja cancelar.',
    )

    def clean(self):
        ''' Form validation '''
        cleaned_data = super().clean()
        booking_ids = cleaned_data.get('booking_ids')
        print(f'Clean Booking IDs: {booking_ids}')

        erros = {}

        if not booking_ids or len(booking_ids) == 0:
            erros['booking_ids'] = 'Selecione pelo menos uma aula.'

        if erros:
            print(f'Erros clean: {erros}')
            raise forms.ValidationError(erros)

        return cleaned_data


class ClassSessionForm(forms.ModelForm):
    ''' 
    Form for the ClassSession model. 
    '''
    class Meta:
        model = ClassSession
        fields = ['fitness_class', 'instructor',
                  'date', 'time', 'participants', 'notes']

    fitness_class = forms.ModelChoiceField(
        label='Aula',
        queryset=WeeklyClass.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Aula',
            }
        )
    )
    instructor = forms.ModelChoiceField(
        label='Instrutor',
        queryset=Instructor.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Instrutor',
            }
        )
    )
    participants = forms.ModelMultipleChoiceField(
        label='Participantes',
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-control',
                'placeholder': 'Participantes',
            }
        )
    )
    notes = forms.CharField(
        label='Observações',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Observações',
            }
        )
    )

    def clean(self):
        ''' Form validation '''
        cleaned_data = super().clean()
        fitness_class = cleaned_data.get('fitness_class')
        instructor = cleaned_data.get('instructor')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        participants = cleaned_data.get('participants')
        notes = cleaned_data.get('notes')

        erros = {}

        if not fitness_class:
            erros['fitness_class'] = 'A aula é obrigatória.'

        if not instructor:
            erros['instructor'] = 'O instrutor é obrigatório.'

        if not participants:
            erros['participants'] = 'Selecione pelo menos um participante.'

        if notes:
            if len(notes) > 500:
                excedent = len(notes) - 500
                erros['notes'] = (
                    f'O campo de observações tem {len(notes)} '
                    f'caracteres. Só são permitidos 500 caracteres. '
                    f'Tem {excedent} caracteres a mais.'
                )

        if erros:
            raise forms.ValidationError(erros)

        return cleaned_data


class InstructorSubstitutionForm(forms.ModelForm):
    ''' Form for the InstructorSubstitution model. '''
    class Meta:
        model = InstructorSubstitution
        fields = ['fitness_class', 'substitute_instructor', 'date', 'reason']

    fitness_class = forms.ModelChoiceField(
        label='Aula',
        queryset=WeeklyClass.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    substitute_instructor = forms.ModelChoiceField(
        label='Instrutor substituto',
        queryset=Instructor.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    date = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    reason = forms.CharField(
        label='Motivo',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        max_length=500,
    )

    def clean(self):
        ''' Form validation '''
        cleaned_data = super().clean()
        fitness_class = cleaned_data.get('fitness_class')
        substitute_instructor = cleaned_data.get('substitute_instructor')
        date = cleaned_data.get('date')
        reason = cleaned_data.get('reason')

        print(f'Fitness Class: {fitness_class}')
        print(f'Substitute Instructor: {substitute_instructor}')
        print(f'Date: {date}')
        print(f'Reason: {reason}')
        print(f'Fitness Class Instructor: {fitness_class.instructor.name}')

        erros = {}

        if not fitness_class:
            erros['fitness_class'] = 'A aula é obrigatória.'

        if not substitute_instructor:
            erros['substitute_instructor'] = 'O instrutor substituto é '
            'obrigatório.'

        if substitute_instructor == fitness_class.instructor:
            erros['substitute_instructor'] = 'O instrutor substituto não pode '
            'ser o mesmo que o instrutor da aula.'

        if not date:
            erros['date'] = 'A data é obrigatória.'
        if date:
            if date < datetime.date.today():
                erros['date'] = 'A data não pode ser no passado.'

        if reason:
            if len(reason) < 5:
                erros['reason'] = (
                    'O motivo deve ter pelo menos 5 caracteres.'
                )
            if len(reason) > 500:
                excedent = len(reason) - 500
                erros['reason'] = (
                    f'O motivo tem {len(reason)} caracteres. '
                    f'Só são permitidos 500 caracteres. '
                    f'Tem {excedent} caracteres a mais.'
                )

        if erros:
            raise forms.ValidationError(erros)

        return cleaned_data

''' This file is used to create forms for the physical_evaluations app. '''
from django import forms
from .models import (
    PhysicalEvaluation, PhysicalEvaluationImages,
    EatingHabitsAnswers, HealthStateAnswers
)
from .models import BodyType
from scheduling.models import Instructor
from django.utils import timezone
from django.contrib import messages


class PhysicalEvaluationForm(forms.ModelForm):
    ''' Physical Evaluation form. '''

    class Meta:
        ''' Meta class. '''
        model = PhysicalEvaluation
        fields = ['body_type', 'date', 'weight', 'height', 'body_fat_percentage', 'total_water_percentage',
                  'muscle_mass_percentage', 'fitness_level', 'calories_burned', 'metabolic_age',
                  'bone_mass', 'visceral_fat_percentage', 'waist_circumference', 'belly_circumference',
                  'hip_circumference', 'leg_circumference', 'arm_circumference',
                  'observations']
        labels = {
            'body_type': 'Tipo de corpo',
            'date': 'Data',
            'weight': 'Peso',
            'height': 'Altura',
            'body_fat_percentage': 'Gordura corporal',
            'total_water_percentage': 'Água',
            'muscle_mass_percentage': 'Massa muscular',
            'fitness_level': 'Nível de fitness',
            'calories_burned': 'Calorias queimadas',
            'metabolic_age': 'Idade metabólica',
            'bone_mass': 'Massa óssea',
            'visceral_fat_percentage': 'Gordura visceral',
            'waist_circumference': 'Circunferência da cintura',
            'belly_circumference': 'Circunferência do abdômen',
            'hip_circumference': 'Circunferência do quadril',
            'leg_circumference': 'Circunferência da perna',
            'arm_circumference': 'Circunferência do braço',
            'observations': 'Observações'
        }

    body_type = forms.ModelChoiceField(
        label='Tipo de corpo',
        queryset=BodyType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date = forms.DateField(
        label='Data',
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    weight = forms.DecimalField(
        label='Peso',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    height = forms.DecimalField(
        label='Altura',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    body_fat_percentage = forms.DecimalField(
        label='Percentagem de Gordura corporal',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    total_water_percentage = forms.DecimalField(
        label='Percentagem de Água',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    muscle_mass_percentage = forms.DecimalField(
        label='Percentagem de Massa muscular',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    fitness_level = forms.IntegerField(
        label='Nível de fitness',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    calories_burned = forms.IntegerField(
        label='Calorias queimadas',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    metabolic_age = forms.IntegerField(
        label='Idade metabólica',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    bone_mass = forms.DecimalField(
        label='Massa óssea',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    visceral_fat_percentage = forms.DecimalField(
        label='Percentagem de Gordura visceral',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    waist_circumference = forms.DecimalField(
        label='Circunferência da cintura',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    belly_circumference = forms.DecimalField(
        label='Circunferência do abdômen',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    hip_circumference = forms.DecimalField(
        label='Circunferência do quadril',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    leg_circumference = forms.DecimalField(
        label='Circunferência da perna',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    arm_circumference = forms.DecimalField(
        label='Circunferência do braço',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    observations = forms.CharField(
        label='Observações',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    def clean(self):
        ''' Clean method. '''
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        observations = cleaned_data.get('observations')

        errors = {}

        if date > timezone.now().date():

            errors['date'] = 'A data não pode ser maior que a data atual.'

        if observations:
            observations_length = len(observations)
            observations_excepted_length = 1000
            surplus = observations_length - observations_excepted_length
            if observations_length > 1000:
                errors['observations'] = (
                    f'As observações não podem ter mais de 255 '
                    f'caracteres. As observações têm mais {surplus} caracteres.'
                )

        if errors:
            raise forms.ValidationError(errors)
        return cleaned_data


class PhysicalEvaluationImagesForm(forms.ModelForm):
    ''' Physical Evaluation Images form. '''

    class Meta:
        ''' Meta class. '''
        model = PhysicalEvaluationImages
        fields = ['image_front', 'image_side', 'image_back']
        labels = {
            'image_front': 'Imagem da frente',
            'image_side': 'Imagem de lado',
            'image_back': 'Imagem de costas'
        }

    image_front = forms.ImageField(
        label='Imagem da frente',
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )
    image_side = forms.ImageField(
        label='Imagem de lado',
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )
    image_back = forms.ImageField(
        label='Imagem de costas',
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )

    def save(self, commit=True):
        ''' Save method. '''

        # Get the instance
        instance = super().save(commit=False)

        # Handle the image_front
        if not self.cleaned_data.get('image_front'):

            # If no image is provided, keep the exixting one
            instance.image_front = self.instance.image_front

        # Handle the image_side
        if not self.cleaned_data.get('image_side'):

            # If no image is provided, keep the existing one
            instance.image_side = self.instance.image_side

        # Handle the image_back
        if not self.cleaned_data.get('image_back'):

            # If no image is provided, keep the existing one
            instance.image_back = self.instance.image_back

        # Save the instance
        if commit:
            instance.save()

        return instance


class EatingHabitsAnswersForm(forms.Form):
    ''' Eating Habits Answers dynamic form. '''

    def __init__(self, *args, questions=None, **kwargs):
        super(EatingHabitsAnswersForm, self).__init__(*args, **kwargs)
        if questions:
            for question in questions:
                # Check if the question is about alcohol consumption
                if "álcool" in question.question_text.lower():
                    self.fields[f'answer_{question.id}'] = forms.ChoiceField(
                        label=question.question_text,
                        choices=EatingHabitsAnswers.ALCOHOL_CONSUMPTION_CHOICES,
                        widget=forms.Select(
                            attrs={'class': 'form-control' ' ' 'nice-select'}),
                        required=True
                    )
                else:
                    self.fields[f'answer_{question.id}'] = forms.CharField(
                        label=question.question_text,
                        widget=forms.TextInput(
                            attrs={'class': 'form-control'}),
                        required=True
                    )


class HealthStateAnswersForm(forms.Form):
    ''' Health State Answers dynamic form. '''

    def __init__(self, *args, questions=None, **kwargs):
        super(HealthStateAnswersForm, self).__init__(*args, **kwargs)
        if questions:
            for question in questions:
                self.fields[f'answer_{question.id}'] = forms.CharField(
                    label=question.question_text,
                    widget=forms.CheckboxInput(
                        attrs={'class': 'form-check-input'}),
                    required=False
                )

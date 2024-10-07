from utils.image_validators import resize_image
import os
from django.db import models
from user_profiles.models import UserProfile
from scheduling.models import Instructor
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # The file will be uploaded to
    # MEDIA_ROOT/assets/images/physical_evaluation/<username>/<filename>

    return os.path.join(
        'assets/images/physical_evaluation',
        instance.evaluation.user.username,
        filename
    )


class BodyType(models.Model):
    ''' Body Type model. '''
    class Meta:
        verbose_name = 'Body Type'
        verbose_name_plural = 'Body Types'

    BODY_TYPE_CHOICES = [
        ('ECTOMORFO', 'Ectomorfo'),
        ('MESOMORFO', 'Mesomorfo'),
        ('ENDOMORFO', 'Endomorfo'),
    ]
    type_name = models.CharField(
        max_length=10, choices=BODY_TYPE_CHOICES, unique=True)
    ideal_weight_min = models.DecimalField(max_digits=5, decimal_places=2)
    ideal_weight_max = models.DecimalField(max_digits=5, decimal_places=2)
    ideal_body_fat_min = models.DecimalField(max_digits=5, decimal_places=2)
    ideal_body_fat_max = models.DecimalField(max_digits=5, decimal_places=2)
    total_water_min = models.DecimalField(max_digits=5, decimal_places=2)
    total_water_max = models.DecimalField(max_digits=5, decimal_places=2)
    muscle_mass_min = models.DecimalField(max_digits=5, decimal_places=2)
    muscle_mass_max = models.DecimalField(max_digits=5, decimal_places=2)
    fitness_level_min = models.IntegerField()
    fitness_level_max = models.IntegerField()
    calories_burned_min = models.IntegerField()
    calories_burned_max = models.IntegerField()
    metabolic_age_min = models.IntegerField()
    metabolic_age_max = models.IntegerField()
    bone_mass_min = models.DecimalField(max_digits=4, decimal_places=2)
    bone_mass_max = models.DecimalField(max_digits=4, decimal_places=2)
    visceral_fat_min = models.DecimalField(max_digits=4, decimal_places=2)
    visceral_fat_max = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_type_name_display()


class PhysicalEvaluation(models.Model):
    ''' Physical Evaluation model. '''
    class Meta:
        verbose_name = 'Physical Evaluation'
        verbose_name_plural = 'Physical Evaluations'

    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True,
        related_name='evaluations_instructor')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='evaluations')
    body_type = models.ForeignKey(
        BodyType, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    waist_circumference = models.DecimalField(max_digits=5, decimal_places=2)
    belly_circumference = models.DecimalField(max_digits=5, decimal_places=2)
    hip_circumference = models.DecimalField(max_digits=5, decimal_places=2)
    leg_circumference = models.DecimalField(max_digits=5, decimal_places=2)
    arm_circumference = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    total_water_percentage = models.DecimalField(
        max_digits=5, decimal_places=2)
    muscle_mass_percentage = models.DecimalField(
        max_digits=5, decimal_places=2)
    fitness_level = models.IntegerField()
    calories_burned = models.IntegerField()
    metabolic_age = models.IntegerField()
    bone_mass = models.DecimalField(max_digits=4, decimal_places=2)
    visceral_fat_percentage = models.DecimalField(
        max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    fp = models.DecimalField(max_digits=5, decimal_places=2)
    observations = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.body_type}"

    def save(self, *args, **kwargs):
        ''' Saving the physical evaluation. '''

        # Check if the instructor exists
        print('Instructor Model Save:', self.instructor)

        if not Instructor.objects.filter(id=self.instructor.id).exists():
            print('Instructor not found')
            print('Self user:', self.user)
            print('Self instructor:', self.instructor)
            instructor = Instructor.objects.first()
            self.instructor = instructor

        # Calculate the IMC
        self.imc = float(round(self.weight / (self.height ** 2), 2))
        print('IMC:', self.imc)

        # Calculate the body fat percentage
        age = self.user.profile.get_age()
        print('User:', self.user)
        print('Age:', age)
        if hasattr(self.user, 'profile') and self.user.profile.date_of_birth:
            age = self.user.profile.get_age()
            print('if Age:', age)
        else:
            age = 0  # or another default value
            print('else Age:', age)

        if self.user.profile.gender == 'M':
            self.fp = (1.20 * self.imc) + (0.23 * age) - 16.2
        else:
            self.fp = (1.20 * self.imc) + (0.23 * age) - 5.4

        super().save(*args, **kwargs)


class PhysicalEvaluationImages(models.Model):
    ''' Physical Evaluation Image model. '''
    class Meta:
        verbose_name = 'Physical Evaluation Image'
        verbose_name_plural = 'Physical Evaluation Images'

    evaluation = models.ForeignKey(
        PhysicalEvaluation, on_delete=models.CASCADE, related_name='images')
    image_front = models.ImageField(upload_to=user_directory_path)
    image_side = models.ImageField(upload_to=user_directory_path)
    image_back = models.ImageField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        ''' Saving the physical evaluation image. '''
        # Resize the images before saving
        # Obtaining the instance of the model before saving
        if self.pk:
            old_instance = PhysicalEvaluationImages.objects.get(pk=self.pk)
        else:
            old_instance = None

        # Saving the instance to get the image path before resizing
        super().save(*args, **kwargs)

        # List to store the images that need to be resized
        images_to_resize = []

        # Check if image_front was changed
        if old_instance:
            if self.image_front and (old_instance.image_front != self.image_front):
                images_to_resize.append(self.image_front)
            if self.image_side and (old_instance.image_side != self.image_side):
                images_to_resize.append(self.image_side)
            if self.image_back and (old_instance.image_back != self.image_back):
                images_to_resize.append(self.image_back)
        else:
            # If no old instance, it's a new object; resize all images
            if self.image_front:
                images_to_resize.append(self.image_front)
            if self.image_side:
                images_to_resize.append(self.image_side)
            if self.image_back:
                images_to_resize.append(self.image_back)

        # Resize the images that need to be resized
        for image in images_to_resize:
            resize_image(image, 800, True, 80)
            image.seek(0)  # Reset file pointer

        # Save again to update with resized images
        if images_to_resize:
            super().save(*args, **kwargs)

    def __str__(self):
        ''' String representation of the model. '''
        try:
            # Safely attempt to access evaluation attributes
            return f"{self.evaluation.user.username} - {self.evaluation.date}"
        except (AttributeError, PhysicalEvaluation.DoesNotExist):
            # Handle the case where evaluation is not set
            return "PhysicalEvaluationImages (no evaluation)"

    def labels(self):
        return {
            'image_front': 'Imagem da frente',
            'image_side': 'Imagem de lado',
            'image_back': 'Imagem de costas'
        }


class EatingHabitsQuestions(models.Model):
    ''' Eating Habits Questions model. '''
    class Meta:
        verbose_name = 'Eating Habits Question'
        verbose_name_plural = 'Eating Habits Questions'

    question_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question_text) if self.question_text else ''


class EatingHabitsAnswers(models.Model):
    ''' Eating Habits Answers model. '''
    ''' Respostas do questionário de hábitos alimentares '''

    ALCOHOL_CONSUMPTION_CHOICES = [
        ('Nao bebo', 'Não bebo'),
        ('Socialmente', 'Socialmente'),
        ('Moderadamente', 'Moderadamente'),
        ('Excessivamente', 'Excessivamente'),
    ]

    class Meta:
        verbose_name = 'Eating Habits Answer'
        verbose_name_plural = 'Eating Habits Answers'

    evaluation = models.ForeignKey(
        PhysicalEvaluation, on_delete=models.CASCADE,
        related_name='eating_habits', default=None)
    question = models.ForeignKey(
        EatingHabitsQuestions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.evaluation.user} - {self.question.question_text}"


class HealthStateQuestions(models.Model):
    ''' Health State Questions model. '''
    class Meta:
        verbose_name = 'Health State Question'
        verbose_name_plural = 'Health State Questions'
    question_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question_text) if self.question_text else ''


class HealthStateAnswers(models.Model):
    ''' Health State Answers model. '''
    ''' Respostas do questionário de estado de saúde '''
    class Meta:
        verbose_name = 'Health State Answer'
        verbose_name_plural = 'Health State Answers'

    evaluation = models.ForeignKey(
        PhysicalEvaluation, on_delete=models.CASCADE,
        related_name='health_state', default=None)
    question = models.ForeignKey(
        HealthStateQuestions, on_delete=models.CASCADE)
    answer = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.evaluation.user} - {self.question.question_text}"

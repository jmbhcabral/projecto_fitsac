''' User profile model. '''
from django.core.exceptions import ValidationError
from django.db import models
from utils.image_validators import resize_image


class UserProfile(models.Model):
    ''' User profile model. '''

    # Gender Definition
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Masculino'),
        (FEMALE, 'Feminino'),
        (OTHER, 'Outro')
    ]

    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='assets/frontend/images/users/',
        blank=True,
        null=True
    )
    profession = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    postal_code = models.IntegerField(
        blank=True,
        null=True
    )
    locality = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    client_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    nif = models.IntegerField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    reset_password_code = models.IntegerField(
        blank=True,
        null=True
    )
    reset_password_code_expires = models.DateTimeField(
        blank=True,
        null=True
    )
    is_instructor = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):
        ''' Save the user profile. '''

        # Generate the client number if it hasn't been set
        if not self.client_number:
            self.client_number = self.generate_client_number()

        # Resize the photo before saving (if it exists)
        if self.photo:
            current_photo_name = str(self.photo.name)
            # Resize the image only if it's a new upload
            if current_photo_name != self.photo.name:
                resize_image(self.photo, 362, True, 80)

        # Save the object (calls super() only once)
        super().save(*args, **kwargs)

    # Generate the client number
    def generate_client_number(self):
        ''' Generates a unique client number in the format FIT-XXXX '''
        last_client = UserProfile.objects.all().order_by('id').last()

        if last_client and last_client.client_number.startswith('FIT-'):
            # Extract the last client number and increment
            last_number = int(last_client.client_number.split('-')[1])
            new_number = last_number + 1
        else:
            # Start from a base number if no client numbers exist
            new_number = 1050  # or another starting point

        return f'FIT-{new_number}'

    def get_age(self):
        ''' Calculate the age of the user. '''
        from datetime import date

        if self.date_of_birth:
            today = date.today()
            born = self.date_of_birth
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return None

    def clean(self):
        errors = {}
        ''' Validate the NIF. '''
        from utils.model_validators import validar_nif

        if self.nif and not validar_nif(str(self.nif)):
            errors['nif'] = 'O NIF é inválido.'

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return str(self.user)

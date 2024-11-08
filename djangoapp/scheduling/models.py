''' Models for the scheduling app '''
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from utils.image_validators import resize_image
from utils.qr_code import generate_qr_code
import uuid
from io import BytesIO


class Instructor(models.Model):
    instructor = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='instructor',
        default=None
    )
    bio = models.TextField()

    def __str__(self):
        return str(f'{self.instructor.first_name} {self.instructor.last_name}')


class WeeklyClass(models.Model):
    DAYS_OF_WEEK = [
        (0, 'Segunda-feira'),
        (1, 'Terça-feira'),
        (2, 'Quarta-feira'),
        (3, 'Quinta-feira'),
        (4, 'Sexta-feira'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]

    title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    instructor = models.ForeignKey(
        Instructor,
        related_name='regular_instructor',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    duration = models.DurationField(
        null=False,
        blank=False,
        help_text="Duração da aula (ex. 1:30:00 para 1 hora e meia)"
    )
    day_of_week = models.IntegerField(
        choices=DAYS_OF_WEEK,
        null=False,
        blank=False
    )
    time = models.TimeField(
        null=False,
        blank=False
    )
    max_participants = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    is_visible = models.BooleanField(
        default=False
    )

    def __str__(self):
        return (
            f"{self.title} com {self.get_current_instructors()} às "
            f"{self.get_class_time(datetime.today().date())} "
            f"({self.get_day_of_week_display()})"
        )

    def get_current_instructors(self, class_date=None, time=None):
        '''
        Verifica se há um instrutor substituto para a data especificada,
        considerando o dia da semana e o horário.
        '''
        print('Getting current instructors')
        print(f"date: {class_date}, time: {time}")

        if not class_date and not time:
            class_date = self.day_of_week
            time = self.time

            return self.instructor.instructor.first_name

        if class_date and time:
            try:
                substitution = InstructorSubstitution.objects.get(
                    fitness_class=self,
                    date=class_date,
                    fitness_class__time=time
                )
                return substitution.substitute_instructor.instructor.first_name
            except InstructorSubstitution.DoesNotExist:
                return self.instructor.instructor.first_name

    def get_class_time(self, date):
        ''' Retorna o horário da aula, considerando qualquer exceção de
        horário. Se houver uma exceção para a data específica e esta aula,
        usa-se o horário da exceção; caso contrário, usa-se o horário padrão.
        '''
        try:
            exception = ClassTimeException.objects.get(
                fitness_class=self, date=date)
            return exception.new_time
        except ClassTimeException.DoesNotExist:
            return self.time


class InstructorSubstitution(models.Model):
    fitness_class = models.ForeignKey(WeeklyClass, on_delete=models.CASCADE)
    original_instructor = models.ForeignKey(
        Instructor,
        related_name='original_instructors',
        on_delete=models.SET_NULL,
        null=True
    )
    substitute_instructor = models.ForeignKey(
        Instructor,
        related_name='substitute_instructors',
        on_delete=models.SET_NULL,
        null=True
    )
    date = models.DateField()
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        ''' Save the substitution. '''
        if not self.original_instructor:
            self.original_instructor = self.fitness_class.instructor

        super().save(*args, **kwargs)

    def get_day_of_week(self):
        return self.fitness_class.day_of_week

    def get_class_time(self):
        return self.fitness_class.time

    def __str__(self):
        return (
            f'Substituição para {self.fitness_class.title} '
            f'no dia {self.date} ás { self.fitness_class.time } '
            f' com {self.substitute_instructor.instructor.first_name}'
        )


class ClassTimeException(models.Model):
    fitness_class = models.ForeignKey(WeeklyClass, on_delete=models.CASCADE)
    date = models.DateField()
    new_time = models.TimeField()

    def __str__(self):
        return (
            f"Exceção para {self.fitness_class.title} em "
            f"{self.date} às {self.new_time}"
        )


class ClassSession(models.Model):
    fitness_class = models.ForeignKey(
        WeeklyClass, on_delete=models.CASCADE, related_name='class_session')
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    participants = models.ManyToManyField(User, blank=True)
    notes = models.TextField(blank=True, null=True)
    qr_code = models.ImageField(
        upload_to='assets/class_sessions/qr_codes/', blank=True)
    session_identifier = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        ''' Saving the class session. '''
        if self.fitness_class:
            # If the instructor is not set, use the regular instructor.
            if not self.instructor:
                self.instructor = self.fitness_class.instructor

            # If the time is not set, use the regular time.
            self.time = self.fitness_class.get_class_time(self.date)

            # If the QR code is not set, generate it.
            if not self.qr_code:
                qr_data = f'{self.session_identifier}'
                img = generate_qr_code(qr_data)

                buffer = BytesIO()
                img.save(buffer, format='PNG')
                file_name = f'classsession_qr_{self.pk}.png'
                self.qr_code.save(file_name, buffer, save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f'{self.fitness_class.title} com '
            f'{self.instructor.instructor.first_name} '
            f'em {self.date} às {self.time}'
        )


class Booking(models.Model):
    fitness_class = models.ForeignKey(
        WeeklyClass,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    canceled = models.BooleanField(default=False)
    canceled_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (
            f"{self.user.username} reservou {self.fitness_class.title} "
            f"no dia {self.get_booking_date()} às {self.get_booking_time()}"
        )

    def get_booking_date(self):
        ''' Returns the date of the booking, 
        considering the day of the week of the class. '''
        created_at_date = self.created_at.date()  # pylint: disable=no-member
        weekday = created_at_date.weekday()
        days_until_class = (self.fitness_class.day_of_week - weekday) % 7
        return created_at_date + timezone.timedelta(days=days_until_class)

    def get_booking_time(self):
        ''' Returns the time of the booking,
        considering the time of the class. '''
        return self.fitness_class.get_class_time(self.get_booking_date())

    def get_class_datetime(self):
        ''' Returns the datetime of the class. '''
        class_date = self.get_booking_date()
        class_time = self.get_booking_time()
        return timezone.make_aware(datetime.combine(class_date, class_time))

    def get_canceled_status(self):
        ''' Returns the status of the booking. '''
        return 'Cancelado' if self.canceled else 'Ativo'

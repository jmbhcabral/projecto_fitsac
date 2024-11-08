''' This file contains the view for the booking form. '''

from django.views.generic.edit import FormView
from scheduling.forms import BookingForm, CancelBookingForm
from scheduling.models import WeeklyClass, Booking
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class BookingClassView(LoginRequiredMixin, FormView):
    template_name = 'user_profiles/pages/user-booking-class.html'
    form_class = BookingForm

    login_url = '/login/'

    def form_valid(self, form):
        ''' Handle the form submission. '''

        classes = form.cleaned_data.get('fitness_class')

        user = self.request.user

        # Check if classes is not None
        if not classes:
            messages.error(
                self.request, 'Nenhuma aula foi selecionada.')
            # Makes the form invalid, reloads the page with the data
            return self.form_invalid(form)

        # Converte os IDs recebidos em instâncias do modelo WeeklyClass
        bookings_to_create = []

        for class_instance in classes:

            bookings_to_create.append(
                Booking(
                    fitness_class=class_instance,
                    user=user
                )
            )

        # Verifica se há aulas para criar reservas
        if bookings_to_create:
            Booking.objects.bulk_create(bookings_to_create)
            messages.success(self.request, 'Aula(s) reservada(s) com sucesso!')
            return redirect('scheduling:user_classes_management')
        else:
            messages.error(
                self.request, 'Nenhuma aula foi encontrada ou selecionada.')

        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Handle the form submission. '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                print(f'{label}: {error}')
                messages.error(self.request, f'{label}: {error}')

        # Template reload with the form and the classes

        # Get the current timezone-aware datetime
        now = timezone.now()

        # Get the day of the week
        today_day_of_week = now.weekday()

        # Get the day of the week for tomorrow
        tomorrow_day_of_week = (today_day_of_week + 1) % 7

        # Get the current time
        current_time = now.time()

        # Get the classes that the user has booked
        booked_classes = Booking.objects.filter(
            user=self.request.user,
            canceled=False,
        ).select_related('fitness_class')

        # Filter the booked classes
        future_bookings = [
            booking.fitness_class for booking in booked_classes
            if booking.fitness_class.day_of_week == today_day_of_week
            and booking.fitness_class.time > current_time or
            booking.fitness_class.day_of_week == tomorrow_day_of_week
        ]

        # Get today's classes starting from the current time
        today_classes = WeeklyClass.objects.filter(
            day_of_week=today_day_of_week,
            time__gte=current_time,
            is_visible=True
        ).exclude(id__in=[wc.id for wc in future_bookings]).order_by('time')

        # Get tomorrow's classes starting from the current time
        tomorrow_classes = WeeklyClass.objects.filter(
            day_of_week=tomorrow_day_of_week,
            is_visible=True
        ).exclude(id__in=[wc.id for wc in future_bookings]).order_by('time')

        # Combine today's and tomorrow's classes
        classes_sorted = list(today_classes) + list(tomorrow_classes)

        # Verificar o instrutor (original ou substituto) para cada aula
        classes_with_instructors = []
        for fitness_class in classes_sorted:
            # class date is tomorrow
            class_date = timezone.now().date() + timezone.timedelta(days=1)
            # Passar a data e a hora para o método get_current_instructors
            instructor = fitness_class.get_current_instructors(
                class_date=class_date,  # Passar a data da aula
                time=fitness_class.time  # Passar o horário da aula
            )
            classes_with_instructors.append({
                'id': fitness_class.id,
                'day_of_week': fitness_class.get_day_of_week_display(),
                'fitness_class': fitness_class,
                'instructor': instructor,
                'time': fitness_class.time,
            })

        # add the form to the context
        context = self.get_context_data(form=form)

        # Add the classes to the context
        context['classes_with_instructors'] = classes_with_instructors

        # reload the page with the form and the classes
        return self.render_to_response(context)

    def get(self, request):
        ''' Handle GET requests. '''

        # Get the current timezone-aware datetime
        now = timezone.now()

        # Get the day of the week
        today_day_of_week = now.weekday()

        # Get the day of the week for tomorrow
        tomorrow_day_of_week = (today_day_of_week + 1) % 7

        # Current time
        current_time = now.time()

        # Get the classes that the user has booked
        booked_classes = Booking.objects.filter(
            user=request.user,
            canceled=False,
        ).select_related('fitness_class')

        # Filter the booked classes
        future_bookings = [
            booking.fitness_class for booking in booked_classes
            if booking.fitness_class.day_of_week == today_day_of_week
            and booking.fitness_class.time > current_time or
            booking.fitness_class.day_of_week == tomorrow_day_of_week
        ]

        # Get today's classes starting from the current time
        today_classes = WeeklyClass.objects.filter(
            day_of_week=today_day_of_week,
            time__gte=current_time,
            is_visible=True
        ).exclude(id__in=[wc.id for wc in future_bookings]).order_by('time')

        # Get tomorrow's classes
        tomorrow_classes = WeeklyClass.objects.filter(
            day_of_week=tomorrow_day_of_week,
            is_visible=True
        ).exclude(id__in=[wc.id for wc in future_bookings]).order_by('time')

        # Combine today's and tomorrow's classes
        classes_sorted = list(today_classes) + \
            list(tomorrow_classes)

        # Verificar o instrutor (original ou substituto) para cada aula
        classes_with_instructors = []
        for fitness_class in classes_sorted:
            # class date is tomorrow
            class_date = timezone.now().date() + timezone.timedelta(days=1)
            # Passar a data e a hora para o método get_current_instructors
            instructor = fitness_class.get_current_instructors(
                class_date=class_date,  # Passar a data da aula
                time=fitness_class.time  # Passar o horário da aula
            )
            classes_with_instructors.append({
                'id': fitness_class.id,
                'day_of_week': fitness_class.get_day_of_week_display(),
                'fitness_class': fitness_class,
                'instructor': instructor,
                'time': fitness_class.time,
            })

        # Add the form to the context
        context = {
            'form': self.form_class(),
            # Passa as aulas e os instrutores
            'classes_with_instructors': classes_with_instructors,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ''' Handle POST requests. '''

        form = self.form_class(request.POST)

        # Check if the form is valid
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CancelBookingView(LoginRequiredMixin, FormView):
    ''' View to cancel a booking. '''
    template_name = 'user_profiles/pages/user-booking-class-cancel.html'
    form_class = CancelBookingForm

    login_url = '/login/'

    def get(self, request):
        ''' Handle GET requests. '''

        # Get the classes for the next day
        now = timezone.now()

        # Get the classes that the user has booked
        booked_classes = Booking.objects.filter(
            user=request.user,
            canceled=False,
        )\
            .select_related('fitness_class')\
            .order_by('fitness_class__day_of_week', 'fitness_class__time')

        # Filter only classes that didn't happen yet
        future_bookings = [
            booking.fitness_class for booking in booked_classes
            if booking.get_class_datetime() > now
        ]

        # Fill the form with the classes
        form = self.form_class()

        # Update the queryset before validation
        form.fields['booking_ids'].queryset = Booking.objects.filter(
            id__in=[b.id for b in booked_classes if b.get_class_datetime()
                    > now]
        )\
            .order_by('fitness_class__day_of_week', 'fitness_class__time')

        # Add the form to the context
        context = {
            'form': form,
            'future_bookings': future_bookings,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ''' Handle POST requests. '''

        form = self.form_class(request.POST)

        # Capturing the booking IDs from the POST
        # TODO: Remove this
        # booking_ids_post = request.POST.getlist('booking_ids')

        # Fill the form with the classes
        form = self.form_class(request.POST,)

        # Get the current timezone-aware datetime
        now = timezone.now()

        # Get the classes that the user has booked
        booked_classes = Booking.objects.filter(
            user=request.user,
            canceled=False,
        ).select_related('fitness_class')

        # Update the queryset before validation
        form.fields['booking_ids'].queryset = Booking.objects.filter(
            id__in=[b.id for b in booked_classes if b.get_class_datetime()
                    > now]
        )

        # Capturing the booking IDs from the queryset
        booking_ids_queryset = form.fields['booking_ids'].queryset.values_list(
            'id', flat=True)
        print(f'Booking IDs no queryset: {list(booking_ids_queryset)}')

        # Comparar os IDs do POST com os do queryset
        # TODO: Remove this
        # ids_comparison = set(booking_ids_post).intersection(
        #     set(map(str, booking_ids_queryset)))
        # print(
        #     f'Booking IDs que coincidem entre POST e queryset: '
        #     f'{ids_comparison}')

        booking_to_cancel = None

        if form.is_valid():
            print('Form is valid')
            booking_to_cancel = form.cleaned_data.get('booking_ids')
            print(f'Booking to cancel: {booking_to_cancel}')

        # Cancel all bookings selected
        if booking_to_cancel:
            for booking in booking_to_cancel:
                print(f'Booking do for: {booking}')
                booking.canceled = True
                booking.canceled_at = timezone.now()
                booking.save()

            # Show a message to the user
            numbre_of_bookings_canceled = len(booking_to_cancel)

            if numbre_of_bookings_canceled > 1:
                messages.success(
                    self.request, (
                        f'{numbre_of_bookings_canceled} '
                        'presenças canceladas com sucesso!'
                    )
                )
            elif numbre_of_bookings_canceled == 1:
                messages.success(
                    self.request, 'Presença cancelada com sucesso!')
        else:
            for field, errors in form.errors.items():
                label = form[field].label
                for error in errors:
                    messages.error(self.request, f"{label}: {error}")
            messages.error(
                self.request, 'Nenhuma presença foi selecionada.')
            return redirect('scheduling:user_cancel_booking')

        return redirect('scheduling:user_classes_management')

    def form_invalid(self, form):
        ''' Handle the form submission. '''
        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")
        return super().form_invalid(form)

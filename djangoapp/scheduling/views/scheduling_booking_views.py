from django.shortcuts import render
from django.utils import timezone
from django.views import View
from ..models import Booking
from django.contrib.auth.mixins import LoginRequiredMixin


class ClassesNextDayView(
    LoginRequiredMixin,
    View
):
    login_url = '/login/'

    def get(self, request):
        ''' Handle GET requests. '''
        # Get the current timezone-aware datetime
        now = timezone.now()

        # Filter classes that wheren't canceled and are scheduled

        booked_classes = Booking.objects\
            .filter(
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

        # Extract associated classes from future reservations
        future_classes = [
            booking.fitness_class for booking in booked_classes
        ]

        context = {
            'future_classes': future_classes,
            'future_bookings': future_bookings,
        }

        return render(
            request,
            'user_profiles/pages/user-classes-management.html',
            context
        )

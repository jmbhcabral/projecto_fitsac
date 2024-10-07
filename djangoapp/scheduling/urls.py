''' This file contains the URL patterns for the scheduling app. '''
from django.urls import path

from scheduling.views import (
    classes_management, instructors_management,
    weekly_classes_management, instructor_create, instructor_edit,
    instructor_single_view, instructor_delete, weekly_classes_create,
    weekly_classes_single_class, weekly_classes_edit,
    weekly_classes_delete, search_users
)
from scheduling.views import (
    ClassesNextDayView, BookingClassView, CancelBookingView,
    InstructorSubstitutionsView, InstructorSubstitutionCreateView
)


app_name = 'scheduling'

urlpatterns = [
    path('scheduling/', classes_management, name='classes_management'),
    # instructors
    path('scheduling/instructors/', instructors_management,
         name='instructors_management'),
    path('scheduling/search-users/', search_users, name='search_users'),
    path('scheduling/instructors/create/', instructor_create,
         name='instructor_create'),
    path('scheduling/instructors/<int:id>/', instructor_single_view,
         name='instructor_single_view'),
    path('scheduling/instructors/edit/<int:id>/', instructor_edit,
         name='instructor_edit'),
    path('scheduling/instructors/delete/<int:id>/', instructor_delete,
         name='instructor_delete'),
    # weekly classes
    path('scheduling/weekly-classes/', weekly_classes_management,
         name='weekly_classes_management'),
    path('scheduling/weekly-classes/create/', weekly_classes_create,
         name='weekly_classes_create'),
    path('scheduling/weekly-classes/<int:class_id>/',
         weekly_classes_single_class, name='weekly_classes_single_class'),
    path('scheduling/weekly-classes/edit/<int:id>/', weekly_classes_edit,
         name='weekly_classes_edit'),
    path('scheduling/weekly-classes/delete/<int:id>/', weekly_classes_delete,
         name='weekly_classes_delete'),
    # classes next day
    path('scheduling/user-classes-management/', ClassesNextDayView.as_view(),
         name='user_classes_management'),
    # booking class
    path('scheduling/user-booking-class/', BookingClassView.as_view(),
         name='user_booking_class'),
    # cancel booking
    path('scheduling/user-cancel-booking/', CancelBookingView.as_view(),
         name='user_cancel_booking'),
    # instructor substitution
    path('scheduling/instructor-substitution/',
         InstructorSubstitutionsView.as_view(),
         name='instructor_substitution'),
    path('scheduling/instructor-substitution/create/',
         InstructorSubstitutionCreateView.as_view(),
         name='instructor_substitution_create'),

]

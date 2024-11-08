''' This file is used to register the models with the admin interface. '''
from django.contrib import admin
from scheduling.models import (
    Instructor, WeeklyClass, Booking, ClassTimeException, ClassSession,
    InstructorSubstitution
)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    ''' Admin class for the Instructor model. '''
    list_display = ('id', 'instructor', 'bio')
    search_fields = ('instructor', 'bio')
    list_filter = ('instructor', 'bio')


@admin.register(WeeklyClass)
class WeeklyClassAdmin(admin.ModelAdmin):
    ''' Admin class for the WeeklyClass model. '''
    list_display = ('title', 'instructor', 'day_of_week', 'time', 'is_visible')
    search_fields = ('title', 'instructor')
    list_filter = ('title', 'instructor')
    list_editable = ('is_visible',)


@admin.register(InstructorSubstitution)
class InstructorSubstitutionAdmin(admin.ModelAdmin):
    ''' Admin class for the InstructorSubstitution model. '''
    list_display = ('fitness_class', 'date', 'substitute_instructor')
    search_fields = ('fitness_class', 'substitute_instructor')
    list_filter = ('fitness_class', 'substitute_instructor')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ''' Admin class for the Booking model. '''
    list_display = ('id', 'fitness_class', 'user', 'created_at',
                    'canceled', 'canceled_at'
                    )
    search_fields = ('fitness_class', 'user')
    list_filter = ('fitness_class', 'user')


@admin.register(ClassTimeException)
class ClassTimeExceptionAdmin(admin.ModelAdmin):
    ''' Admin class for the ClassTimeException model. '''
    list_display = ('fitness_class', 'date', 'new_time')
    search_fields = ('fitness_class', 'date')
    list_filter = ('fitness_class', 'date')


@admin.register(ClassSession)
class ClassSessionAdmin(admin.ModelAdmin):
    ''' Admin class for the ClassSession model. '''
    list_display = ('fitness_class', 'instructor', 'date', 'time')
    search_fields = ('fitness_class', 'instructor')
    list_filter = ('fitness_class', 'instructor')

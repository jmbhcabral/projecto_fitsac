''' This file contains the views for the scheduling app. '''
from django.shortcuts import render, get_object_or_404
from scheduling.models import Instructor


def classes_management(request):
    return render(request, 'scheduling/pages/classes-management.html')


def instructors_management(request):
    instructors = Instructor.objects.all()
    if instructors:
        context = {
            'instructors': instructors
        }
        return render(
            request,
            'scheduling/pages/instructors-management.html',
            context
        )
    return render(request, 'scheduling/pages/instructors-management.html')


def instructor_single_view(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    if instructor:
        context = {
            'instructor': instructor
        }
        return render(
            request,
            'scheduling/pages/instructor-single-view.html',
            context
        )

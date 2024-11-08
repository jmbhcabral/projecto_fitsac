''' This file contains the views for the scheduling app. '''
from django.shortcuts import render, get_object_or_404, redirect
from scheduling.models import Instructor
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def instructors_management(request):

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

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


@login_required(login_url='/login/')
def instructor_single_view(request, id):

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

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

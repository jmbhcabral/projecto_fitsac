''' This module contains the views for the scheduling forms. '''

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from scheduling.forms import InstructorForm, WeeklyClassForm
from scheduling.models import Instructor, WeeklyClass
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import JsonResponse


def search_users(request):
    ''' Search for users. '''
    query = request.GET.get('q', '')

    if query:
        # Filter users by first name, last name, or email
        users = User.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
        results = [{'id': user.id, 'text': f'{user.get_full_name()} ({user.email})'}
                   for user in users]
    else:
        results = []

    return JsonResponse({'results': results})


def instructor_create(request):
    ''' Create a new instructor. '''
    action_form = reverse('scheduling:instructor_create')
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES)
        context = {
            'form': form,
            'action_form': action_form
        }
        if form.is_valid():
            # Store the instructor instance in a variable before saving it
            instructor_instance = form.save(commit=False)
            # Get the user selected in the form
            instructor_user = form.cleaned_data.get('instructor')

            # Access the user profile and set the user as the instructor
            instructor_user.profile.is_instructor = True

            # Save the user profile
            instructor_user.profile.save()

            # Save the instructor instance
            instructor_instance.save()

            messages.success(request, 'Instrutor criado com sucesso.')
            return redirect('scheduling:instructors_management')
        else:
            # Adicionar erros ao messages
            for field, errors in form.errors.items():
                label = form[field].label
                for error in errors:
                    messages.error(request, f"{label}: {error}")
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return render(
                request,
                'scheduling/pages/instructor-create.html',
                context
            )

    context = {
        'form': InstructorForm(initial={'bio': ''}),
        'action_form': action_form
    }

    return render(
        request,
        'scheduling/pages/instructor-create.html',
        context
    )


def instructor_edit(request, id):
    ''' Edit an existing instructor. '''
    instructor = get_object_or_404(Instructor, id=id)
    form_action = reverse('scheduling:instructor_edit', args=[id])
    print(f'Instructor: {instructor.instructor.id}')
    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES, instance=instructor)

        context = {
            'form': form,
            'form_action': form_action,
            'instructor': instructor
        }

        if form.is_valid():
            bio = form.cleaned_data.get('bio')
            print(f'Bio: {bio}')
            instructor_instance = form.save(commit=False)
            instructor_instance.instructor.id = instructor.instructor.id
            instructor_instance.bio = bio
            instructor_instance.save()
            print(f'Instructor: {instructor.id}')
            messages.success(request, 'Instrutor editado com sucesso.')
            return redirect('scheduling:instructors_management')
        else:
            # Adicionar erros ao messages
            for field, errors in form.errors.items():
                label = form[field].label
                for error in errors:
                    messages.error(request, f"{label}: {error}")
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return render(
                request,
                'scheduling/pages/instructor-edit.html',
                context
            )

    context = {
        'instructor': instructor,
        'form': InstructorForm(instance=instructor),
        'form_action': form_action
    }

    return render(
        request,
        'scheduling/pages/instructor-edit.html',
        context
    )


def instructor_delete(request, id):
    ''' Delete an existing instructor. '''
    instructor = get_object_or_404(Instructor, id=id)

    if request.method == 'POST':

        confirmation = request.POST.get('confirmation', 'no')

        if confirmation == 'yes':
            instructor.delete()
            messages.success(request, 'Instrutor deletado com sucesso.')
            return redirect('scheduling:instructors_management')
        else:
            messages.warning(
                request,
                'Tem certeza que deseja deletar este instrutor?'
            )
            return render(
                request,
                'scheduling/pages/instructor-single-view.html',
                {'instructor': instructor,
                 'confirmation': 'yes'}
            )

    return render(
        request,
        'scheduling/pages/instructor-single-view.html',
        {'instructor': instructor}
    )

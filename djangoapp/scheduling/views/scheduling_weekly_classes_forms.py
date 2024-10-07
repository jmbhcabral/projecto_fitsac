''' This file contains the views for the weekly classes forms. '''
from scheduling.forms import WeeklyClassForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from scheduling.models import WeeklyClass


def weekly_classes_create(request):
    ''' Create a new weekly class. '''
    form_action = reverse('scheduling:weekly_classes_create')
    if request.method == 'POST':
        form = WeeklyClassForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Aula criada com sucesso.')
            return redirect('scheduling:weekly_classes_management')

        else:
            # Adicionar erros ao messages
            for field, errors in form.errors.items():
                label = form[field].label
                for error in errors:
                    messages.error(request, f"{label}: {error}")
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return render(
                request,
                'scheduling/pages/weekly-classes-create.html',
                context
            )

    context = {
        'form': WeeklyClassForm(),
        'form_action': form_action
    }

    return render(
        request,
        'scheduling/pages/weekly-classes-create.html',
        context
    )


def weekly_classes_edit(request, id):
    ''' Edit an existing weekly class. '''
    weekly_class = get_object_or_404(WeeklyClass, id=id)
    form_action = reverse('scheduling:weekly_classes_edit', args=[id])

    if request.method == 'POST':
        form = WeeklyClassForm(
            request.POST, request.FILES, instance=weekly_class)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Aula editada com sucesso.')
            return redirect('scheduling:weekly_classes_management')
        else:
            # Adicionar erros ao messages
            for field, errors in form.errors.items():
                label = form[field].label
                for error in errors:
                    messages.error(request, f"{label}: {error}")
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return render(
                request,
                'scheduling/pages/weekly-classes-edit.html',
                context
            )

    context = {
        'form': WeeklyClassForm(instance=weekly_class),
        'form_action': form_action,
        'weekly_class': weekly_class
    }

    return render(
        request,
        'scheduling/pages/weekly-classes-edit.html',
        context
    )


def weekly_classes_delete(request, id):
    ''' Delete an existing weekly class. '''
    weekly_class = get_object_or_404(WeeklyClass, id=id)

    if request.method == 'POST':

        confirmation = request.POST.get('confirmation', 'no')

        if confirmation == 'yes':
            weekly_class.delete()
            messages.success(request, 'Aula deletada com sucesso.')
            return redirect('scheduling:weekly_classes_management')
        else:
            messages.warning(
                request, 'Tem certeza que deseja deletar esta aula?')

    return render(
        request,
        'scheduling/pages/weekly-classes-single-class.html',
        {'weekly_class': weekly_class, 'confirmation': 'yes'}
    )

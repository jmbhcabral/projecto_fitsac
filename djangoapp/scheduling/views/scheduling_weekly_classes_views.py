from django.shortcuts import render, get_object_or_404, redirect
from scheduling.models import WeeklyClass
from utils.formatters import format_duration
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def weekly_classes_management(request):
    ''' Weekly classes management page. '''

    # Check if the user is in the _admin group
    if not request.user.groups.filter(name='_admin').exists():
        return redirect('user_profiles:user_account')

    weekly_classes = WeeklyClass.objects.all().order_by('day_of_week', 'time')

    # Arrange the classes by day of the week
    classes_by_day = {}
    days_of_week = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                    'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

    for day_value, day_name in enumerate(days_of_week):
        classes_by_day[day_name] = weekly_classes.filter(day_of_week=day_value)

    context = {
        'weekly_classes': weekly_classes,
        'classes_by_day': classes_by_day,
        'days_of_week': days_of_week,
    }

    return render(request, 'scheduling/pages/weekly-classes.html', context)


@login_required(login_url='/login/')
def weekly_classes_single_class(request, class_id):
    ''' Weekly classes single class page. '''

    # Check if the user is in the _access_restricted group
    if not request.user.groups.filter(name='_access_restricted').exists():
        return redirect('user_profiles:user_account')

    weekly_class = get_object_or_404(WeeklyClass, pk=class_id)
    formatted_duration = format_duration(weekly_class.duration)

    context = {
        'weekly_class': weekly_class,
        'formatted_duration': formatted_duration
    }

    return render(
        request,
        'scheduling/pages/weekly-classes-single-class.html',
        context
    )

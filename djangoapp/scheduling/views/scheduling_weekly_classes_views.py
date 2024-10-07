from django.shortcuts import render, get_object_or_404
from scheduling.models import WeeklyClass
from utils.formatters import format_duration


def weekly_classes_management(request):
    weekly_classes = WeeklyClass.objects.all().order_by('day_of_week', 'time')

    # Organizar as aulas por dia da semana
    classes_by_day = {}
    days_of_week = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                    'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

    for day_value, day_name in enumerate(days_of_week):
        classes_by_day[day_name] = weekly_classes.filter(day_of_week=day_value)

    print('---------Debugging---------')
    for class_ in weekly_classes:
        print(class_ .instructor)

    context = {
        'weekly_classes': weekly_classes,
        'classes_by_day': classes_by_day,
        'days_of_week': days_of_week,
    }

    return render(request, 'scheduling/pages/weekly-classes.html', context)


def weekly_classes_single_class(request, class_id):
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

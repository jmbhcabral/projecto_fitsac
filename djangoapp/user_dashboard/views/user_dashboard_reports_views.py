from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from scheduling.models import ClassSession, WeeklyClass
from django.utils import timezone
from django.db.models import Count, Avg, Min, Sum, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


class UserDashboardReportsView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        TemplateView
):
    ''' View to render the user dashboard reports page '''

    template_name = 'user_dashboard/pages/reports.html'

    login_url = '/login/'

    def test_func(self):
        # Checks if the user is authenticated and if it belongs
        # to the '_access_restricted' group
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def get_context_data(self, **kwargs):
        ''' Method to get the context data '''

        # Get the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Create a list of reports
        reports = []

        # Get total number of classes and participants in a week
        today = timezone.now()
        week_start = today - timezone.timedelta(days=today.weekday())
        week_end = week_start + timezone.timedelta(days=6)

        classes_week = ClassSession.objects.filter(
            date__range=[week_start, week_end])

        total_classes_week = classes_week.count()

        total_participants_week = classes_week\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        participants_avg_week = classes_week\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        # Get the total number of classes and participants in a month
        month_start = today.replace(day=1)
        month_end = (month_start + timezone.timedelta(days=32))\
            .replace(day=1) - timezone.timedelta(days=1)

        classes_month = ClassSession.objects.filter(
            date__range=[month_start, month_end])

        total_classes_month = classes_month.count()

        total_participants_month = classes_month\
            .annotate(num_participants=Count(
                'participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        participants_avg_month = classes_month\
            .annotate(num_participants=Count(
                'participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        # Get the total number of classes in a year
        year_start = today.replace(month=1, day=1)
        year_end = today.replace(month=12, day=31)

        classes_year = ClassSession.objects.filter(
            date__range=[year_start, year_end])

        total_classes_year = classes_year.count()

        total_participants_year = classes_year\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        participants_avg_year = classes_year\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        # Get the total number of classes from the beginning
        classes = ClassSession.objects.all()

        total_classes = classes.count()

        total_participants = classes\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        participants_avg_total = classes\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        # Obtaining ids of participants who attended classes in the week
        participants_week_ids = classes_week.values_list(
            'participants', flat=True).distinct()

        # Ckeck the first session of each participant in the week
        new_students_week = (
            ClassSession.objects.filter(participants__in=participants_week_ids)
            .values('participants')  # group by participant
            .annotate(first_class=Min('date'))  # get the first class date
            # Filter who started this week
            .filter(first_class__range=[week_start, week_end])
            .count()
        )

        # Obtaining ids of participants who attended classes in the month
        participants_month_ids = classes_month.values_list(
            'participants', flat=True).distinct()

        # Ckeck the first session of each participant in the month
        new_students_month = (
            ClassSession.objects.filter(
                participants__in=participants_month_ids)
            .values('participants')  # group by participant
            .annotate(first_class=Min('date'))  # get the first class date
            # Filter who started this month
            .filter(first_class__range=[month_start, month_end])
            .count()
        )

        # Obtaining ids of participants who attended classes in the year
        participants_year_ids = classes_year.values_list(
            'participants', flat=True).distinct()

        # Ckeck the first session of each participant in the year
        new_students_year = (
            ClassSession.objects.filter(
                participants__in=participants_year_ids)
            .values('participants')  # group by participant
            .annotate(first_class=Min('date'))  # get the first class date
            # Filter who started this year
            .filter(first_class__range=[year_start, year_end])
            .count()
        )

        # Obtaining ids of participants who attended classes from the beginning
        participants_total_ids = classes.values_list(
            'participants', flat=True).distinct()

        # Ckeck the first session of each participant from the beginning
        new_students_total = (
            ClassSession.objects.filter(
                participants__in=participants_total_ids)
            .values('participants')  # group by participant
            .annotate(first_class=Min('date'))  # get the first class date
            .count()
        )

        # Populate the reports list
        reports = [
            {
                'description': 'Número de aulas',
                'week': total_classes_week,
                'month': total_classes_month,
                'year': total_classes_year,
                'total': total_classes
            },
            {
                'description': 'Média de participantes',
                'week': participants_avg_week,
                'month': participants_avg_month,
                'year': participants_avg_year,
                'total': participants_avg_total
            },
            {
                'description': 'Total de participantes',
                'week': total_participants_week,
                'month': total_participants_month,
                'year': total_participants_year,
                'total': total_participants
            },
            {
                'description': 'Novos alunos',
                'week': new_students_week,
                'month': new_students_month,
                'year': new_students_year,
                'total': new_students_total
            }
        ]

        context['reports'] = reports

        # Classes with the most participants
        weekly_classes = WeeklyClass.objects.annotate(
            participants_week=Count('class_session__participants', filter=Q(
                class_session__date__gte=week_start)),
            participants_month=Count('class_session__participants', filter=Q(
                class_session__date__gte=month_start)),
            participants_year=Count('class_session__participants', filter=Q(
                class_session__date__gte=year_start)),
            total_participants=Count('class_session__participants')
        ).order_by('-total_participants')

        context['weekly_classes'] = weekly_classes

        # Obtain students attendance data
        students_attendance = []

        # All students
        User = get_user_model()
        all_participants_dict = User.objects.all()

        # Storing attendance by week data for each student in a dictionary
        students_week_dict = {
            student['participants']: student['num_classes']
            for student in ClassSession.objects
            .filter(participants__in=participants_week_ids)
            .values('participants')
            .annotate(num_classes=Count('participants'))
        }

        # Storing attendance by month data for each student in a dictionary
        students_month_dict = {
            student['participants']: student['num_classes']
            for student in ClassSession.objects
            .filter(participants__in=participants_month_ids)
            .values('participants')
            .annotate(num_classes=Count('participants'))
        }

        # Storing attendance by year data for each student in a dictionary
        students_year_dict = {
            student['participants']: student['num_classes']
            for student in ClassSession.objects
            .filter(participants__in=participants_year_ids)
            .values('participants')
            .annotate(num_classes=Count('participants'))
        }

        # Storing attendance from the beginning data for
        # each student in a dictionary
        students_total_dict = {
            student['participants']: student['num_classes']
            for student in ClassSession.objects
            .filter(participants__in=participants_total_ids)
            .values('participants')
            .annotate(num_classes=Count('participants'))
        }

        # Creating a list of dictionaries with attendance data for each student
        for participant in all_participants_dict:
            participant_id = participant.id
            students_attendance.append({
                'name': participant.get_full_name(),
                'week': students_week_dict.get(participant_id, 0),
                'month': students_month_dict.get(participant_id, 0),
                'year': students_year_dict.get(participant_id, 0),
                'total': students_total_dict.get(participant_id, 0)
            })

        # Get the order_by parameter from the request
        order_by = self.request.GET.get('order_by', 'name_asc')

        # Define the order field on the parameter value
        if order_by == 'name_asc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['name'])

        elif order_by == 'name_desc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['name'], reverse=True)

        elif order_by == 'week_asc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['week'])

        elif order_by == 'week_desc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['week'], reverse=True)

        elif order_by == 'month_asc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['month'])

        elif order_by == 'month_desc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['month'], reverse=True)

        elif order_by == 'year_asc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['year'])

        elif order_by == 'year_desc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['year'], reverse=True)

        elif order_by == 'total_asc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['total'])

        elif order_by == 'total_desc':
            students_attendance = sorted(
                students_attendance, key=lambda x: x['total'], reverse=True)

        context['students_attendance'] = students_attendance

        return context


class UserDashboardReportsFilterView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        TemplateView
):
    ''' View to render the user dashboard reports filter page '''

    template_name = 'user_dashboard/pages/reports-filter.html'

    login_url = '/login/'

    def test_func(self):
        '''
        Checks if the user is authenticated and if it belongs
        to the '_access_restricted' group
        '''
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def get_context_data(self, **kwargs):
        ''' Method to get the context data '''

        # Get the context data from the parent class method
        context = super().get_context_data(**kwargs)

        # Get current year
        current_year = timezone.now().year

        # Generate a list of years from 2000 to the current year
        years = list(range(2000, current_year + 1))

        # Pass the years list to the context
        context['current_year'] = current_year
        context['years'] = years

        # Get the selected date or use today's
        # date as default date from the request
        selected_date_str = self.request.GET.get('selected_date')

        if selected_date_str:
            selected_date = timezone.datetime.strptime(
                selected_date_str, '%Y-%m-%d').date()
        else:
            selected_date = timezone.now().date()

        reports = []

        # Get the week start and end dates
        week_start = selected_date - \
            timezone.timedelta(days=selected_date.weekday())

        week_end = week_start + timezone.timedelta(days=6)

        # Get the month start and end dates
        month_start = selected_date.replace(day=1)

        month_end = (month_start + timezone.timedelta(days=32))\
            .replace(day=1) - timezone.timedelta(days=1)

        # Get the year start and end dates for the selected date
        year_start = selected_date.replace(month=1, day=1)
        year_end = selected_date.replace(month=12, day=31)

        # Obtain totals for daily, weekly, monthly, yearly and total
        # for selected date
        daily_total = ClassSession.objects.filter(date=selected_date).count()
        weekly_total = ClassSession.objects.filter(
            date__range=[week_start, week_end]).count()
        monthly_total = ClassSession.objects.filter(
            date__range=[month_start, month_end]).count()
        yearly_total = ClassSession.objects.filter(
            date__range=[year_start, year_end]).count()
        total_total = ClassSession.objects.count()

        # Obtain Averages participants for daily, weekly, monthly, yearly
        # and total for selected date
        daily_avg = ClassSession.objects\
            .filter(date=selected_date)\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        weekly_avg = ClassSession.objects\
            .filter(date__range=[week_start, week_end])\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        monthly_avg = ClassSession.objects\
            .filter(date__range=[month_start, month_end])\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        yearly_avg = ClassSession.objects\
            .filter(date__range=[year_start, year_end])\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        total_avg = ClassSession.objects\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Avg('num_participants'))['num_participants__avg'] or 0

        # Obtain total participants for daily, weekly, monthly, yearly and
        # total for selected date
        daily_total_participants = ClassSession.objects\
            .filter(date=selected_date)\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        weekly_total_participants = ClassSession.objects\
            .filter(date__range=[week_start, week_end])\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        monthly_total_participants = ClassSession.objects\
            .filter(date__range=[month_start, month_end])\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        yearly_total_participants = ClassSession.objects\
            .filter(date__range=[year_start, year_end])\
            .annotate(num_participants=Count('participants'))\
            .aggregate(Sum('num_participants'))['num_participants__sum'] or 0

        # Obtain ids of participants who attended classes in the day, week,
        # month, year and total for selected date
        participants_day_ids = ClassSession.objects\
            .filter(date=selected_date)\
            .values_list('participants', flat=True).distinct()

        participants_week_ids = ClassSession.objects\
            .filter(date__range=[week_start, week_end])\
            .values_list('participants', flat=True).distinct()

        participants_month_ids = ClassSession.objects\
            .filter(date__range=[month_start, month_end])\
            .values_list('participants', flat=True).distinct()

        participants_year_ids = ClassSession.objects\
            .filter(date__range=[year_start, year_end])\
            .values_list('participants', flat=True).distinct()

        participants_total_ids = ClassSession.objects\
            .values_list('participants', flat=True).distinct()

        # Obtain new students for the day, week, month, year and total
        # for selected date
        daily_new_students = ClassSession.objects\
            .filter(participants__in=participants_day_ids)\
            .values('participants')\
            .annotate(first_class=Min('date'))\
            .filter(first_class=selected_date)\
            .count()

        weekly_new_students = ClassSession.objects\
            .filter(participants__in=participants_week_ids)\
            .values('participants')\
            .annotate(first_class=Min('date'))\
            .filter(first_class__range=[week_start, week_end])\
            .count()

        monthly_new_students = ClassSession.objects\
            .filter(participants__in=participants_month_ids)\
            .values('participants')\
            .annotate(first_class=Min('date'))\
            .filter(first_class__range=[month_start, month_end])\
            .count()

        yearly_new_students = ClassSession.objects\
            .filter(participants__in=participants_year_ids)\
            .values('participants')\
            .annotate(first_class=Min('date'))\
            .filter(first_class__range=[year_start, year_end])\
            .count()

        total_new_students = ClassSession.objects\
            .filter(participants__in=participants_total_ids)\
            .values('participants')\
            .annotate(first_class=Min('date'))\
            .count()

        # Obtain distinct participants who attended classes in the day, week,
        # month, year and total for selected date
        participants_day = ClassSession.objects\
            .filter(date=selected_date)\
            .values('participants')\
            .distinct()\
            .count()

        participants_week = ClassSession.objects\
            .filter(date__range=[week_start, week_end])\
            .values('participants')\
            .distinct()\
            .count()

        participants_month = ClassSession.objects\
            .filter(date__range=[month_start, month_end])\
            .values('participants')\
            .distinct()\
            .count()

        participants_year = ClassSession.objects\
            .filter(date__range=[year_start, year_end])\
            .values('participants')\
            .distinct()\
            .count()
        participants_total = ClassSession.objects\
            .values('participants')\
            .distinct()\
            .count()

        # Populate the reports list
        reports = [
            {
                'description': 'Número de aulas',
                'day': daily_total,
                'week': weekly_total,
                'month': monthly_total,
                'year': yearly_total,
                'total': total_total
            },
            {
                'description': 'Média de participantes',
                'day': daily_avg,
                'week': weekly_avg,
                'month': monthly_avg,
                'year': yearly_avg,
                'total': total_avg
            },
            {
                'description': 'Total de participantes',
                'day': daily_total_participants,
                'week': weekly_total_participants,
                'month': monthly_total_participants,
                'year': yearly_total_participants,
                'total': yearly_total_participants
            },
            {
                'description': 'Novos alunos',
                'day': daily_new_students,
                'week': weekly_new_students,
                'month': monthly_new_students,
                'year': yearly_new_students,
                'total': total_new_students
            },
            {
                'description': 'Alunos únicos',
                'day': participants_day,
                'week': participants_week,
                'month': participants_month,
                'year': participants_year,
                'total': participants_total
            },
        ]

        # Obtain students attendance data
        students_attendance = []
        User = get_user_model()
        all_participants = User.objects.all()

        # Obtain attendance for each student in the selected period
        for participant in all_participants:
            participant_id = participant.id

            day_attendance = ClassSession.objects\
                .filter(date=selected_date, participants=participant_id)\
                .count()

            week_attendance = ClassSession.objects\
                .filter(date__range=[week_start, week_end],
                        participants=participant_id)\
                .count()

            month_attendance = ClassSession.objects\
                .filter(date__range=[month_start, month_end],
                        participants=participant_id)\
                .count()

            year_attendance = ClassSession.objects\
                .filter(date__range=[year_start, year_end],
                        participants=participant_id)\
                .count()

            students_attendance.append({
                'name': participant.get_full_name(),
                'day': day_attendance,
                'week': week_attendance,
                'month': month_attendance,
                'year': year_attendance
            })

            # atribute data to the context
            context['selected_date'] = selected_date
            context['reports'] = reports
            context['students_attendance'] = students_attendance

        return context

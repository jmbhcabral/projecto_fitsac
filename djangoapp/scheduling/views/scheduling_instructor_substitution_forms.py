''' View for the instructor substitution page forms. '''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from ..forms import InstructorSubstitutionForm
from ..models import InstructorSubstitution, Instructor, WeeklyClass
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class InstructorSubstitutionCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    View
):
    ''' View for the instructor substitution creation. '''

    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def __init__(self):
        ''' Constructor method. '''
        super().__init__()
        self.form = InstructorSubstitutionForm()
        self.template = 'scheduling/pages/instructor-substitutions-create.html'
        self.context = {
            'form': self.form,
        }

    def get(self, request):
        ''' Handle GET requests. '''
        self.context['instructors'] = Instructor.objects.all()

        # Order classes by day of week and time
        self.context['classes'] = WeeklyClass.objects.all().order_by(
            'day_of_week', 'time')

        return render(
            request,
            self.template,
            self.context
        )

    def post(self, request):
        ''' Handle POST requests. '''
        form = InstructorSubstitutionForm(request.POST)

        if form.is_valid():
            fitness_class = form.cleaned_data['fitness_class']
            substitute_instructor = form.cleaned_data['substitute_instructor']
            date = form.cleaned_data['date']
            reason = form.cleaned_data['reason']

            InstructorSubstitution.objects.create(
                fitness_class=fitness_class,
                substitute_instructor=substitute_instructor,
                date=date,
                reason=reason
            )

            messages.success(request, 'Substituição realizada com sucesso.')

            return redirect('scheduling:instructor_substitution')

        return render(
            request,
            self.template,
            self.context
        )


from ..models import InstructorSubstitution
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class InstructorSubstitutionsView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    View
):
    ''' View for the instructor substitution page. '''

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

    def get(self, request):
        ''' Handle GET requests. '''
        instructor_substitutions = InstructorSubstitution.objects.all()

        context = {
            'instructor_substitutions': instructor_substitutions,
        }

        return render(
            request,
            'scheduling/pages/instructor-substitutions.html',
            context
        )

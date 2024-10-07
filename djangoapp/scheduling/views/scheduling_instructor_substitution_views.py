
from ..models import InstructorSubstitution
from django.shortcuts import render
from django.views import View


class InstructorSubstitutionsView(View):
    ''' View for the instructor substitution page. '''

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

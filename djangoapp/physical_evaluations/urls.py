from django.urls import path
from .views import (
    UserSearchView, SingleUserView,
    BodyCompositionView, PhysicalEvaluationFormView,
    BodyCompositionSingleView, BodyCompositionUpdateView,
    PhysicalEvaluationImagesView, PhysicalEvaluationImagesFormView,
    PhysicalEvaluationImagesUpdateView, EatingHabitsView,
    EatingHabitsAswersFormView, EatingHabitsAnswersUpdateFormView,
    HealthStateView, HealthStateFormView, HealthStateAnswersUpdateFormView
)

app_name = 'physical_evaluations'

urlpatterns = [
    # Physical evaluations
    path('students-management-search/', UserSearchView.as_view(),
         name='students_management_search'),
    path('student-management-single/<int:pk>', SingleUserView.as_view(),
         name='student_management_single'),
    path('body-composition-assessment/<int:pk>', BodyCompositionView.as_view(),
         name='body_composition_assessment'),
    path('body-composition/create/<int:pk>', PhysicalEvaluationFormView.as_view(),
         name='body_composition_create'),
    path('body-composition-single/<int:pk>', BodyCompositionSingleView.as_view(),
         name='body_composition_single'),
    path('body-composition/update/<int:pk>', BodyCompositionUpdateView.as_view(),
         name='body_composition_update'),
    # Evaluation images
    path('body-composition-images/<int:pk>', PhysicalEvaluationImagesView.as_view(),
         name='evaluation_images'),
    path('body-composition-images/create/<int:pk>', PhysicalEvaluationImagesFormView.as_view(),
         name='evaluation_images_create'),
    path('body-composition-images/update/<int:pk>', PhysicalEvaluationImagesUpdateView.as_view(),
         name='evaluation_images_update'),
    # Eating habits
    path('eating-habits/<int:pk>', EatingHabitsView.as_view(),
         name='eating_habits'),
    path('eating-habits/create/<int:pk>', EatingHabitsAswersFormView.as_view(),
         name='eating_habits_create'),
    path('eating-habits/update/<int:pk>', EatingHabitsAnswersUpdateFormView.as_view(),
         name='eating_habits_update'),
    # Health state
    path('health-state/<int:pk>', HealthStateView.as_view(),
         name='health_state'),
    path('health-state/create/<int:pk>', HealthStateFormView.as_view(),
         name='health_state_create'),
    path('health-state/update/<int:pk>', HealthStateAnswersUpdateFormView.as_view(),
         name='health_state_update'),
]

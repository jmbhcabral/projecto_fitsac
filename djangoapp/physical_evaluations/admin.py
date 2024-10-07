from django.contrib import admin
from .models import (
    PhysicalEvaluation, BodyType, PhysicalEvaluationImages,
    EatingHabitsQuestions, EatingHabitsAnswers, HealthStateQuestions,
    HealthStateAnswers
)


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'ideal_weight_min', 'ideal_weight_max')
    search_fields = ('type_name', 'ideal_weight_min', 'ideal_weight_max')


@admin.register(PhysicalEvaluation)
class PhysicalEvaluationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'body_type')
    search_fields = ('user', 'date', 'body_type')


@ admin.register(PhysicalEvaluationImages)
class PhysicalEvaluationImagesAdmin(admin.ModelAdmin):
    list_display = ('evaluation', 'image_front', 'image_side', 'image_back')
    search_fields = ('evaluation', 'image_front', 'image_side', 'image_back')


@ admin.register(EatingHabitsQuestions)
class EatingHabitsQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'created_at')
    search_fields = ('question_text', 'created_at')


@ admin.register(EatingHabitsAnswers)
class EatingHabitsAnswersAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer',)


@ admin.register(HealthStateQuestions)
class HealthStateQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'created_at')
    search_fields = ('question_text', 'created_at')


@ admin.register(HealthStateAnswers)
class HealthStateAnswersAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')
    list_editable = ('answer',)

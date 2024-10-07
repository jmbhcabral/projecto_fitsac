from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile
        verbose_name = 'Perfil de Utilizador'
        verbose_name_plural = 'Perfis de Utilizadores'
    list_display = ('user', 'phone', 'photo', 'profession', 'is_instructor')
    search_fields = ('user', 'phone', 'profession', 'is_instructor')
    list_filter = ('user', 'phone', 'profession', 'is_instructor')
    readonly_fields = ('created_at', 'updated_at', 'is_instructor')
    list_editable = ('is_instructor',)

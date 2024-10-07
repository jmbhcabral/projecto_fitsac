from django.contrib import admin
from fitsac.models import (
    Contact
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ''' Admin class for the Contact model. '''
    list_display = ['name', 'email', 'subject', 'message']
    search_fields = ['name', 'email', 'subject', 'message']
    list_filter = ['name', 'email', 'subject', 'message']
    list_per_page = 10

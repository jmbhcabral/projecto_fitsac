from django.contrib import admin
from .models import Pack, Payment, Subscription, Invoice


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    ''' Pack admin '''
    list_display = ('name', 'price', 'order', 'is_active',
                    'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    list_editable = ('order', 'is_active')
    date_hierarchy = 'created_at'
    ordering = ('name',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    ''' Payment admin '''
    list_display = ('user', 'subscription', 'invoice', 'date',
                    'created_at', 'updated_at')
    search_fields = ('user', 'subscription')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    ''' Subscription admin '''
    list_display = ('user', 'pack', 'start_date',
                    'end_date', 'created_at', 'updated_at')
    search_fields = ('user', 'pack')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    ''' Invoice admin '''
    list_display = ('user', 'invoice_number', 'subscription', 'amount',
                    'status', 'invoice_date', 'created_at', 'updated_at')
    search_fields = ('user', 'subscription')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('status',)

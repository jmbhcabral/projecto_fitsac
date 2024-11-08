from collections import defaultdict
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from billing.models import Pack, Payment, Subscription, Invoice
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BillingView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Billing view '''
    template_name = 'billing/pages/billing-home.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data '''
        context = super().get_context_data(**kwargs)

        context['services'] = 'Estou na view de billing'

        return context


class PackView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Pack view '''
    template_name = 'billing/pages/billing-pack-home.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data '''
        context = super().get_context_data(**kwargs)

        packs = Pack.objects.all().order_by('order')

        context['packs'] = packs

        return context


class SubscriptionView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Subscription view '''
    template_name = 'billing/pages/billing-subscription-home.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data '''
        context = super().get_context_data(**kwargs)

        subscriptions = Subscription\
            .objects\
            .all()\
            .filter(end_date__isnull=True)\
            .order_by('created_at')

        context['subscriptions'] = subscriptions

        return context


class PaymentView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Payment view '''
    template_name = 'billing/pages/billing-payment-home.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data '''

        context = super().get_context_data(**kwargs)

        # Users with overdue payments
        users_with_overdue_payments = Invoice.objects.filter(
            status=False
        ).order_by('user__first_name', 'invoice_date')

        overdue_payments_by_user = defaultdict(list)

        # Iterate over the users with overdue payments
        for item in users_with_overdue_payments:
            overdue_payments_by_user[item.user].append(item)

        context['overdue_payments_by_user'] = overdue_payments_by_user

        # Users Search
        queryset = self.request.GET.get('q')

        # Get User model
        User = get_user_model()

        if queryset:

            # Filter users by first_name
            users = User.objects.filter(first_name__icontains=queryset)

        else:
            # If queryset is None, return an empty queryset
            users = User.objects.none()

        context['users'] = users

        return context


class PaymentUserView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    ''' Payment User view '''
    template_name = 'billing/pages/billing-payment-user.html'
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

    def get_context_data(self, **kwargs):
        ''' Get context data '''
        context = super().get_context_data(**kwargs)

        user_id = kwargs.get('pk')

        User = get_user_model()

        user = User.objects.get(pk=user_id)

        payments = Payment.objects.filter(user=user)

        late_payments = Invoice.objects.filter(
            user=user,
            status=False
        )

        context['user'] = user
        context['payments'] = payments
        context['late_payments'] = late_payments

        return context

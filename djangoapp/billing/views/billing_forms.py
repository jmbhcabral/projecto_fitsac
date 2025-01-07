from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, FormView, DeleteView
)
from billing.models import Pack, Subscription, Payment, Invoice
from billing.forms import (
    PackForm, PackOrderForm, SubscriptionForm, PaymentForm,
    PaymentUpdateForm
)
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from typing import Optional, Type
from django.db.models import QuerySet, Model


class PackCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    ''' Pack create view '''
    template_name = 'billing/pages/billing-pack-create.html'
    model = Pack
    form_class = PackForm
    success_url = reverse_lazy('billing:pack_home')
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

    def form_valid(self, form):
        ''' Form valid '''

        messages.success(self.request, 'O pacote foi criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Form invalid '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))


class PackUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    ''' Pack update view '''
    template_name = 'billing/pages/billing-pack-edit.html'
    model = Pack
    form_class = PackForm
    success_url = reverse_lazy('billing:pack_home')
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

    def form_valid(self, form):
        ''' Form valid '''

        messages.success(
            self.request,
            'O pacote foi atualizado com sucesso!'
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Form invalid '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))


class PackOrderFormView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    FormView
):
    ''' Pack order form '''
    template_name = 'billing/pages/billing-pack-order-edit.html'
    form_class = PackOrderForm
    success_url = reverse_lazy('billing:pack_home')
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

    def get_form_kwargs(self):
        ''' Pass all packs dynamically to the form '''

        kwargs = super().get_form_kwargs()

        kwargs['packs'] = self.get_packs()

        return kwargs

    def get_packs(self):
        ''' Get all current packs ordered by their current order'''

        return Pack.objects.all().order_by('order')

    def get_context_data(self, **kwargs):
        ''' Add packs to context for template rendering '''

        context = super().get_context_data(**kwargs)

        context['packs'] = self.get_packs()

        return context

    def form_valid(self, form):
        ''' Process form data to update pack order '''

        packs = self.get_packs()

        pack_bulk = []

        for pack in packs:

            # Get the order from the form for each pack
            order_value = form.cleaned_data[str(pack.id)]

            if order_value is not None and order_value != pack.order:
                pack.order = order_value
                pack_bulk.append(pack)

        # Update all packs in a single query
        Pack.objects.bulk_update(pack_bulk, ['order'])

        messages.success(
            self.request, 'A ordem dos pacotes foi atualizada com sucesso!')

        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Handle form errors '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))


class SubscriptionCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    ''' View to create a subscription '''
    template_name = 'billing/pages/billing-subscription-create.html'
    model = Subscription
    form_class = SubscriptionForm
    success_url = reverse_lazy('billing:subscription_home')
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

    def form_valid(self, form):
        ''' Form valid '''

        # Save the subscription
        self.object = form.save()

        # Generate invoice for the subscription
        self.generate_invoice_for_subscription(self.object)

        messages.success(self.request, 'A assinatura foi criada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Form invalid '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))

    def generate_invoice_for_subscription(self, subscription):
        ''' Generate invoice for the subscription '''

        # Generate invoice
        start_date = subscription.start_date
        print(f'start_date day: {start_date.day}')

        if 1 <= start_date.day <= 14:

            amount = subscription.pack.price
            status = False
        elif 15 <= start_date.day <= 23:

            amount = subscription.pack.price / 2
            status = False
        else:

            amount = 0
            status = True

        Invoice.objects.create(
            user=subscription.user,
            subscription=subscription,
            amount=amount,
            status=status,
            invoice_date=start_date
        )


class SubscriptionUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    ''' View to update a subscription '''
    template_name = 'billing/pages/billing-subscription-edit.html'
    model = Subscription
    form_class = SubscriptionForm
    success_url = reverse_lazy('billing:subscription_home')
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

    def form_valid(self, form):
        ''' Form valid '''

        messages.success(
            self.request,
            'A assinatura foi atualizada com sucesso!'
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Form invalid '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))


class PaymentCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    ''' View to create a payment '''
    template_name = 'billing/pages/billing-payment-create.html'
    model = Payment
    form_class = PaymentForm
    success_url = reverse_lazy('billing:payment_home')
    login_url = '/login/'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'groups')
            and self.request.user.groups
            .filter(name='_access_restricted').exists()
        )
    
    def get_form_kwargs(self):
        ''' Passa o utilizador ao formulário '''
        kwargs = super().get_form_kwargs()
        user_id = self.kwargs.get('pk')  # Obtém o ID do utilizador do URL
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        kwargs['user'] = user  # Passa o utilizador para o formulário
        return kwargs

    def handle_no_permission(self):
        ''' Redirect to the admin home page. '''
        return redirect('user_profiles:user_account')

    def get_context_data(self, **kwargs):
        ''' Get context data '''

        context = super().get_context_data(**kwargs)

        # Get the user from the URL
        user_id = self.kwargs.get('pk')
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)

        context['user'] = user

        return context

    def form_valid(self, form):
        ''' Form valid '''

        # Get the instance of the form
        instance = form.save(commit=False)

        # Get the user from the URL
        user_id = self.kwargs.get('pk')

        # Get the latest subscription for the user
        pack_subscription = Subscription.objects.filter(
            user=user_id).order_by('-id').first()

        # Get the invoice from the form
        invoice = form.cleaned_data.get('invoice')

        # Assign user to the payment
        instance.user = pack_subscription.user

        # Assign the subscription to the payment
        instance.subscription = pack_subscription

        # Assign the invoice to the payment
        instance.invoice = invoice

        instance.save()

        # Update the invoice status to True
        invoice.status = True
        invoice.save()

        messages.success(
            self.request,
            'O pagamento foi criado com sucesso!'
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Form invalid '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")

        return self.render_to_response(self.get_context_data(form=form))


class PaymentUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    ''' View to update a payment '''
    template_name = 'billing/pages/billing-payment-edit.html'
    model = Payment
    form_class = PaymentUpdateForm
    success_url = reverse_lazy('billing:payment_home')
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

        context['form'] = self.get_form(self.get_form_class())

        context['form'].fields['invoice'].initial = self.object.invoice

        return context

    def form_valid(self, form):
        ''' Form valid '''

        messages.success(
            self.request,
            'O pagamento foi atualizado com sucesso!'
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Form invalid '''

        for field, errors in form.errors.items():
            label = form[field].label
            for error in errors:
                messages.error(self.request, f"{label}: {error}")
        return self.render_to_response(self.get_context_data(form=form))


class PaymentDeleteView(DeleteView):
    ''' View to delete a payment '''

    model = Payment
    success_url = reverse_lazy('billing:payment_home')
    login_url = '/login/'

    # def get_object(self, queryset: Optional[QuerySet] = None) -> Payment:
    #     ''' Get the object '''
    #     return super().get_object(queryset=queryset)

    def post(self, request, *args, **kwargs):
        ''' Delete method '''

        payment = self.get_object()

        user_id = payment.user.pk

        payment.delete()

        payment.invoice.status = False

        payment.invoice.save()

        return JsonResponse({'success': True, 'user_id': user_id})

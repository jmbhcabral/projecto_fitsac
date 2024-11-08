from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction


class Pack(models.Model):
    ''' Pack model '''
    class Meta:
        ordering = ('name',)
        verbose_name = 'Pack'
        verbose_name_plural = 'Packs'

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Payment(models.Model):
    ''' Payment model '''
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    invoice = models.ForeignKey(
        'Invoice', on_delete=models.CASCADE, default=None)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f'{self.user} - {self.subscription} - {self.invoice}')


class Subscription(models.Model):
    ''' Subscription model '''

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f'{self.user} - {self.pack}')


class Invoice(models.Model):
    ''' Invoice model '''
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=255, unique=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.BooleanField(default=False)
    invoice_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        ''' Save invoice '''

        if not self.invoice_number:
            start_number = 1000

            # Get last invoice number by Invoice ID
            last_invoice = Invoice.objects.order_by('-id').first()
            if last_invoice:
                # Increment start number by 1
                start_number = int(
                    last_invoice.invoice_number.split('-')[-1]) + 1

            self.invoice_number = f'FitSac{timezone.now().year}-{start_number:04d}'

        super().save(*args, **kwargs)

    def __str__(self):
        return str(f'{self.invoice_number} - {self.get_month_name()} - {self.subscription.pack}')

    def get_month_name(self):
        MONTHS_PT = {
            1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
            5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
            9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
        }

        if self.invoice_date:
            return MONTHS_PT[self.invoice_date.month]
        else:
            return ''


def generate_invoices_for_subscriptions_without_end_date():
    ''' Generate invoices for subscriptions without end date '''

    today = timezone.now().date()
    if today.day == 1:  # Check if it's the first day of the month
        subscriptions = Subscription.objects.filter(end_date__isnull=True)

        with transaction.atomic():
            for subscription in subscriptions:
                # Check if there is already an invoice for this month
                if not Invoice.objects.filter(subscription=subscription, payment_date=today).exists():
                    Invoice.objects.create(
                        user=subscription.user,
                        subscription=subscription,
                        amount=subscription.pack.price
                    )

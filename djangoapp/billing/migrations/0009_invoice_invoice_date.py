# Generated by Django 4.2.16 on 2024-10-31 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_remove_payment_month_year_payment_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
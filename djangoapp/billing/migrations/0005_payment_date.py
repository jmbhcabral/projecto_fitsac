# Generated by Django 4.2.16 on 2024-10-17 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_pack_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

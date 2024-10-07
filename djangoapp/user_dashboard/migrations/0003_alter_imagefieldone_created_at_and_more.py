# Generated by Django 4.2.13 on 2024-05-21 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0002_imagefieldone_textfield1_textfield2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefieldone',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='textfield1',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='textfield2',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='userdashboard',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
    ]

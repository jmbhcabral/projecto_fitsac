# Generated by Django 4.2.13 on 2024-06-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0013_sectionfour_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionfour',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Ordem'),
        ),
    ]
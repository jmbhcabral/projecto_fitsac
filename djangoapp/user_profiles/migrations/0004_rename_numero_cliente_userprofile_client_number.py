# Generated by Django 4.2.16 on 2024-09-05 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='numero_cliente',
            new_name='client_number',
        ),
    ]

# Generated by Django 4.2.16 on 2024-09-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0004_rename_numero_cliente_userprofile_client_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='client_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

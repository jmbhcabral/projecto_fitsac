# Generated by Django 4.2.16 on 2024-10-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0006_remove_instructor_email_remove_instructor_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classsession',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='assets/class_sessions/qr_codes/'),
        ),
    ]

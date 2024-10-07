# Generated by Django 4.2.14 on 2024-09-05 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='assets/frontend/images/users/')),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_cliente', models.IntegerField(blank=True, null=True)),
                ('nif', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

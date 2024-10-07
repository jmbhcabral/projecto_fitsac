# Generated by Django 4.2.16 on 2024-09-21 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0004_classsession_created_at_classsession_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklyclass',
            name='substitute_instructor',
        ),
        migrations.AlterField(
            model_name='classsession',
            name='date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='InstructorSubstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fitness_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.weeklyclass')),
                ('original_instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='original_instructors', to='scheduling.instructor')),
                ('substitute_instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='substitute_instructors', to='scheduling.instructor')),
            ],
        ),
    ]
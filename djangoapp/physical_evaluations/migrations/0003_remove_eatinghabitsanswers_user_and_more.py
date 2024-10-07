# Generated by Django 4.2.16 on 2024-09-26 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0005_remove_weeklyclass_substitute_instructor_and_more'),
        ('physical_evaluations', '0002_eatinghabitsquestions_healthstatequestions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eatinghabitsanswers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='healthstateanswers',
            name='user',
        ),
        migrations.AddField(
            model_name='eatinghabitsanswers',
            name='evaluation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='eating_habits', to='physical_evaluations.physicalevaluation'),
        ),
        migrations.AddField(
            model_name='healthstateanswers',
            name='evaluation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='health_state', to='physical_evaluations.physicalevaluation'),
        ),
        migrations.AddField(
            model_name='physicalevaluation',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluations_instructor', to='scheduling.instructor'),
        ),
    ]
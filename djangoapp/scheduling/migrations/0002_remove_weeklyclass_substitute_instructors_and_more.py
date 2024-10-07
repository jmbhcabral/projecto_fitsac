# Generated by Django 4.2.14 on 2024-09-01 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklyclass',
            name='substitute_instructors',
        ),
        migrations.AddField(
            model_name='weeklyclass',
            name='substitute_instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='substitute_instructors', to='scheduling.instructor'),
        ),
        migrations.AlterField(
            model_name='weeklyclass',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='regular_instructor', to='scheduling.instructor'),
        ),
    ]

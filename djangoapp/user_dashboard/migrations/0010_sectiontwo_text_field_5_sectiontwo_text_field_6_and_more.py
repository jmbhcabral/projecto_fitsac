# Generated by Django 4.2.13 on 2024-06-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0009_alter_card_options_alter_offersicons_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectiontwo',
            name='text_field_5',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Header da foto 2'),
        ),
        migrations.AddField(
            model_name='sectiontwo',
            name='text_field_6',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Paragrafo da foto 2'),
        ),
        migrations.AlterField(
            model_name='sectiontwo',
            name='text_field_3',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Header foto 1'),
        ),
        migrations.AlterField(
            model_name='sectiontwo',
            name='text_field_4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Paragrafo foto 1'),
        ),
    ]

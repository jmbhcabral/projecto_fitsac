# Generated by Django 4.2.13 on 2024-07-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0015_remove_sectionone_image_sectionone_image_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingoffers',
            name='name',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Nome da Oferta'),
        ),
    ]

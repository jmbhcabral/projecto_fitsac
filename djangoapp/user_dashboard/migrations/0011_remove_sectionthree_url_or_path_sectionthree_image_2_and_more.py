# Generated by Django 4.2.13 on 2024-06-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0010_sectiontwo_text_field_5_sectiontwo_text_field_6_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionthree',
            name='url_or_path',
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='assets/frontend/images/section_3/images/', verbose_name='Imagem 2 de Secção 3'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='assets/frontend/images/section_3/images/', verbose_name='Imagem 3 de Secção 3'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='section_header',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Header da Secção 3'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='text_field_1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Header da foto 1'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='text_field_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Paragrafo da foto 1'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='text_field_3',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Header da foto 2'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='text_field_4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Paragrafo da foto 2'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='url_or_path_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL ou caminho da foto 1'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='url_or_path_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL ou caminho da foto 2'),
        ),
        migrations.AddField(
            model_name='sectionthree',
            name='url_or_path_3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL ou caminho da foto 3'),
        ),
        migrations.AlterField(
            model_name='sectionthree',
            name='text_field_5',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Header da foto 3'),
        ),
        migrations.AlterField(
            model_name='sectionthree',
            name='text_field_6',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Paragrafo da foto 3'),
        ),
    ]
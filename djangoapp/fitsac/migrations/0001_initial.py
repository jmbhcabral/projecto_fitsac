# Generated by Django 4.2.14 on 2024-08-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Escreva o seu Nome.', max_length=100)),
                ('email', models.EmailField(help_text='Escreva o seu Email.', max_length=150)),
                ('subject', models.CharField(help_text='Escreva o Assunto.', max_length=100)),
                ('message', models.TextField(help_text='Escreva a sua Mensagem.', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
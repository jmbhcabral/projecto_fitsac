# Generated by Django 4.2.14 on 2024-08-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0019_alter_sectionnine_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposDeAulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='Escreva o tipo de aula.', max_length=100)),
                ('description', models.TextField(help_text='Escreva a Descrição.', max_length=500)),
                ('image', models.ImageField(help_text='Escolha a Imagem.', upload_to='tipos_de_aulas')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=25)),
                ('endereco', models.CharField(max_length=70)),
            ],
        ),
    ]

# Generated by Django 5.2.2 on 2025-06-25 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventosEmpresa', '0002_alter_eventosempresa_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventosempresa',
            options={'managed': False, 'ordering': ['eventos_descricao_titulo']},
        ),
    ]

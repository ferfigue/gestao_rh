# Generated by Django 4.0.1 on 2022-01-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extras', '0004_registrohoraextra_date_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

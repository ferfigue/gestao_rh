# Generated by Django 4.0.1 on 2022-01-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extras', '0005_alter_registrohoraextra_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
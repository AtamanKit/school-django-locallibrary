# Generated by Django 5.0.5 on 2024-05-09 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='data_of_birth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='data_of_death',
            new_name='date_of_death',
        ),
    ]
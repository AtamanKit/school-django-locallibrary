# Generated by Django 5.0.5 on 2024-05-15 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_maark_returned', 'Set book as returned'),)},
        ),
    ]
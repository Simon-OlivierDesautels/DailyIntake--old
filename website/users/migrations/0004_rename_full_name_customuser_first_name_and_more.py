# Generated by Django 4.1.2 on 2022-10-08 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_full_name_customuser_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='last_name',
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vue_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeeName',
            new_name='Name',
        ),
    ]
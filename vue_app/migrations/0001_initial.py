# Generated by Django 2.2.12 on 2021-10-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('Description', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
            ],
        ),
    ]
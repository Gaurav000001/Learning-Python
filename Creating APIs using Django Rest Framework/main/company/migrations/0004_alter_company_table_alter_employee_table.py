# Generated by Django 4.2.4 on 2023-08-13 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_rename_company_id_employee_company'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='company',
            table='companies',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employees',
        ),
    ]

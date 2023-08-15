# Generated by Django 4.2.4 on 2023-08-12 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phoneNo', models.CharField(max_length=10)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('Software Engineer', 'SE'), ('Manager', 'manager'), ('Project Lead', 'PL')], max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
# Generated by Django 4.1 on 2022-09-12 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organisation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(default=0)),
                ('organisation_name', models.CharField(max_length=100)),
                ('organisation_address', models.JSONField()),
                ('organisation_location', models.CharField(max_length=100)),
                ('number_of_employees', models.IntegerField()),
                ('annual_turn_over', models.BigIntegerField()),
                ('capital_amount', models.BigIntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('te_id', models.IntegerField(primary_key=True, serialize=False)),
                ('join_date', models.DateTimeField(default=0)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_department', models.CharField(max_length=100)),
                ('employee_address', models.JSONField()),
                ('employee_salary', models.BigIntegerField()),
                ('designation', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('organisation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeapp.organization')),
            ],
            options={
                'db_table': 'Employees',
            },
        ),
    ]

from django.db import models

# Create your models here.

class Organization(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    start_date = models.DateField(default=0)
    organization_name = models.CharField(max_length=100)
    organization_address = models.JSONField()
    organization_location = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    annual_turn_over = models.BigIntegerField()
    capital_amount = models.BigIntegerField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'Organization'

class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    organization_id = models.ForeignKey(Organization,on_delete=models.CASCADE)
    join_date = models.DateTimeField(default=0)
    employee_name = models.CharField(max_length=100)
    employee_department = models.CharField(max_length=100)
    employee_address = models.JSONField()
    employee_salary = models.BigIntegerField()
    designation = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'Employees'
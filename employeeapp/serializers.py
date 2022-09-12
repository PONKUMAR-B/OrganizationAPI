from dataclasses import fields
from .models import Employees, Organization
from rest_framework import serializers

# create a organisation field serializer
class OrganizationDetails(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

# create a Employees field serializer
class EmployeesDetails(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
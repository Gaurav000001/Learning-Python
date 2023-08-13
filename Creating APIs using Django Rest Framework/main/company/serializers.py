from rest_framework import serializers
from company.models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"
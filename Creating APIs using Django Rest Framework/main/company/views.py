from django.shortcuts import render
from django.http import request
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from company.models import Company, Employee
from company.serializers import CompanySerializer, EmployeeSerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    # This function fill be called using primary key which by default None and which is refering to company_id
    # http://localhost:8000/companies/{company_id}/employees/
    @action(detail=True, methods=['GET'])
    def employees(self, request, pk = None):
        try:
            company = Company.objects.get(pk = pk)
            employees = Employee.objects.filter(company = company)
            
            employees_serialized = EmployeeSerializer(employees, many = True, context = {'request': request})
            return Response(employees_serialized.data)
        
        except Company.DoesNotExist:
            return Response({
                'message': 'Invalid companyId provided'
            }, status=status.HTTP_404_NOT_FOUND)  # Change the status code here for a "Not Found" scenario
        except Exception as e:
            return Response({
                'message': 'An error occurred'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Change the status code here for a generic error




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
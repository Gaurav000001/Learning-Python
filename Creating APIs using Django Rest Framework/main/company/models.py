from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=
                            (
                                ('IT', 'IT'),
                                ('Sales', 'Sales'),
                                ('Marketing','Marketing'),
                                ('Auto Mobiles', 'Auto Mobiles')
                            ))
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.company_name
    
    # Specifying the custom table name
    class Meta:
        db_table = 'companies'
    

class Employee(models.Model):
    employee_id  = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    address = models.TextField()
    phoneNo = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=20, choices=
                                (('Software Engineer', 'SE'),
                                ('Manager', 'manager'),
                                ('Project Lead', 'PL')))
    salary = models.DecimalField(decimal_places=2, max_digits=7)
    
    # Establishing relationship here
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    # Specifying the custom table name
    class Meta:
        db_table = 'employees'
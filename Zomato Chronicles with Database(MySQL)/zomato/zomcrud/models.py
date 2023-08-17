from django.db import models

# Create your models here.
class Dishes(models.Model):
    class Meta:
        db_table = 'dishes'
    
    dishID = models.AutoField('Order ID', primary_key=True, unique=True,)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # max_digits and decimal_places attributes are mandatory to use
    image = models.ImageField(upload_to="dish_images")
    is_available = models.BooleanField(default=False)
    
    
    
    
class Orders(models.Model):
    class Meta:
        db_table = 'orders'
        
    orderID = models.AutoField('Order ID', primary_key=True, unique=True,)
    customer_name = models.CharField(max_length=50)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2)
    
    ORDER_CHOICES = (
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready to pickup', 'Ready to Pickup'),
        ('delivered', 'Delivered')
    )
    
    order_status = models.CharField(max_length=50, choices=ORDER_CHOICES, default='received')
    
    dishes = models.ManyToManyField('Dishes', related_name='Orders', blank=True)
    

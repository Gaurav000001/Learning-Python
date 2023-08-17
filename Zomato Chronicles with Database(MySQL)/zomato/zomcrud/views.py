from django.shortcuts import render, redirect
from .models import Dishes, Orders

# Create your views here.
def home(request):
    return render(request, 'base.html')

def menu(request):
    
    dishes = Dishes.objects.all()
    
    return render(request, 'menu.html', context={'dishes': dishes})


def add_dish(request):
    
    if request.method == "POST":
        
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        image = request.FILES.get('image')
        is_available = data.get('is_available') == 'on'
        
        Dishes.objects.create(
            name = name,
            description = description,
            price = int(price),
            image = image,
            is_available = is_available
        )
        
        return redirect('/menu')
        # If we don't redirect it, it will try to persist data to the database when doing hard refresh.
    
    return render(request, "add_dish.html")


def delete_dish(request, dishID):
    
    dish = Dishes.objects.get(dishID = dishID)
    dish.delete()
    
    return redirect('/menu')

def update_availability(request, dishID, is_available):
    
    dish = Dishes.objects.filter(dishID = dishID).update(is_available = False if is_available == 'True' else True)
    
    return redirect('/menu')
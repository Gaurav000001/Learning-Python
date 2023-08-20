from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Dishes, Orders

# Create your views here.
def home(request):
    return render(request, 'base.html')

def search(request, page):
    
    dishes = Dishes.objects.filter(name__icontains = request.GET.get('search'))
    
    if len(dishes) == 0:
        return None
    else:
        return render(request, page+'.html', context={'dishes': dishes})

def menu(request):
    
    dishes = Dishes.objects.all()
    
    if request.GET.get('search'):
        search_results = search(request, 'menu')
        if search_results is not None:
            return search_results
    
    else:
        return render(request, 'menu.html', context={'dishes': dishes})


def add_dish(request):
    if request.GET.get('search'):
        search_results = search(request, 'menu')
        if search_results is not None:
            return search_results
    
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


def update_dish(request, dishID):
    
    if request.GET.get('search'):
        search_results = search(request, 'menu')
        if search_results is not None:
            return search_results
    
    dish = Dishes.objects.get(dishID = dishID)
    
    if request.method == "POST":
        
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        image = request.FILES.get('image')
        is_available = data.get('is_available') == 'on'
        
        dish.name = name
        dish.description = description
        dish.price = price
        dish.is_available = is_available
        
        if image is not None:
            dish.image = image
            
        dish.save()
            
        return redirect('/menu')
        
    return render(request, 'update_dish.html', context={'dish': dish})
    
    
    
    
def order_items(request):
    
    if request.GET.get('search'):
        search_results = search(request, 'order_items')
        if search_results is not None:
            return search_results
    
    if request.method == 'POST':
        # Get the selected dish IDs from the form
        selected_dish_ids = request.POST.getlist('selected_dishes')
        customer_name = request.POST.get('customer_name')
        
        # Query the database to check if all selected dishes are available
        available_dishes = Dishes.objects.filter(dishID__in=selected_dish_ids, is_available=True)
        
        if available_dishes.count() == len(selected_dish_ids):
            # All selected dishes are available, proceed with the order
            
            # Calculate the total bill based on the selected dishes' prices
            total_bill = sum(dish.price for dish in available_dishes)

            # Create an Order instance
            order = Orders.objects.create(
                customer_name = customer_name,
                total_bill = total_bill
            )

            # Add the selected dishes to the order
            order.dishes.set(available_dishes)
            
            return redirect('orders')
        
        else:
            # Not all selected dishes are available
            # You can handle this case accordingly, for example, by showing an error message
            return JsonResponse({"Error": 'Some Dishes are not available, please order carefully!!'}, status=400)
        

    dishes = Dishes.objects.all()
    return render(request, 'order_items.html', {'dishes': dishes})
    

def orders(request):
    
    orders = Orders.objects.all()
    
    return render(request, 'orders.html', context={"orders": orders})


def order_details(request, orderID):
    
    order = Orders.objects.get(orderID = orderID)
    
    if order:
        dishes = order.dishes.all()
        
        return render(request, 'order_details.html', context={"dishes": dishes})
    
    else:
        return JsonResponse({"Error": 'Wrong orderID entered'}, status=400)
    

def update_order_status(request, orderID):
    
    order = Orders.objects.get(orderID = orderID)
    
    if order:
        current_status = order.order_status
        print(current_status)
        
        if current_status != 'delivered':
            order_statuses = ['received', 'preparing', 'ready to pickup', 'delivered']
            order.order_status = order_statuses[order_statuses.index(current_status) + 1]
            order.save()
        
    return redirect('orders')
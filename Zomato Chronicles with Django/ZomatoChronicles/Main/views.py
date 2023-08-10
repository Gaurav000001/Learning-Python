from django.shortcuts import render
from django.http import *
import json
import os

data = {}
# Get the path to the JSON file relative to your project's root directory
file = os.path.join(os.path.dirname(__file__), 'data', 'data.json')


def load_data():
    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return {}



def add_dish(request):
    
    data = load_data()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        available = request.POST.get('available')

        if name and price and available:  # Basic data validation
            try:
                with open(file, 'r') as json_file:
                    data = json.load(json_file)
                    
                # Convert string to boolean
                available = available.lower() == 'true'

                dish = {
                    'name': name,
                    'price': price,
                    'available': available
                }

                menu = data['menu']
                dish_id = str(data['ids']['dish_id'])
                menu[dish_id] = dish
                data['ids']['dish_id'] += 1

                with open(file, 'w') as json_file:
                    json.dump(data, json_file, indent=4)

                return JsonResponse({'message': 'Dish added successfully'})

            except FileNotFoundError:
                return HttpResponseServerError('Data file not found')
            except PermissionError:
                return HttpResponseServerError('Permission denied. Unable to write to JSON file.')
            except json.JSONDecodeError:
                return HttpResponseServerError('Error decoding JSON file')
            except Exception as e:
                return HttpResponseServerError(f'An error occurred: {e}')
        else:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    return render(request, "add_dish.html")




def remove_dish(request, dish_id):
    
    data = load_data()
    
    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return HttpResponseServerError('Data file not found')
    except json.JSONDecodeError:
        return HttpResponseServerError('Error decoding JSON file')

    menu = data.get('menu', {})

    if not dish_id:
        return HttpResponseBadRequest('Missing dish_id')

    if dish_id in menu:
        dish = menu[dish_id]
        name = dish.get('name')

        try:
            del menu[dish_id]
            with open(file, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            return JsonResponse({'message': f'Dish "{name}" removed from menu successfully'})

        except PermissionError:
            return HttpResponseServerError('Permission denied. Unable to write to JSON file.')
        except Exception as e:
            return HttpResponseServerError(f'An error occurred: {e}')

    else:
        return JsonResponse({'error': f'Dish with Dish ID: {dish_id} is not present in the Menu'}, status=404)




def update_availability(request):
    
    data = load_data()
    
    if request.method == 'POST':

        try:
            with open(file, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return HttpResponseServerError('Data file not found')
        except json.JSONDecodeError:
            return HttpResponseServerError('Error decoding JSON file')

        menu = data.get('menu', {})
        dish_id = request.POST.get('dish_id')
        available = True if request.POST.get('available').lower() == 'true' else False

        if not dish_id:
            return HttpResponseBadRequest('Missing dish_id')

        if dish_id in menu:
            dish = menu[dish_id]
            name = dish.get('name')

            # Validate 'available' input
            if available is None or not isinstance(available, bool):
                return HttpResponseBadRequest('Invalid "available" value')

            dish['available'] = available

            try:
                with open(file, 'w') as json_file:
                    json.dump(data, json_file, indent=4)

                return JsonResponse({'message': f'Availability status for Dish "{name}" updated successfully'})

            except PermissionError:
                return HttpResponseServerError('Permission denied. Unable to write to JSON file.')
            except Exception as e:
                return HttpResponseServerError(f'An error occurred: {e}')

        else:
            return JsonResponse({'error': f'Dish with Dish ID: {dish_id} is not present in the Menu'}, status=404)
    
    return render(request, "update_availability.html")

def display_menu(request):
    
    data = load_data()
    
    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return render(request, 'error.html', {'message': 'Data file not found'})
    except json.JSONDecodeError:
        return render(request, 'error.html', {'message': 'Error decoding JSON file'})

    menu = data.get('menu', {})

    menu_items = []
    for dish_id, dish in menu.items():
        name = dish.get('name')
        price = dish.get('price')
        available = dish.get('available')

        menu_items.append({
            'id': dish_id,
            'name': name,
            'price': price,
            'availability': 'Available' if available else 'Not Available'
        })

    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)



def take_order(request):
    
    data = load_data()
    
    try:
        if request.method == 'POST':
            customer_name = request.POST.get('customer_name')
            input_line = request.POST.get('dish_ids')
            dish_ids = [x for x in input_line.split()]
            menu = data.get('menu', {})
            orders = data.get('orders', {})
            new_order = {}
            bill_price = 0
            
            new_order['customer_name'] = customer_name
            new_order['bill_price'] = 0
            new_order['dish_n_prices'] = []
            dish_n_prices = new_order['dish_n_prices']
            
            for dish_id in dish_ids:
                if dish_id in menu:
                    dish = menu[dish_id]
                    dish_name = dish.get('name')
                    dish_price = dish.get('price')
                    dish_available = dish.get('available')
                    
                    if dish_available == False:
                        return JsonResponse({'error': f'Dish with Dish ID: {dish_id} not available'})
                    
                    dish_n_price = [dish_id, dish_name, dish_price]
                    dish_n_prices.append(dish_n_price)
                    
                    bill_price += dish_price
                    
                else:
                    return JsonResponse({'error': f'Dish with Dish ID: {dish_id} not available'})
            
            if bill_price > 0:
                new_order['bill_price'] = bill_price
                new_order['status'] = "received"
                order_id = data['ids']['order_id']
                data['ids']['order_id'] = int(order_id) + 1
                
                order_id = str(order_id)
                orders[order_id] = new_order
                
                try:
                    with open(file, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    
                    return JsonResponse({'message': 'Order placed successfully!'})
                except PermissionError:
                    return JsonResponse({'error': 'Permission denied. Unable to write to JSON file.'})
                except Exception as e:
                    return JsonResponse({'error': f'An error occurred: {e}'})
            
            else:
                return JsonResponse({'error': 'No items were added.'})
        
    except Exception as e:
        return JsonResponse({'error': 'Invalid input, please try again'})
    
    return render(request, 'take_order.html')



def update_order_status(request, order_id):
    
    data = load_data()
    
    try:
        if request.method == 'POST':
            orders = data.get('orders', {})
            
            if order_id in orders:
                order = orders[order_id]
                previous_status = order.get('status')
                status = request.POST.get('status', 'received')
                order['status'] = status
                
                try:
                    with open(file, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    
                    return JsonResponse({'message': f'Status Updated from {previous_status} to {status} successfully!'})
                except PermissionError:
                    return JsonResponse({'error': 'Permission denied. Unable to write to JSON file.'})
                except Exception as e:
                    return JsonResponse({'error': f'An error occurred: {e}'})
                
            else:
                return JsonResponse({'error': f'Order with Order ID: {order_id} not found...'})
        
    except Exception as e:
        return JsonResponse({'error': 'An error occurred'})
    
    return render(request, "update_order_status.html")




def display_orders(request):
    
    data = load_data()
    
    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return render(request, 'error.html', {'message': 'Data file not found'})
    except json.JSONDecodeError:
        return render(request, 'error.html', {'message': 'Error decoding JSON file'})

    orders = data.get('orders', {})

    order_list = []
    for order_id, order in orders.items():
        customer_name = order.get('customer_name')
        bill_price = order.get('bill_price')
        status = order.get('status')

        order_list.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'bill_price': bill_price,
            'status': status,
        })

    context = {'order_list': order_list}
    return render(request, 'orders.html', context)

        
        
        
def review_orders(request):
    
    data = load_data()
    
    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return render(request, 'error.html', {'message': 'Data file not found'})
    except json.JSONDecodeError:
        return render(request, 'error.html', {'message': 'Error decoding JSON file'})

    orders = data.get('orders', {})

    order_list = []
    for order_id, order in orders.items():
        customer_name = order.get('customer_name')
        dish_n_prices = order.get('dish_n_prices', [])
        bill_price = order.get('bill_price')
        status = order.get('status')

        dish_list = []
        for dish_id, dish_name, dish_price in dish_n_prices:
            dish_list.append({
                'dish_id': dish_id,
                'dish_name': dish_name,
                'dish_price': dish_price
            })

        order_list.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'dish_list': dish_list,
            'bill_price': bill_price,
            'status': status
        })

    context = {'order_list': order_list}
    return render(request, 'review_orders.html', context)
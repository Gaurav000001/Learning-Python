import json

# Sample menu and orders (you can use your own data from previous tasks)
data = {}
round = 1


def load_data():
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return {}



def add_dish(name, price, available):
    dish = {
        'name': name,
        'price': price,
        'available': available
    }
    menu = data['menu']
    
    id = data['ids']['dish_id']
    data['ids']['dish_id'] = id + 1
    
    menu[id] = dish
    
    try:
        # Attempt to write data to a JSON file
        # While opening the file to write on it, if not found, file will be automatically created
        with open('data.json', 'w') as json_file:
            # indent is added to make the file format more readable
            json.dump(data, json_file, indent=4)

    except PermissionError:
        print("Error: Permission denied. Unable to write to JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_dish(dish_id):
    
    menu = data['menu']
    
    if dish_id in menu:
        
        dish = menu[dish_id]
        name = dish['name']
        del menu[dish_id]
        
        try:
            # Attempt to write data to a JSON file
            # While opening the file to write on it, if not found, file will be automatically created
            with open('data.json', 'w') as json_file:
                # indent is added to make the file format more readable
                json.dump(data, json_file, indent=4)

                print(f"Dish:- {name} is Removed From Menu successfully!!")
                
        except PermissionError:
            print("Error: Permission denied. Unable to write to JSON file.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
    else:
        print(f"Dish with Dish ID: {dish_id} is not present in the Menu!!")

def update_availability(dish_id, available):
    
    menu = data['menu']
    
    if dish_id in menu:
        
        dish = menu[dish_id]
        name = dish['name']
        dish['available'] = available
        
        try:
            # Attempt to write data to a JSON file
            # While opening the file to write on it, if not found, file will be automatically created
            with open('data.json', 'w') as json_file:
                # indent is added to make the file format more readable
                json.dump(data, json_file, indent=4)

                print(f"Availability status for Dish:- {name} is updated successfully!!")
                
        except PermissionError:
            print("Error: Permission denied. Unable to write to JSON file.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    else:
        print(f"Dish with Dish ID: {dish_id} is not present in the Menu!!")

def display_menu():
    print("\n-----------------   Menu:  ------------------")
    
    menu = data['menu']
    
    for id in menu:
        
        dish = menu[id]
        name = dish['name']
        price = dish['price']
        available = dish['available']
        
        print(f"\n~ Id:- {id}\n~ Dish:- {name}\n~ Price:- {price}\n~ Availability:- ({'Available' if available else 'Not Available'})")



def take_order():
    try:
        
        customer_name = str(input("Enter your Name: "))
        input_line = input("Enter Dish IDs separated by spaces: ")
        dish_ids = [x for x in input_line.split()]
        menu = data['menu']
        orders = data['orders']
        new_order = {}
        bill_price = 0
        
        new_order['customer_name'] = customer_name
        new_order['bill_price'] = 0
        new_order['dish_n_prices'] = []
        dish_n_prices = new_order['dish_n_prices']
        
        
        for dish_id in dish_ids:
            if dish_id in menu:
                
                dish = menu[dish_id]
                dish_name = dish['name']
                dish_price = dish['price']
                dish_available = dish['available']
                
                if dish_available == False:
                    print(f"Dish with Dish ID: {dish_id} not available..")
                    continue
                
                dish_n_price = [dish_id, dish_name, dish_price]
                dish_n_prices.append(dish_n_price)
                
                bill_price += dish_price
                
            else:
                print(f"Dish with Dish ID: {dish_id} not available..")
        
        # Add it to orders only if the bill price is greater than 0 means customer has ordered something
        if bill_price > 0:
            
            new_order['bill_price'] = bill_price
            new_order['status'] = "received"
            order_id = data['ids']['order_id']
            data['ids']['order_id'] = int(order_id) + 1
            
            orders[order_id] = new_order
            
            try:
                # Attempt to write data to a JSON file
                # While opening the file to write on it, if not found, file will be automatically created
                with open('data.json', 'w') as json_file:
                    # indent is added to make the file format more readable
                    json.dump(data, json_file, indent=4)
                
                print("Order placed successfully!")
            except PermissionError:
                print("Error: Permission denied. Unable to write to JSON file.")
            except Exception as e:
                print(f"An error occurred: {e}")
        
        
        else:
            print('No items were added.')
        
        
    except:
        print("Invalid input, please try again")
        return

def update_order_status(order_id, status):
    
    orders = data['orders']
    
    if order_id in orders:
        order = orders[order_id]
        previous_status = order['status']
        order['status'] = status
        
        try:
            # Attempt to write data to a JSON file
            # While opening the file to write on it, if not found, file will be automatically created
            with open('data.json', 'w') as json_file:
                # indent is added to make the file format more readable
                json.dump(data, json_file, indent=4)

                print(f"Status Updated from {previous_status} to {status} successfully!!")
                
        except PermissionError:
            print("Error: Permission denied. Unable to write to JSON file.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    else:
        print(f"Dish with Dish ID: {dish_id} is not present in the Menu!!")
        
        
        
def review_orders():
    print("\n-----------------   Orders:  ------------------")
    orders = data['orders']
    
    for id in orders:
        
        order = orders[id]
        customer_name = order['customer_name']
        dish_n_prices = order['dish_n_prices']
        bill_price = order['bill_price']
        status = order['status']
        
        print(f"\n~ Order ID:- {id}\n~ Customer Name:- {customer_name}")
        
        for i in range(len(dish_n_prices)):
            dish_id, dish_name, dish_price = dish_n_prices[i]
            
            print(f"~~~ Dish ID:- {dish_id}\n~~~ Dish:- {dish_name}\n~~~ Price:- {dish_price}")
            
        print(f"~ Bill:- {bill_price}\n~ status:- {status}")




# Load data from file
data = load_data()


while True:
    if round == 1:
        print("------------------------------------------------------------------")
        print("================== Welcome To Zesty Zomato =======================")
        print("------------------------------------------------------------------")

    print("*******")
    print("1. Add Dish to Menu")
    print("2. Update Dish Availability")
    print("3. Delete Dish from Menu")
    print("4. Take Order")
    print("5. Update Order Status")
    print("6. View Orders")
    print("7. Display Menu")
    print("8. Exit")
    print("*******")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
           try:
               
                name = input("Enter Dish Name: ")
                price = float(input("Enter Dish Price: "))
                available = input("Is Dish Available? (yes/no): ").lower() == "yes"
                add_dish(name, price, available)
                print("Dish added successfully!")
               
           except:
               print("Invalid Input, Please try again later...")

        elif choice == 2:
            try:
                
                dish_id = int(input("Enter Dish ID to update availability: "))
                available = input("Set Dish Availability? (yes/no): ").lower() == "yes"
                update_availability(str(dish_id), (True if "yes" else False))
                
            except:
                print("Invalid Input, Please try again later...")
        
        elif choice == 3:
            
            try:
                dish_id = int(input("Enter Dish ID You want to Remove From Menu: "))
                
                remove_dish(str(dish_id))
                print()
            
            except:
                 print("Invalid input, please enter a number")
                 continue
            

        elif choice == 4:
            take_order()
            print()

        elif choice == 5:
            try:
                
                # Implement the function to update order status
                order_id = int(input("Enter Order ID: "))
                valid_statuses = ['received', 'preparing', 'ready for pickup', 'delivered']
                
                for i, order_status in enumerate(valid_statuses):
                    print(f"{i+1}. {order_status}")
                    
                selected_order_status = int(input("Update Order Status: (To be implemented): "))
                
                if selected_order_status in range(0, len(valid_statuses)+1):
                    update_order_status(str(order_id), valid_statuses[selected_order_status-1])
                    print()
                else:
                    print("Invalid input, please select from give data above...")
                    continue
                
            except:
                print("Invalid input, please enter a number")
                continue

        elif choice == 6:
            # Implement the function to review orders
            review_orders()
            print()

        elif choice == 7:
            display_menu()
            print()

        elif choice == 8:
            print("\nThank You!! Keep using our services....")
            print("Exiting.......")
            break

        else:
            print("Invalid input, please try again")
            continue

        # Incrementing the round value to ensure that the welcome message will not be printed again
        round = 0

    except ValueError:
        print("Invalid input, please enter a number")
        continue
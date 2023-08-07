import json
import datetime


# ---------------------------------------------------------------

# data = {
#  "ids": {"snack": 1, "bill": 1},
#  "snacks": {
#             name: {
#                 "id": 1,
#                 "stock": 2,
#                 "price": 30
#                 }
#             },
#  "sales": {},
#  "bills": {}}
round = 1

# name will be unique along with id
# snack = {
#     "id": 1,
#     "stock": 2,
#     "price": 30
# }




# ---------------------------------------------------------------


# Add snack by providing snack name price and stock available
def addSnackToInventory() -> bool:
    try:
        name = str(input("Enter Snack Name: ").strip()).lower()
        stock = int(input("Enter Number of stock available: "))
        price = int(input("Enter Price: "))
        
        try:
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
                
                if data:
                    # When data is present in .json file program will try to execute this 
                    # if statement but it will do nothing as it will get passed by the executer
                    pass
                
                else:
                    # When .json file is completely empty this statement will get executed
                    print("JSON file is empty or contains no data.")
                
                # Getting the snacks data
                snacks = data["snacks"]
                
                # If a snack with the same name is already available provide a Error message to user and return False
                for e in snacks:
                    if name in snacks[e]["name"]:
                        print(f"XXXXXXXXXXXXXXXX   Error:: {name} is already in Inventory!!   XXXXXXXXXXXXXXXX")
                        return False
                
                # else Go forward and add the snack to database
                else:
                    
                    # Persisting the data into the database
                    try:
                        # Attempt to write data to a JSON file
                        # While opening the file to write on it, if not found, file will be automatically created
                        with open('data.json', 'w') as json_file:
                            
                            # Getting the next Id for snack
                            id = data["ids"]["snack"]
                            
                            # Printing the data for user to review
                            print("======== This is the data you provided to add =========")
                            print(f"\n~ Id:- {id}\n~ Name:- {name}\n~ Stock:- {stock}\n~ Price:- ₹{price}")
                            
                            while True:
                                wantToPersist = str(input("Want to Add (YES: 'y' OR NO: 'n'): "))
                                
                                if wantToPersist == 'y':
                                    
                                    # Incrementing the next id for snack
                                    data["ids"]["snack"] = id + 1
                                    
                                    # Creating snack dictionary to add in the database
                                    snack = {
                                        "name": name,
                                        "stock": stock,
                                        "price": price
                                    }
                                    
                                    snacks[id] = snack
                                    data["snacks"] = snacks
                                    
                                    # indent is added to make the file format more readable
                                    json.dump(data, json_file, indent=4)
                                    
                                    return True
                                
                                elif wantToPersist == 'n':
                                    
                                    # User choose not to add the snack then we need to write the data 
                                    # which were present in the database initially else the all the data 
                                    # from data.json file will get erased
                                    json.dump(data, json_file, indent=4)
                                    
                                    return False
                                
                                else:
                                    print("Invalid input, please try again")
                                    continue
                            
                            
                    
                    except PermissionError:
                        print("Error: Permission denied. Unable to write to JSON file.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                    

        except FileNotFoundError:
            print("JSON file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON data in the file.")
        
    except:
        print("Invalid input, please try again later")
        
    
    
    
def showAllSnacksAvailable():
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            
            if data:
                # When data is present in .json file program will try to execute this 
                # if statement but it will do nothing as it will get passed by the executer
                pass
            
            else:
                # When .json file is completely empty this statement will get executed
                print("JSON file is empty or contains no data.")
                
            snacks = data["snacks"]

            # Cheking if the empty
            if not snacks:
                print("\nXXXXXXXXXXXXXXXX   No Snack Available to display   XXXXXXXXXXXXXXXX")
            
            else:
                for id in snacks:
                    snack = snacks[id]
                    name = snack["name"]
                    stock = snack["stock"]
                    price = snack["price"]
                    
                    # Display only those items which are available means have stock more 1 or more
                    if stock > 0:
                        print(f"\n~ Id:- {id}\n~ Name:- {name}\n~ Stock:- {stock}\n~ Price:- ₹{price}")
    
    except FileNotFoundError:
        print("JSON file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data in the file.")
    
    
    
    
def saleSnack():
    try:
        
        id = int(input("Enter Snack ID: "))
        
        try:
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)

                if data:
                # When data is present in .json file program will try to execute this 
                # if statement but it will do nothing as it will get passed by the executer
                    pass
            
                else:
                    # When .json file is completely empty this statement will get executed
                    print("JSON file is empty or contains no data.")
                
                # Extracting Snacks from data
                snacks = data["snacks"]
                # Getting Snack by Id if not present get(id) method will return None
                snack = snacks.get(id)
                
                # If snack is not found with id print error
                if snack is None:
                    print(f"\nXXXXXXXXXXXXXXXX    Snack with ID: {id} Not Found    XXXXXXXXXXXXXXXX")
                    
                # Else provide snack information and ask for quantity required
                else:
                    name = snack["name"]
                    stock = snack["stock"]
                    price = snack["price"]
                    
                    # Displaying the product information to the user
                    print("\n#####################   Yippee!! Found Your Snack   #####################")
                    print("----- Please Confirm that it is the Product you where searching for -----")
                    print(f"\n~ Id:- {id}\n~ Name:- {name}\n~ Stock:- {stock}\n~ Price:- ₹{price}")
                    
                    # Getting confirmation from user
                    confirmation = int(input("Please Confirm (YES: 1, NO: 0): "))
                    
                    if confirmation == 1:
                        # Getting quantity from user
                        quantity = int(print("Enter quantity: "))
                        
                        # Check if user provided valid input or not
                        if quantity <= 0:
                            print("Invalid input, please try again later")
                            
                        # Check if these much quantity available or not
                        elif quantity > stock:
                            print("\nSorry! We don't have enough of this item to fulfill your order.\n")
                        
                        # Calculate the bill Create The bill Persist into the database at "bills" section and
                        # Update sales information at "sales" section
                        # Update product stock at "snacks" section 
                        else:
                            # Preparing to update all the necessary resources
                            # After preparation will take a final confirmation before start writing to the database
                            
                            # Creating Bill
                            billPrice = quantity * price
                            billId = data["ids"]["bill"]
                            
                            current_date = datetime.datetime.today().date()
                            current_date_time = datetime.datetime.now()
                            
                            date = current_date.strftime('%d-%m-%Y')
                            date_time = current_date_time.strftime('%d-%m-%Y %H:%M:%S')
                            
                            # Bill Format
                            # Bill = {
                            #     'id': 1,
                            #     'snackId': 1, 
                            #     'quantity': quantity,
                            #     'pricePerItem': price,
                            #     'billAmount': billPrice,
                            #     'datetime': time
                            # }
                            bill = {
                                "id": billId,
                                "snackId": id,
                                "quantity": quantity,
                                "pricePerItem": price,
                                "billAmount": billPrice,
                                "datetime": date_time
                            }
                            
                            # Last confirmation from user
                            confirm = int(input("Want to buy the Item (YES: 1, NO: 0): "))
                            
                            # Final Confirmation Done
                            # Let's start write operation
                            if confirm == 1:
                                
                                try:
                                    # Attempt to write data to a JSON file
                                    # While opening the file to write on it, if not found, file will be automatically created
                                    with open('output.json', 'w') as json_file:
                                        # indent is added to make the file format more readable
                                        
                                        # Sales
                                        sales = data['sales']
                                        daySales = sales.get(date, {})
                                        item = daySales.get(name, {})
                                        item['quantity_sold'] = item.get('quantity_sold', 0) + quantity
                                        item['revenue_generated'] = item.get('revenue_generated', 0) + billPrice

                                        daySales[name] = item
                                        sales[date] = daySales
                                        
                                        # Bills
                                        bills = data["bills"]
                                        dayBills = bills.get(date, [])

                                        dayBills.append(bill)
                                        bills[date] = dayBills
                                        
                                        # Update Stock of the snacks
                                        stock = stock - quantity
                                        snack['stock'] = stock
                                        snacks[id] = snack
                                        
                                        # Update next billId
                                        data["ids"]["bill"] = billId + 1
                                        
                                        # Finally writing the updated data to database
                                        json.dump(data, json_file, indent=4)
                                        

                                    print("\n###############  Order Placed successfully.  ##############\n")
                                    print("\n---------------  Here is Your Bill Generated  ---------------")
                                    print(f"\n~ Bill ID:- {billId}\n~ Snack:- {name}\n~ Quantity:- {quantity}\n~ Price Per Item:- ₹{price}\n~ Bill Amount:- ₹{billPrice}\n~ Order Time:- {date_time}")
                                    
                                except PermissionError:
                                    print("Error: Permission denied. Unable to write to JSON file.")
                                except Exception as e:
                                    print(f"An error occurred: {e}")
                            
                            elif confirmation == 0:
                                print("\n===========   System abort, Happy Shopping...   ============")
                                
                            else:
                                print("Invalid input, please try again later")
                                return
                            
                        
                    elif confirmation == 0:
                        print("\n===========   System abort, Happy Shopping...   ============")
                        
                    else:
                        print("Invalid input, please try again later")
                        return
            
        
        except FileNotFoundError:
            print("JSON file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON data in the file.")
        
    except:
        print("Invalid input, please try again later")






def removeSnackFromInventory() -> bool:
    return

# Can update stock available and price 
def updateSnackDetails() -> dict:
    return


def showSalesHistory():
    return






# d = {}
# # KeyError
# print(d["name"])

while True:
    if round == 1:
        print("------------------------------------------------------------------")
        print("================== Welcome To Mumbai Munchies  ===================")
        print("------------------------------------------------------------------")
        
    print("*******")
    print("1. Add Snack to inventory")
    print("2. Update Existing Snack details")
    print("3. Sale Snack and Generate Bill")
    print("4. Delete Snack from inventory")
    print("5. Show Sales History")
    print("6. Show All Snacks Available")
    print("7. Exit")
    print("*******")
    
    try: 
        choice = int(input("Enter your choice: "))

        if choice == 1:
            if addSnackToInventory():
                print("################   Item added successfully!!   ################")
            else:
                print("XXXXXXXXXXXXXXXX   Not able to add Item..   XXXXXXXXXXXXXXXX")
            print()
            
        # elif choice == 2:
            
        # elif choice == 3:
            
        # elif choice == 4:
            
        # elif choice == 5:
        
        elif choice == 6:
            showAllSnacksAvailable()
            print()
            
        elif choice == 7:
            print("\nThank You!! Keep using our services....")
            print("Exiting.......")
            break
        
        else:
            print("Invalid input, please try again")
            continue
        
        # Incrementing the round value to ensure that the welcome message will not be printed again
        round = 0
    
    except:
        print("Invalid input, please try again")
        continue
    
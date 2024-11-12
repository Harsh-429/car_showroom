# import json

# # Car information dictionary with images (simulated as URLs)
# car_details = {
#         'family cars': {
#         'Ertiga': {'Price': '₹8.64 lakh', 'Model': 'ZXI', 'Engine': '1.5L Petrol', 'Mileage': '19.01 kmpl', 'Seating': '7-seater'},
#         'Kia Carens': {'Price': '₹9.60 lakh', 'Model': 'Prestige', 'Engine': '1.5L Petrol', 'Mileage': '16.5 kmpl', 'Seating': '7-seater'},
#         'Tata Nexon': {'Price': '₹7.99 lakh', 'Model': 'XZ+', 'Engine': '1.2L Petrol', 'Mileage': '17.57 kmpl', 'Seating': '5-seater'}
#     },
#     'off roading cars': {
#         'Mahindra Thar': {'Price': '₹13.49 lakh', 'Model': 'LX', 'Engine': '2.0L Petrol', 'Mileage': '15.2 kmpl', 'Seating': '4-seater'},
#         'Jimny': {'Price': '₹12.74 lakh', 'Model': 'Zeta', 'Engine': '1.5L Petrol', 'Mileage': '16.94 kmpl', 'Seating': '4-seater'},
#         'Urban Cruiser': {'Price': '₹9.02 lakh', 'Model': 'Premium', 'Engine': '1.5L Petrol', 'Mileage': '17.03 kmpl', 'Seating': '5-seater'}
#     },
#     'suv': {
#         'Mahindra Scorpio': {'Price': '₹13.54 lakh', 'Model': 'S11', 'Engine': '2.2L Diesel', 'Mileage': '15 kmpl', 'Seating': '7-seater'},
#         'Fortuner': {'Price': '₹32.59 lakh', 'Model': 'Legender', 'Engine': '2.8L Diesel', 'Mileage': '10.4 kmpl', 'Seating': '7-seater'},
#         'Tata Harrier': {'Price': '₹14.49 lakh', 'Model': 'XZ+', 'Engine': '2.0L Diesel', 'Mileage': '16.35 kmpl', 'Seating': '5-seater'}
#     },
#     'sports cars': {
#         'BMW M2': {'Price': '₹85.00 lakh', 'Model': 'Competition', 'Engine': '3.0L Petrol', 'Mileage': '10 kmpl', 'Seating': '2-seater'},
#         'Porsche 911': {'Price': '₹1.20 crore', 'Model': '911', 'Engine': '3.0L Petrol', 'Mileage': '12.8 kmpl', 'Seating': '2-seater'},
#         'Ford Mustang GT': {'Price': '₹74.61 lakh', 'Model': 'GT', 'Engine': '5.0L V8', 'Mileage': '7.9 kmpl', 'Seating': '4-seater'}
#     },
#     'electric cars': {
#         'Tesla Model S': {'Price': '₹1.50 crore', 'Model': 'Long Range', 'Engine': 'Electric', 'Mileage': '652 km/charge', 'Seating': '5-seater'},
#         'Nexon EV': {'Price': '₹14.74 lakh', 'Model': 'XZ+', 'Engine': 'Electric', 'Mileage': '312 km/charge', 'Seating': '5-seater'},
#         'MG ZS EV': {'Price': '₹23.38 lakh', 'Model': 'Exclusive', 'Engine': 'Electric', 'Mileage': '419 km/charge', 'Seating': '5-seater'}
#     }
# }
   

# # Database for buyer details
# buyer_database = []

# # Greeting message
# def greeting():
#     print("Hello! 👋 Welcome to our car showroom.")
#     print("I'm your assistant here to help you find the perfect car. 🚗")
#     print("Feel free to explore various categories and ask questions about your favorite cars.")

# # Polite response
# def polite_response(message):
#     print(f"\n{message}")
#     print("If you need more assistance, feel free to ask! 😊")

# # EMI calculation
# def calculate_emi(principal, rate, time):
#     monthly_rate = rate / (12 * 100)
#     emi = principal * monthly_rate * (1 + monthly_rate) ** (time * 12) / ((1 + monthly_rate) ** (time * 12) - 1)
#     return emi

# # Adding buyer details
# def add_buyer_details(name, car_choice, category):
#     buyer_info = {
#         'name': name,
#         'car': car_choice,
#         'details': car_details[category][car_choice]
#     }
#     buyer_database.append(buyer_info)
#     with open('buyer_database.json', 'w') as db_file:
#         json.dump(buyer_database, db_file)
#     print(f"Your details have been saved, {name}. Thank you for your interest in {car_choice}!")

# # Main program starts here
# greeting()

# while True:
#     # Asking the user for car type
#     n = input('\nWhich type of car do you wish to explore (family cars, off roading cars, suv, sports cars, electric cars)? ').lower()
    
#     if n in car_details:
#         polite_response(f"Here are the available options for {n}:")
#         for car in car_details[n]:
#             print(f"- {car} (Image: {car_details[n][car]})")
        
#         # Asking the user for a specific car
#         car_choice = input("\nWhich car would you like more details about? ").lower()
        
#         # Checking if the car exists in the selected category
#         for car_name in car_details[n]:
#             if car_choice == car_name.lower():
#                 polite_response(f"Details for {car_name}:")
#                 for detail, value in car_details[n][car_name].items():
#                     print(f"{detail}: {value}")
                
#                 # Insurance and EMI inquiry
#                 insurance = input("\nWould you like to know about insurance and EMI facilities? (yes/no): ").lower()
#                 if insurance == 'yes':
#                     # Converting price to actual numerical value
#                     principal = float(car_details[n][car_name]['Price'].replace('₹', '').replace(' lakh', '').replace(',', '')) * 100000  # Convert to actual price
#                     rate = float(input("Enter the interest rate (annual %): "))
#                     time = int(input("For how many years would you like to take the EMI? "))
#                     emi = calculate_emi(principal, rate, time)
#                     polite_response(f"The EMI for {car_name} will be approximately: ₹{emi:.2f} per month.")
                
#                 # Asking for buyer details
#                 buyer_name = input("Please enter your name to save your details: ")
#                 add_buyer_details(buyer_name, car_name, n)
                
#                 break
#         else:
#             polite_response(f"Sorry, we don't have details for {car_choice}.")
    
#     else:
#         polite_response("For now, your choice is not available. Please try another category or visit us again later.")
    
#     # Option to continue or exit
#     exit_choice = input("\nWould you like to check more cars? (yes/no): ").lower()
#     if exit_choice != 'yes':
#         polite_response("Thank you for visiting our showroom! Have a great day! 👋")
#         break
# import json

# # Car information dictionary with stock (simulated as inventory)
# car_details = {      
#                'family cars': {
#         'Ertiga': {'Price': '₹8.64 lakh', 'Model': 'ZXI', 'Engine': '1.5L Petrol', 'Mileage': '19.01 kmpl', 'Seating': '7-seater','stock':5},
#         'Kia Carens': {'Price': '₹9.60 lakh', 'Model': 'Prestige', 'Engine': '1.5L Petrol', 'Mileage': '16.5 kmpl', 'Seating': '7-seater','stock':4},
#         'Tata Nexon': {'Price': '₹7.99 lakh', 'Model': 'XZ+', 'Engine': '1.2L Petrol', 'Mileage': '17.57 kmpl', 'Seating': '5-seater','stock':9}
#     },
#     'off roading cars': {
#         'Mahindra Thar': {'Price': '₹13.49 lakh', 'Model': 'LX', 'Engine': '2.0L Petrol', 'Mileage': '15.2 kmpl', 'Seating': '4-seater','stock':8},
#         'Jimny': {'Price': '₹12.74 lakh', 'Model': 'Zeta', 'Engine': '1.5L Petrol', 'Mileage': '16.94 kmpl', 'Seating': '4-seater','stock':2},
#         'Urban Cruiser': {'Price': '₹9.02 lakh', 'Model': 'Premium', 'Engine': '1.5L Petrol', 'Mileage': '17.03 kmpl', 'Seating': '5-seater','stock':7}
#     },
#     'suv': {
#         'Mahindra Scorpio': {'Price': '₹13.54 lakh', 'Model': 'S11', 'Engine': '2.2L Diesel', 'Mileage': '15 kmpl', 'Seating': '7-seater','stock':5},
#         'Fortuner': {'Price': '₹32.59 lakh', 'Model': 'Legender', 'Engine': '2.8L Diesel', 'Mileage': '10.4 kmpl', 'Seating': '7-seater','stock':6},
#         'Tata Harrier': {'Price': '₹14.49 lakh', 'Model': 'XZ+', 'Engine': '2.0L Diesel', 'Mileage': '16.35 kmpl', 'Seating': '5-seater','stock':5}
#     },
#     'sports cars': {
#         'BMW M2': {'Price': '₹85.00 lakh', 'Model': 'Competition', 'Engine': '3.0L Petrol', 'Mileage': '10 kmpl', 'Seating': '2-seater','stock':8},
#         'Porsche 911': {'Price': '₹1.20 crore', 'Model': '911', 'Engine': '3.0L Petrol', 'Mileage': '12.8 kmpl', 'Seating': '2-seater','stock':5},
#         'Ford Mustang GT': {'Price': '₹74.61 lakh', 'Model': 'GT', 'Engine': '5.0L V8', 'Mileage': '7.9 kmpl', 'Seating': '4-seater','stock':2}
#     },
#     'electric cars': {
#         'Tesla Model S': {'Price': '₹1.50 crore', 'Model': 'Long Range', 'Engine': 'Electric', 'Mileage': '652 km/charge', 'Seating': '5-seater','stock':5},
#         'Nexon EV': {'Price': '₹14.74 lakh', 'Model': 'XZ+', 'Engine': 'Electric', 'Mileage': '312 km/charge', 'Seating': '5-seater','stock':3},
#         'MG ZS EV': {'Price': '₹23.38 lakh', 'Model': 'Exclusive', 'Engine': 'Electric', 'Mileage': '419 km/charge', 'Seating': '5-seater','stock':2}
#     }
#     ,
#     # other categories...
# }

# # Database for buyer details and inquiries (for CRM and sales analytics)
# buyer_database = []
# inquiry_count = {}

# # Greeting message
# def greeting():
#     print("Hello! 👋 Welcome to our car showroom.")
#     print("I'm your assistant here to help you find the perfect car. 🚗")
#     print("Feel free to explore various categories and ask questions about your favorite cars.")

# # Polite response
# def polite_response(message):
#     print(f"\n{message}")
#     print("If you need more assistance, feel free to ask! 😊")

# # EMI calculation
# def calculate_emi(principal, rate, time):
#     monthly_rate = rate / (12 * 100)
#     emi = principal * monthly_rate * (1 + monthly_rate) ** (time * 12) / ((1 + monthly_rate) ** (time * 12) - 1)
#     return emi

# # Adding buyer details and updating stock
# def add_buyer_details(name, car_choice, category):
#     car = car_details[category][car_choice]
#     if car['Stock'] > 0:
#         car['Stock'] -= 1
#         buyer_info = {
#             'name': name,
#             'car': car_choice,
#             'details': car
#         }
#         buyer_database.append(buyer_info)
#         # Saving to a file (could be used for CRM purposes)
#         with open('buyer_database.json', 'w') as db_file:
#             json.dump(buyer_database, db_file)
        
#         # Track the number of inquiries (sales analytics)
#         inquiry_count[car_choice] = inquiry_count.get(car_choice, 0) + 1

#         print(f"Your details have been saved, {name}. Thank you for your interest in {car_choice}!")
#         print(f"Remaining stock for {car_choice}: {car['Stock']}")
#     else:
#         polite_response(f"Sorry, {car_choice} is currently out of stock.")

# # Sales analytics report
# def show_sales_analytics():
#     print("\n--- Sales Analytics Report ---")
#     print("Car inquiries so far:")
#     for car, count in inquiry_count.items():
#         print(f"{car}: {count} inquiries")
#     print("-----------------------------")

# # Main program starts here
# greeting()

# while True:
#     # Asking the user for car type
#     n = input('\nWhich type of car do you wish to explore (family cars, off roading cars, suv, sports cars, electric cars)? ').lower()
    
#     if n in car_details:
#         polite_response(f"Here are the available options for {n}:")
#         for car in car_details[n]:
#             stock = car_details[n][car]['Stock']
#             print(f"- {car} (Stock: {stock})")

#         # Asking the user for a specific car
#         car_choice = input("\nWhich car would you like more details about? ").lower()
        
#         # Checking if the car exists in the selected category
#         for car_name in car_details[n]:
#             if car_choice == car_name.lower():
#                 polite_response(f"Details for {car_name}:")
#                 for detail, value in car_details[n][car_name].items():
#                     if detail != 'Stock':  # Exclude stock from user details
#                         print(f"{detail}: {value}")
                
#                 # Insurance and EMI inquiry
#                 insurance = input("\nWould you like to know about insurance and EMI facilities? (yes/no): ").lower()
#                 if insurance == 'yes':
#                     principal = float(car_details[n][car_name]['Price'].replace('₹', '').replace(' lakh', '').replace(',', '')) * 100000
#                     rate = float(input("Enter the interest rate (annual %): "))
#                     time = int(input("For how many years would you like to take the EMI? "))
#                     emi = calculate_emi(principal, rate, time)
#                     polite_response(f"The EMI for {car_name} will be approximately: ₹{emi:.2f} per month.")
                
#                 # Asking for buyer details
#                 buyer_name = input("Please enter your name to save your details: ")
#                 add_buyer_details(buyer_name, car_name, n)

#                 break
#         else:
#             polite_response(f"Sorry, we don't have details for {car_choice}.")
    
#     else:
#         polite_response("For now, your choice is not available. Please try another category or visit us again later.")
    
#     # Option to continue or exit
#     exit_choice = input("\nWould you like to check more cars? (yes/no): ").lower()
#     if exit_choice != 'yes':
#         show_sales_analytics()  # Show sales analytics report before exiting
#         polite_response("Thank you for visiting our showroom! Have a great day! 👋")
#         break
# import json

# # Car information dictionary with stock (simulated as inventory)
# car_details = {      
#     'family cars': {
#         'Ertiga': {'Price': '₹8.64 lakh', 'Model': 'ZXI', 'Engine': '1.5L Petrol', 'Mileage': '19.01 kmpl', 'Seating': '7-seater', 'stock': 5},
#         'Kia Carens': {'Price': '₹9.60 lakh', 'Model': 'Prestige', 'Engine': '1.5L Petrol', 'Mileage': '16.5 kmpl', 'Seating': '7-seater', 'stock': 4},
#         'Tata Nexon': {'Price': '₹7.99 lakh', 'Model': 'XZ+', 'Engine': '1.2L Petrol', 'Mileage': '17.57 kmpl', 'Seating': '5-seater', 'stock': 9}
#     },
#     'off roading cars': {
#         'Mahindra Thar': {'Price': '₹13.49 lakh', 'Model': 'LX', 'Engine': '2.0L Petrol', 'Mileage': '15.2 kmpl', 'Seating': '4-seater', 'stock': 8},
#         'Jimny': {'Price': '₹12.74 lakh', 'Model': 'Zeta', 'Engine': '1.5L Petrol', 'Mileage': '16.94 kmpl', 'Seating': '4-seater', 'stock': 2},
#         'Urban Cruiser': {'Price': '₹9.02 lakh', 'Model': 'Premium', 'Engine': '1.5L Petrol', 'Mileage': '17.03 kmpl', 'Seating': '5-seater', 'stock': 7}
#     },
#     'suv': {
#         'Mahindra Scorpio': {'Price': '₹13.54 lakh', 'Model': 'S11', 'Engine': '2.2L Diesel', 'Mileage': '15 kmpl', 'Seating': '7-seater', 'stock': 5},
#         'Fortuner': {'Price': '₹32.59 lakh', 'Model': 'Legender', 'Engine': '2.8L Diesel', 'Mileage': '10.4 kmpl', 'Seating': '7-seater', 'stock': 6},
#         'Tata Harrier': {'Price': '₹14.49 lakh', 'Model': 'XZ+', 'Engine': '2.0L Diesel', 'Mileage': '16.35 kmpl', 'Seating': '5-seater', 'stock': 5}
#     },
#     'sports cars': {
#         'BMW M2': {'Price': '₹85.00 lakh', 'Model': 'Competition', 'Engine': '3.0L Petrol', 'Mileage': '10 kmpl', 'Seating': '2-seater', 'stock': 8},
#         'Porsche 911': {'Price': '₹1.20 crore', 'Model': '911', 'Engine': '3.0L Petrol', 'Mileage': '12.8 kmpl', 'Seating': '2-seater', 'stock': 5},
#         'Ford Mustang GT': {'Price': '₹74.61 lakh', 'Model': 'GT', 'Engine': '5.0L V8', 'Mileage': '7.9 kmpl', 'Seating': '4-seater', 'stock': 2}
#     },
#     'electric cars': {
#         'Tesla Model S': {'Price': '₹1.50 crore', 'Model': 'Long Range', 'Engine': 'Electric', 'Mileage': '652 km/charge', 'Seating': '5-seater', 'stock': 5},
#         'Nexon EV': {'Price': '₹14.74 lakh', 'Model': 'XZ+', 'Engine': 'Electric', 'Mileage': '312 km/charge', 'Seating': '5-seater', 'stock': 3},
#         'MG ZS EV': {'Price': '₹23.38 lakh', 'Model': 'Exclusive', 'Engine': 'Electric', 'Mileage': '419 km/charge', 'Seating': '5-seater', 'stock': 2}
#     }
# }

# # Database for buyer details and inquiries (for CRM and sales analytics)
# buyer_database = []
# inquiry_count = {}

# # Greeting message
# def greeting():
#     print("Hello! 👋 Welcome to our car showroom.")
#     print("I'm your assistant here to help you find the perfect car. 🚗")
#     print("Feel free to explore various categories and ask questions about your favorite cars.")

# # Polite response
# def polite_response(message):
#     print(f"\n{message}")
#     print("If you need more assistance, feel free to ask! 😊")

# # EMI calculation
# def calculate_emi(principal, rate, time):
#     monthly_rate = rate / (12 * 100)
#     emi = principal * monthly_rate * (1 + monthly_rate) ** (time * 12) / ((1 + monthly_rate) ** (time * 12) - 1)
#     return emi

# # Adding buyer details and updating stock
# def add_buyer_details(name, car_choice, category):
#     try:
#         car = car_details[category][car_choice]
#         if car['stock'] > 0:
#             car['stock'] -= 1
#             buyer_info = {
#                 'name': name,
#                 'car': car_choice,
#                 'details': car
#             }
#             buyer_database.append(buyer_info)
#             # Save to file
#             with open('buyer_database.json', 'w') as db_file:
#                 json.dump(buyer_database, db_file)
            
#             # Track the number of inquiries (sales analytics)
#             inquiry_count[car_choice] = inquiry_count.get(car_choice, 0) + 1

#             print(f"Your details have been saved, {name}. Thank you for your interest in {car_choice}!")
#             print(f"Remaining stock for {car_choice}: {car['stock']}")
#         else:
#             polite_response(f"Sorry, {car_choice} is currently out of stock.")
#     except KeyError:
#         polite_response("Sorry, an error occurred with the car selection. Please try again.")

# # Sales analytics report
# def show_sales_analytics():
#     print("\n--- Sales Analytics Report ---")
#     print("Car inquiries so far:")
#     for car, count in inquiry_count.items():
#         print(f"{car}: {count} inquiries")
#     print("-----------------------------")

# # Main program starts here
# greeting()

# while True:
#     # Asking the user for car type
#     n = input('\nWhich type of car do you wish to explore (family cars, off roading cars, suv, sports cars, electric cars)? ').lower()
    
#     if n in car_details:
#         polite_response(f"Here are the available options for {n}:")
#         for car in car_details[n]:
#             stock = car_details[n][car]['stock']
#             print(f"- {car} (Stock: {stock})")

#         # Asking the user for a specific car
#         car_choice = input("\nWhich car would you like more details about? ").lower()
        
#         # Checking if the car exists in the selected category
#         car_found = False
#         for car_name in car_details[n]:
#             if car_choice == car_name.lower():
#                 car_found = True
#                 polite_response(f"Details for {car_name}:")
#                 for detail, value in car_details[n][car_name].items():
#                     if detail != 'stock':  # Exclude stock from user details
#                         print(f"{detail}: {value}")
                
#                 # Insurance and EMI inquiry
#                 insurance = input("\nWould you like to know about insurance and EMI facilities? (yes/no): ").lower()
#                 if insurance == 'yes':
#                     try:
#                         principal = float(car_details[n][car_name]['Price'].replace('₹', '').replace(' lakh', '').replace(',', '')) * 100000
#                         rate = float(input("Enter the interest rate (annual %): "))
#                         time = int(input("For how many years would you like to take the EMI? "))
#                         emi = calculate_emi(principal, rate, time)
#                         polite_response(f"The EMI for {car_name} will be approximately: ₹{emi:.2f} per month.")
#                     except ValueError:
#                         polite_response("Invalid input for EMI calculation. Please try again.")
                
#                 # Asking for buyer details
#                 buyer_name = input("Please enter your name to save your details: ")
#                 add_buyer_details(buyer_name, car_name, n)

#                 break
        
#         if not car_found:
#             polite_response(f"Sorry, we don't have details for {car_choice}.")
    
#     else:
#         polite_response("For now, your choice is not available. Please try another category or visit us again later.")
    
#     # Option to continue or exit
#     exit_choice = input("\nWould you like to check more cars? (yes/no): ").lower()
#     if exit_choice != 'yes':
#         show_sales_analytics()  # Show sales analytics report before exiting
#         polite_response("Thank you for visiting our showroom! Have a great day! 👋")
#         break
import json

# Car information dictionary with stock (simulated as inventory)
car_details = {      
    'family cars': {
        'Ertiga': {'Price': '₹8.64 lakh', 'Model': 'ZXI', 'Engine': '1.5L Petrol', 'Mileage': '19.01 kmpl', 'Seating': '7-seater', 'stock': 5},
        'Kia Carens': {'Price': '₹9.60 lakh', 'Model': 'Prestige', 'Engine': '1.5L Petrol', 'Mileage': '16.5 kmpl', 'Seating': '7-seater', 'stock': 4},
        'Tata Nexon': {'Price': '₹7.99 lakh', 'Model': 'XZ+', 'Engine': '1.2L Petrol', 'Mileage': '17.57 kmpl', 'Seating': '5-seater', 'stock': 9}
    },
    'off roading cars': {
        'Mahindra Thar': {'Price': '₹13.49 lakh', 'Model': 'LX', 'Engine': '2.0L Petrol', 'Mileage': '15.2 kmpl', 'Seating': '4-seater', 'stock': 8},
        'Jimny': {'Price': '₹12.74 lakh', 'Model': 'Zeta', 'Engine': '1.5L Petrol', 'Mileage': '16.94 kmpl', 'Seating': '4-seater', 'stock': 2},
        'Urban Cruiser': {'Price': '₹9.02 lakh', 'Model': 'Premium', 'Engine': '1.5L Petrol', 'Mileage': '17.03 kmpl', 'Seating': '5-seater', 'stock': 7}
    },
    'suv': {
        'Mahindra Scorpio': {'Price': '₹13.54 lakh', 'Model': 'S11', 'Engine': '2.2L Diesel', 'Mileage': '15 kmpl', 'Seating': '7-seater', 'stock': 5},
        'Fortuner': {'Price': '₹32.59 lakh', 'Model': 'Legender', 'Engine': '2.8L Diesel', 'Mileage': '10.4 kmpl', 'Seating': '7-seater', 'stock': 6},
        'Tata Harrier': {'Price': '₹14.49 lakh', 'Model': 'XZ+', 'Engine': '2.0L Diesel', 'Mileage': '16.35 kmpl', 'Seating': '5-seater', 'stock': 5}
    },
    'sports cars': {
        'BMW M2': {'Price': '₹85.00 lakh', 'Model': 'Competition', 'Engine': '3.0L Petrol', 'Mileage': '10 kmpl', 'Seating': '2-seater', 'stock': 8},
        'Porsche 911': {'Price': '₹1.20 crore', 'Model': '911', 'Engine': '3.0L Petrol', 'Mileage': '12.8 kmpl', 'Seating': '2-seater', 'stock': 5},
        'Ford Mustang GT': {'Price': '₹74.61 lakh', 'Model': 'GT', 'Engine': '5.0L V8', 'Mileage': '7.9 kmpl', 'Seating': '4-seater', 'stock': 2}
    },
    'electric cars': {
        'Tesla Model S': {'Price': '₹1.50 crore', 'Model': 'Long Range', 'Engine': 'Electric', 'Mileage': '652 km/charge', 'Seating': '5-seater', 'stock': 5},
        'Nexon EV': {'Price': '₹14.74 lakh', 'Model': 'XZ+', 'Engine': 'Electric', 'Mileage': '312 km/charge', 'Seating': '5-seater', 'stock': 3},
        'MG ZS EV': {'Price': '₹23.38 lakh', 'Model': 'Exclusive', 'Engine': 'Electric', 'Mileage': '419 km/charge', 'Seating': '5-seater', 'stock': 2}
    }
}

# Database for buyer details and inquiries (for CRM and sales analytics)
buyer_database = []
inquiry_count = {}

# Greeting message
def greeting():
    print("Hello! 👋 Welcome to our car showroom.")
    print("I'm your assistant here to help you find the perfect car. 🚗")
    print("Feel free to explore various categories and ask questions about your favorite cars.")

# Polite response
def polite_response(message):
    print(f"\n{message}")
    print("If you need more assistance, feel free to ask! 😊")

# EMI calculation with down payment
def calculate_emi(principal, rate, time, down_payment):
    # Reduce principal by down payment
    loan_amount = principal - down_payment
    monthly_rate = rate / (12 * 100)
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** (time * 12) / ((1 + monthly_rate) ** (time * 12) - 1)
    return emi

# Adding buyer details and updating stock
def add_buyer_details(name, car_choice, category):
    try:
        car = car_details[category][car_choice]
        if car['stock'] > 0:
            car['stock'] -= 1
            buyer_info = {
                'name': name,
                'car': car_choice,
                'details': car
            }
            buyer_database.append(buyer_info)
            # Save to file
            with open('buyer_database.json', 'w') as db_file:
                json.dump(buyer_database, db_file)
            
            # Track the number of inquiries (sales analytics)
            inquiry_count[car_choice] = inquiry_count.get(car_choice, 0) + 1

            print(f"Your details have been saved, {name}. Thank you for your interest in {car_choice}!")
            print(f"Remaining stock for {car_choice}: {car['stock']}")
        else:
            polite_response(f"Sorry, {car_choice} is currently out of stock.")
    except KeyError:
        polite_response("Sorry, an error occurred with the car selection. Please try again.")

# Sales analytics report
def show_sales_analytics():
    print("\n--- Sales Analytics Report ---")
    print("Car inquiries so far:")
    for car, count in inquiry_count.items():
        print(f"{car}: {count} inquiries")
    print("-----------------------------")

# Main program starts here
greeting()

while True:
    # Asking the user for car type
    n = input('\nWhich type of car do you wish to explore (family cars, off roading cars, suv, sports cars, electric cars)? ').lower()
    
    if n in car_details:
        polite_response(f"Here are the available options for {n}:")
        for car in car_details[n]:
            stock = car_details[n][car]['stock']
            print(f"- {car} (Stock: {stock})")

        # Asking the user for a specific car
        car_choice = input("\nWhich car would you like more details about? ").lower()
        
        # Checking if the car exists in the selected category
        car_found = False
        for car_name in car_details[n]:
            if car_choice == car_name.lower():
                car_found = True
                polite_response(f"Details for {car_name}:")
                for detail, value in car_details[n][car_name].items():
                    if detail != 'stock':  # Exclude stock from user details
                        print(f"{detail}: {value}")
                
                # Insurance and EMI inquiry
                insurance = input("\nWould you like to know about insurance and EMI facilities? (yes/no): ").lower()
                if insurance == 'yes':
                    try:
                        principal = float(car_details[n][car_name]['Price'].replace('₹', '').replace(' lakh', '').replace(',', '')) * 100000
                        rate = float(input("Enter the interest rate (annual %): "))
                        time = int(input("For how many years would you like to take the EMI? "))
                        down_payment = float(input("Enter the down payment amount (in ₹): "))
                        emi = calculate_emi(principal, rate, time, down_payment)
                        polite_response(f"The EMI for {car_name} will be approximately: ₹{emi:.2f} per month.")
                    except ValueError:
                        polite_response("Invalid input for EMI calculation. Please try again.")
                
                # Asking for buyer details
                buyer_name = input("Please enter your name to save your details: ")
                add_buyer_details(buyer_name, car_name, n)

                break
        
        if not car_found:
            polite_response(f"Sorry, we don't have details for {car_choice}.")
    
    else:
        polite_response("For now, your choice is not available. Please try another category or visit us again later.")
    
    # Option to continue or exit
    exit_choice = input("\nWould you like to check more cars? (yes/no): ").lower()
    if exit_choice != 'yes':
        show_sales_analytics()  # Show sales analytics report before exiting
        polite_response("Thank you for visiting our showroom! Have a great day! 👋")
        break
    
    



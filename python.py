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

# Customizations for some cars
customizations = {
    'Ertiga': {'Colors': ['Red', 'Blue', 'Black'], 'Wheels': ['Alloy', 'Standard']},
    'Kia Carens': {'Colors': ['White', 'Grey'], 'Wheels': ['Standard']}
}

# Insurance plans
insurance_plans = {
    'basic': {'premium': '₹15,000/year', 'coverage': 'Basic Coverage'},
    'premium': {'premium': '₹30,000/year', 'coverage': 'Full Coverage with Theft Protection'}
}

# Database for buyer details and inquiries (for CRM and sales analytics)
buyer_database = []
inquiry_count = {}

# User profiles to save preferences and wishlist
user_profiles = {}
test_drive_bookings = []

# Different tone functions
def greeting_tone():
    print("Hello! 👋 Welcome to our car showroom. I'm your assistant to help you find the perfect car. 😊")
    
def formal_response(message):
    print(f"\n{message}")
    print("Please let me know if you require further assistance. Thank you.")

def casual_response(message):
    print(f"\n{message}")
    print("Got any other questions? Feel free to ask! 😄")

def friendly_response(message):
    print(f"\n{message}")
    print("Don't hesitate to ask if you need any more info! 😊")

# EMI calculation with down payment
def calculate_emi(principal, rate, time, down_payment):
    loan_amount = principal - down_payment
    monthly_rate = rate / (12 * 100)
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** (time * 12) / ((1 + monthly_rate) ** (time * 12) - 1)
    return emi

# Apply discount
def apply_discount(car, category, discount_percent):
    price = float(car_details[category][car]['Price'].replace('₹', '').replace(' lakh', '').replace(',', '')) * 100000
    discounted_price = price - (price * discount_percent / 100)
    return discounted_price

# EMI calculation and down payment feature in action
def emi_and_down_payment(car, category, down_payment, interest_rate, tenure):
    price_in_lakhs = float(car_details[category][car]['Price'].replace('₹', '').replace(' lakh', '').replace(',', ''))
    price_in_rupees = price_in_lakhs * 100000
    discounted_price = apply_discount(car, category, 10)  # Example: 10% discount
    emi = calculate_emi(discounted_price, interest_rate, tenure, down_payment)
    formal_response(f"For the {car}:")
    print(f"Total Price: ₹{price_in_lakhs:.2f} lakh")
    print(f"Discounted Price (10% off): ₹{discounted_price / 100000:.2f} lakh")
    print(f"Down Payment: ₹{down_payment:.2f}")
    print(f"EMI (for {tenure} years at {interest_rate}% interest): ₹{emi:.2f} per month")

# Car comparison feature
def compare_cars(car1, car2, category):
    if car1 in car_details[category] and car2 in car_details[category]:
        formal_response(f"Comparing {car1} and {car2}:")
        print(f"\n{'Attribute':<15} | {'Car 1':<20} | {'Car 2'}")
        print("-" * 50)
        for key in car_details[category][car1]:
            if key != 'stock':
                value1 = car_details[category][car1][key]
                value2 = car_details[category][car2][key]
                print(f"{key:<15} | {value1:<20} | {value2}")
    else:
        formal_response("One or both of the selected cars are not available in this category.")

# Search by budget
def search_by_budget(min_budget, max_budget):
    friendly_response(f"Showing cars between ₹{min_budget} lakh and ₹{max_budget} lakh:")
    found = False
    for category, cars in car_details.items():
        for car, details in cars.items():
            price = float(details['Price'].replace('₹', '').replace(' lakh', '').replace(',', ''))
            if min_budget <= price <= max_budget:
                found = True
                print(f"{car} - {details['Price']} in {category}")
    if not found:
        formal_response("No cars found in the specified budget range.")

# Filter cars by attributes
def filter_cars(attribute, value):
    friendly_response(f"Cars with {attribute} matching {value}:")
    for category, cars in car_details.items():
        for car, details in cars.items():
            if details[attribute] == value:
                print(f"{car} - {details['Price']} ({category})")

# Saving to wishlist in user profile
def save_to_wishlist(user, car, category):
    if user not in user_profiles:
        user_profiles[user] = {'wishlist': []}
   

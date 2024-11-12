# import speech_recognition as sr
# import pyttsx3

# # Initialize the recognizer and TTS engine
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # Set properties for the TTS engine
# engine.setProperty('rate', 150)  # Speed of speech
# engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
# def listen():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
#         audio = recognizer.listen(source)

#         try:
#             print("Recognizing...")
#             query = recognizer.recognize_google(audio, language='en-in')
#             print(f"User said: {query}")
#             return query.lower()
#         except sr.UnknownValueError:
#             print("Sorry, I did not catch that.")
#             return None
#         except sr.RequestError:
#             print("Could not request results. Check your internet connection.")
#             return None
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
# import datetime
# import webbrowser

# def basic_commands(query):
#     if 'time' in query:
#         current_time = datetime.datetime.now().strftime('%I:%M %p')
#         speak(f"The current time is {current_time}")

#     elif 'open google' in query:
#         speak("Opening Google")
#         webbrowser.open("https://www.google.com")

#     elif 'how are you' in query:
#         speak("I am doing great, thanks for asking!")
# import openai

# openai.api_key = 'YOUR_API_KEY'

# def ask_openai(query):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=100
#     )
#     return response.choices[0].text.strip()
# def respond_to_query(query):
#     if 'open' in query or 'time' in query:
#         basic_commands(query)
#     else:
#         response = ask_openai(query)
#         print(f"AI: {response}")
#         speak(response)
# if __name__ == "__main__":
#     speak("Hello, I am your voice assistant. How can I help you today?")
    
#     while True:
#         query = listen()
        
#         if query:
#             if 'exit' in query or 'bye' in query:
#                 speak("Goodbye!")
#                 break
#             respond_to_query(query)

# while True:
#     n = input('greet:')
#     n=n.lower()
#     if n=='good morning' or n=='gm':
#         print('good morning friend!')
#     elif n=='after noon' or n=='an':
#         print('good after noon friend !')
#     elif n=='good night' or n=='gn':
#         print('good night friend!')
#     elif n=='end':
#         print('have a good day!')
#         break
#     else:
#         print('nothing')
# while True:
#     n=input('which type of car do u wish to buy:')
#     n=n.lower()
#     if n=='family cars':
#         print('available options are:/nErtiga /n Kia carena /n tata nexon /n skoda /ncreta /n ford')
#     elif n=='off roding car':
#         print('mahindra thar/n Jimny /n urban cruiser /n tata safari')
#     elif n=='suv':
#         print('mahindra scorpio/n fortuner/n tata harriar/n MG hector')
#     elif n=='sports car':
#         print('BMW m2/n porshe /n ford mustunge /n jaguar')
#     else:
#         print('for now your choice is not available: thank you to visit our showroom')
# Car information dictionary
# car_details = {
#     'family cars': {
#         'Ertiga': {'Price': '₹8.64 lakh', 'Model': 'ZXI', 'Engine': '1.5L Petrol', 'Mileage': '19.01 kmpl'},
#         'Kia Carens': {'Price': '₹9.60 lakh', 'Model': 'Prestige', 'Engine': '1.5L Petrol', 'Mileage': '16.5 kmpl'},
#         'Tata Nexon': {'Price': '₹7.99 lakh', 'Model': 'XZ+', 'Engine': '1.2L Petrol', 'Mileage': '17.57 kmpl'},
#         'Skoda': {'Price': '₹12.69 lakh', 'Model': 'Slavia', 'Engine': '1.0L TSI', 'Mileage': '19.47 kmpl'},
#         'Creta': {'Price': '₹10.44 lakh', 'Model': 'SX', 'Engine': '1.5L Petrol', 'Mileage': '17 kmpl'},
#         'Ford': {'Price': '₹7.49 lakh', 'Model': 'Figo', 'Engine': '1.2L Petrol', 'Mileage': '18.5 kmpl'}
#     },
#     'off roading car': {
#         'Mahindra Thar': {'Price': '₹13.49 lakh', 'Model': 'LX', 'Engine': '2.0L Petrol', 'Mileage': '15.2 kmpl'},
#         'Jimny': {'Price': '₹12.74 lakh', 'Model': 'Zeta', 'Engine': '1.5L Petrol', 'Mileage': '16.94 kmpl'},
#         'Urban Cruiser': {'Price': '₹9.02 lakh', 'Model': 'Premium', 'Engine': '1.5L Petrol', 'Mileage': '17.03 kmpl'},
#         'Tata Safari': {'Price': '₹15.65 lakh', 'Model': 'XT+', 'Engine': '2.0L Diesel', 'Mileage': '14.08 kmpl'}
#     },
#     'suv': {
#         'Mahindra Scorpio': {'Price': '₹13.54 lakh', 'Model': 'S11', 'Engine': '2.2L Diesel', 'Mileage': '15 kmpl'},
#         'Fortuner': {'Price': '₹32.59 lakh', 'Model': 'Legender', 'Engine': '2.8L Diesel', 'Mileage': '10.4 kmpl'},
#         'Tata Harrier': {'Price': '₹14.49 lakh', 'Model': 'XZ+', 'Engine': '2.0L Diesel', 'Mileage': '16.35 kmpl'},
#         'MG Hector': {'Price': '₹14.73 lakh', 'Model': 'Sharp', 'Engine': '1.5L Petrol', 'Mileage': '13.96 kmpl'}
#     },
#     'sports car': {
#         'BMW M2': {'Price': '₹85.00 lakh', 'Model': 'Competition', 'Engine': '3.0L Petrol', 'Mileage': '10 kmpl'},
#         'Porsche': {'Price': '₹1.20 crore', 'Model': '911', 'Engine': '3.0L Petrol', 'Mileage': '12.8 kmpl'},
#         'Ford Mustang': {'Price': '₹74.61 lakh', 'Model': 'GT', 'Engine': '5.0L V8', 'Mileage': '7.9 kmpl'},
#         'Jaguar': {'Price': '₹99.98 lakh', 'Model': 'F-Type', 'Engine': '2.0L Petrol', 'Mileage': '12.9 kmpl'}
#     }
# }

# # Main program
# while True:
#     n = input('Which type of car do you wish to buy (family cars, off roading car, suv, sports car)? ')
#     n = n.lower()
    
#     if n in car_details:
#         print(f"Available options for {n}:")
#         for car in car_details[n]:
#             print(f"- {car}")
        
#         # Ask the user for specific car choice
#         car_choice = input(f"\nWhich car would you like more details about? ")
#         car_choice = car_choice.title()  # Capitalize the car name to match the dictionary keys
        
#         # Show car details if available
#         if car_choice in car_details[n]:
#             print(f"\nDetails for {car_choice}:")
#             for detail, value in car_details[n][car_choice].items():
#                 print(f"{detail}: {value}")
#         else:
#             print(f"Sorry, we don't have details for {car_choice}.")
    
#     else:
#         print('For now, your choice is not available. Thank you for visiting our showroom!')
    
#     # Option to continue or exit
#     exit_choice = input("\nWould you like to check more cars? (yes/no): ").lower()
#     if exit_choice != 'yes':
#         print("Thank you for visiting our showroom!")
#         break
# Car information dictionary
car_details = {
    'family cars': {
        'Ertiga': {'Price': '₹8.64 lakh', 'Model': 'ZXI', 'Engine': '1.5L Petrol', 'Mileage': '19.01 kmpl', 'Seating': '7-seater'},
        'Kia Carens': {'Price': '₹9.60 lakh', 'Model': 'Prestige', 'Engine': '1.5L Petrol', 'Mileage': '16.5 kmpl', 'Seating': '7-seater'},
        'Tata Nexon': {'Price': '₹7.99 lakh', 'Model': 'XZ+', 'Engine': '1.2L Petrol', 'Mileage': '17.57 kmpl', 'Seating': '5-seater'}
    },
    'off roading cars': {
        'Mahindra Thar': {'Price': '₹13.49 lakh', 'Model': 'LX', 'Engine': '2.0L Petrol', 'Mileage': '15.2 kmpl', 'Seating': '4-seater'},
        'Jimny': {'Price': '₹12.74 lakh', 'Model': 'Zeta', 'Engine': '1.5L Petrol', 'Mileage': '16.94 kmpl', 'Seating': '4-seater'},
        'Urban Cruiser': {'Price': '₹9.02 lakh', 'Model': 'Premium', 'Engine': '1.5L Petrol', 'Mileage': '17.03 kmpl', 'Seating': '5-seater'}
    },
    'suv': {
        'Mahindra Scorpio': {'Price': '₹13.54 lakh', 'Model': 'S11', 'Engine': '2.2L Diesel', 'Mileage': '15 kmpl', 'Seating': '7-seater'},
        'Fortuner': {'Price': '₹32.59 lakh', 'Model': 'Legender', 'Engine': '2.8L Diesel', 'Mileage': '10.4 kmpl', 'Seating': '7-seater'},
        'Tata Harrier': {'Price': '₹14.49 lakh', 'Model': 'XZ+', 'Engine': '2.0L Diesel', 'Mileage': '16.35 kmpl', 'Seating': '5-seater'}
    },
    'sports cars': {
        'BMW M2': {'Price': '₹85.00 lakh', 'Model': 'Competition', 'Engine': '3.0L Petrol', 'Mileage': '10 kmpl', 'Seating': '2-seater'},
        'Porsche 911': {'Price': '₹1.20 crore', 'Model': '911', 'Engine': '3.0L Petrol', 'Mileage': '12.8 kmpl', 'Seating': '2-seater'},
        'Ford Mustang': {'Price': '₹74.61 lakh', 'Model': 'GT', 'Engine': '5.0L V8', 'Mileage': '7.9 kmpl', 'Seating': '4-seater'}
    },
    'electric cars': {
        'Tesla Model S': {'Price': '₹1.50 crore', 'Model': 'Long Range', 'Engine': 'Electric', 'Mileage': '652 km/charge', 'Seating': '5-seater'},
        'Nexon EV': {'Price': '₹14.74 lakh', 'Model': 'XZ+', 'Engine': 'Electric', 'Mileage': '312 km/charge', 'Seating': '5-seater'},
        'MG ZS EV': {'Price': '₹23.38 lakh', 'Model': 'Exclusive', 'Engine': 'Electric', 'Mileage': '419 km/charge', 'Seating': '5-seater'}
    }
}

# Main program
def polite_response(message):
    print(f"\n{message}")
    print("If you need more assistance, feel free to ask! 😊")

# Adding greeting
def greeting():
    print("Hello! 👋 Welcome to our car showroom.")
    print("I'm your assistant here to help you find the perfect car. 🚗")
    print("Feel free to explore various categories and ask questions about your favorite cars.")
    
greeting()  # Call the greeting function at the start

while True:
    n = input('\nWhich type of car do you wish to explore (family cars, off roading cars, suv, sports cars, electric cars)? ').lower()
    
    if n in car_details:
        polite_response(f"Here are the available options for {n}:")
        for car in car_details[n]:
            print(f"- {car}")
        
        # Ask the user for specific car choice
        car_choice = input("\nWhich car would you like more details about? ").lower()  # Convert input to lowercase
        
        # Check if the car choice exists in lowercase and fetch its details using title for formatting
        for car_name in car_details[n]:
            if car_choice == car_name.lower():
                polite_response(f"Details for {car_name}:")
                for detail, value in car_details[n][car_name].items():
                    print(f"{detail}: {value}")
                
                # Offering more help by answering basic questions
                while True:
                    question = input("\nYou can ask me specific questions like 'price', 'engine', 'mileage', 'seating', or type 'exit' to go back: ").lower()
                    
                    if question == 'exit':
                        polite_response("Let's check other cars then.")
                        break
                    elif question in car_details[n][car_name]:
                        polite_response(f"The {question} of {car_name} is {car_details[n][car_name][question]}.")
                    else:
                        polite_response("I'm sorry, I couldn't understand your question. Please try again.")
                break
        else:
            polite_response(f"Sorry, we don't have details for {car_choice}.")
    
    else:
        polite_response("For now, your choice is not available. Please try another category or visit us again later.")
    
    # Option to continue or exit
    exit_choice = input("\nWould you like to check more cars? (yes/no): ").lower()
    if exit_choice != 'yes':
        polite_response("Thank you for visiting our showroom! Have a great day! 👋")
        break
   
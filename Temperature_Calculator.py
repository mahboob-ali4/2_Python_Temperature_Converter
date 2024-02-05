# 7. Create a program that converts temperatures between Fahrenheit and Celsius.
# °F = °C * (9/5) + 32
# °C = (°F - 32) * 5/9
def temperature_converter():
    print("\n ------------------------------ TEMPERATURE CONVERTER MENU ------------------------------")
    print("\nPress 1 to convert Fahrenheit to Celsius: ")
    print("Press 2 to convert Celsius to Fahrenheit: ")
    print("Press 3 to exit the temperature calculator: ")

def user_choice():
    return input("Please, enter your choice: ")

def Fahrenheit_to_Celsius(user_entered_in_fahrenheit):
    temp_in_celcius = ((user_entered_in_fahrenheit - 32)*5)/9
    print(f"{user_entered_in_fahrenheit}°F IN CELCIUS IS EQUAL TO {round(temp_in_celcius, 2)}°C.")

def Celsius_to_Fahrenheit(user_entered_in_celcius):
    temp_in_fahrenheit = ((user_entered_in_celcius * 9)/5) + 32 
    print(f"{user_entered_in_celcius}°C IN FAHRENHEIT IS EQUAL TO {round(temp_in_fahrenheit, 2)}°F.")

def exit_calculator():
    print("YOU EXIT THE TEMPERATURE CALCULATOR.")

while True:
    temperature_converter()
    choice = user_choice()

    if choice == "1":
        try:
            fahrenheit_by_user = float(input("Enter your Fahrenheit temperature to convert it into celcius: "))
            Fahrenheit_to_Celsius(fahrenheit_by_user)
        except ValueError:
            print("PLEASE! ENTER A NUMERIC VALUE.")
    elif choice == "2":
        try:
            celcius_by_user = float(input("Enter your celcius temperature to convert it into Fahrenheit: "))
            Celsius_to_Fahrenheit(celcius_by_user)
        except ValueError:
            print("PLEASE! ENTER A NUMERIC VALUE.")
    elif choice == "3":
        exit_calculator()
        break
    else:
        print("PLEASE, MAKE A VALID CHOICE.")
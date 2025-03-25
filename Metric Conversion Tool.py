#Create a Python program that converts units of measurement,
#  like kilograms to pounds, Celsius to Fahrenheit, meters to feet, and vice versa.
def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084
print("Welcome to Python Unit Conversion! phiss..")
while True:
    print("\nChoose a conversion type:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Meters to Feet")
    print("6. Feet to Meters")
    print("0. Exit")
    user_input=int(input("ENter Your option! : "))
    if user_input==0:
        print("Bye")
        break
    if user_input not in [1, 2, 3, 4, 5, 6]:
        print("Invalid choice. Please try again.")
        continue

    value=int(input("Enter Value to conver : "))
    if user_input == 1:
        print(f"{value} kilograms is {kg_to_pounds(value)} pounds.")
    elif user_input == 2:
        print(f"{value} pounds is {pounds_to_kg(value)} kilograms.")
    elif user_input == 3:
        print(f"{value} Celsius is {celsius_to_fahrenheit(value)} Fahrenheit.")
    elif user_input == 4:
        print(f"{value} Fahrenheit is {fahrenheit_to_celsius(value)} Celsius.")
    elif user_input == 5:
        print(f"{value} meters is {meters_to_feet(value)} feet.")
    elif user_input == 6:
        print(f"{value} feet is {feet_to_meters(value)} meters.")
    else:
        print("Invalid choice. Please try again.")
        


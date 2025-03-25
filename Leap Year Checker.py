#Create a Python program that determines whether a given year is a leap year. It’s a small yet practical project to practice conditional logic.
def leap_year(user_input):
    if (user_input%4==0 and user_input%100==0)or user_input%400==0:
        print(f"{user_input} : is a Leap Year")
    else:
        print(f"{user_input} is not a leap year ")
print("Welcome to the Leap Year Checker!")
print("Type 'exit' or 'bye' to quit the program.")

while True:
    print("Enter your year :")
    user=(input()).lower()
    if user in['exit','bye']:
        print("Goodbye")
        break
    if user.isdigit():
        year=int(user)
        leap_year(year)
    else:
        print("ENter valid number or enter 'exit' or 'bye'")

    
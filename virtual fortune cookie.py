#Build a Python program that generates random fortune messages for the user when they open a "virtual fortune cookie."
import random 
fortunes = [
    "You will have a great day!",
    "Adventure is on the horizon.",
    "An old friend will surprise you soon.",
    "Success will come your way.",
    "Don't forget to take a break today.",
    "A new opportunity is heading your way.",
    "Laugh often, it's good for the soul!"
]
def get_fortune():
    return random.choice(fortunes)

print("Welcome to Virtual Fortune COokie!")
print("Crack OPen to see Your Fortune Today!")
while True:
    user_input=input("Type 'OPEN' to open a fortune cookie or 'EXIT' to exit")
    if user_input=="OPEN":
        print("Your fortune is ",get_fortune())
    elif user_input=="EXIT":
        print("GOOd bye! ")
        break
    else:
        print("Enter 'OPEN' or 'EXIT' ")


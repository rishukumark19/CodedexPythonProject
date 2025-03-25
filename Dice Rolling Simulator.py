#Build a Python program that simulates rolling one or more dice, displaying the result randomly each time. You can even expand it to include different types of dice.
import random
def dice_roll():
    return random.randint(1,6)
print("WElcome to Dice Rolling! ")
print("Please Roll your dice!")
while True:
    user_input=input("Type 'START' to roll your dice . press'STOP' to exit :").upper()
    if user_input=="START":
        dice1=dice_roll()
        dice2=dice_roll()

        print("Your Dice Roll numbers are:",dice1,dice2)
        print("Total = ",dice1+dice2)
    elif user_input=="STOP":
        print("BYE")
        break
    else:
        print("error try again!")

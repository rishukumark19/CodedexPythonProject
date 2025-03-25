#Create a Python program that lets the user play the classic game against the computer. The computer will randomly select "Rock," "Paper," or "Scissors," and the program will determine the winner.
import random
choice=["ROCK","PAPER","SCISSOR"]

def computer_choice():
    return random.choice(choice)
print("Welcome to the Game! ")
user_input = input("Enter your choice " + ", ".join(choice) + " : ").upper()
print("You choose :",user_input)
computer=computer_choice()
print("Computer choice ",computer)

if user_input==computer:
    print("Its a TIE!")
elif (user_input=="ROCK" and computer=="PAPER")or(user_input=="PAPER" and computer=="SCISSOR")or(user_input=="SCISSOR"and computer=="PAPER"):
    print("You won!!")
else:
    print("Computer Won")


#Build a Python program where the user tries to guess a random number within a specific range.
#The program will provide hints if the guess is too high or too low.
#The program should:
# Generate a random number within a specified range (e.g., 1–100).
# Allow the user to guess the number.
# Provide feedback after each guess (too high, too low, or correct).
# Track the number of attempts and display the result.
import random

print("Welcome to the Game !")
print("Guess of a number between 1-100")
print("Totoal attemps is 6")
guess=random.randint(1,100)
print(guess)
attempts=1

while attempts<=6:
    user_guess=int(input("Enter your Guess : "))
    if user_guess==guess:
        print("Vola! You guess it correct!")
        break
    elif user_guess<guess:
        print("HOT: you are guessing low")
        attempts+=1
    elif user_guess>guess:
        print("COLD: you are guessing high")
        attempts+=1          
if attempts==6:
    print(f"Sorry, you've used all your attempts. The correct number was {guess}.")
    

#Create a Python program that allows users to play the classic party game "Truth or Dare." 
# It will ask players to choose between a truth or dare and display a randomly selected prompt.
import random
truths = [
    "What's your most embarrassing memory?",
    "If you could switch lives with anyone, who would it be?",
    "What's the worst thing you've ever done?",
    "What secret have you never told anyone?",
    "What's your biggest fear?"
]

dares = [
    "Dance like crazy for 30 seconds.",
    "Sing your favorite song out loud.",
    "Pretend to be a chicken for one minute.",
    "Text your crush something embarrassing.",
    "Do 10 pushups right now."
]
def random_choice(choice):
    if choice=="truth":
        return random.choice(truths)
    elif choice=="dare":
        return random.choice(dares)
        
while True:
    choice = input("Choose Truth/Dare. Type 'bye' to EXIT: ").lower()
    if choice == "bye":
        print("Goodbye! Thanks for playing.")
        break
    elif choice not in ["truth", "dare"]:
        print("Invalid choice. Please choose 'truth' or 'dare'.")
        continue
    
    challange = random_choice(choice)
    print(f"\nYour {choice} is: {challange}")

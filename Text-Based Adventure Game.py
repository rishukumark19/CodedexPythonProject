#Create a Python program where the user embarks on an interactive adventure. 
# The user makes choices that determine the outcome of the story.\
def start_adventure():
    print("You are in dark forest! you have 2 paths ")
    print("1.Right")
    print("2.Left")
    choice=input("ENter '1':'Right' OR '2':'Left")
    if choice=="1":
        right()
    elif choice=="2":
        left()
    else:
        start_adventure()
def right():
    print("You took Right! You saw Dragon!")
    print("1. Try to sneek pass him before it wakes up")
    print("2. Run back ASAP!!")
    choice=input("Enter your choice (1/2) : ")
    if choice=="1":
        print("Dragon Wakes up! and Killed you . You Died. Game Over!")
    elif choice=="2":
        print("The Dragon Didnt woke up! you survived ! You Won!!")
    else:
        right()
def left():
    print("You Took Left! you see Magiccal Elf who offers you magical portion!")
    print("1. Accept it and Gain Super strength!")
    print("Polietly decline it and Continue!")
    choice=input("Enter Your choice (1/2) : ")
    if choice=="1":
        print("YAY! you won the Game! ")
    elif choice=="2":
        print("You continue the journey but you didnt gain anything . You loose. Game End ")
    else:
        left()
print("Welcome TO the Game!!!")
start_adventure()


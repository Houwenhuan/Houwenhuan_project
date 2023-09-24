import random

number = random.randint(1, 10)
while True:
    user = int(input("enter the number between 1 and 10: "))
    if user == number:
        print("Correct! You guessed the number in ", number)
    elif user < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

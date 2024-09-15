# this is a random number guessing game
# created by hardik thapar
import random
comp_num=random.randint(0,10)

while (True):
    your_num=int(input("enter the number  between 1 to 10: "))
    if(comp_num==your_num):
        print("your guess is right")
        break;
    elif(comp_num>your_num):
        print(f"your guess is too low, the computer guessed {comp_num}")
    else:
        print(f"your guess is too high, the computer guessed {comp_num}")
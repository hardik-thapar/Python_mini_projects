# this is a snake , water, gun game made by- Hardik Thapar

import random
'''
computer- the number computer chooses
s-  = -1
w-water= 0
g-gun = 1
enter- you enter s or w or g
'''

computer=random.choice([-1,0,1])
dict={"s":-1, "w":0, "g":1 }
reverse_dict={-1:"snake", 0:"water", 1:"gun"}
enter=input("enter your choice: ")
you=dict[enter]
print("your choice is: ", reverse_dict[you])
print("compter chose: ", reverse_dict[computer])

if(computer==you):
    print("its a draw!")
else:

    # comp choses -1(snake)
    if(computer==-1 and you==0):
        print("you lose")
    elif(computer==-1 and you==1):
        print("you win")
    # if comp chooses 0(water)
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    # if comp chooses 1(gun)
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    else:
        print("something went wrong")

     
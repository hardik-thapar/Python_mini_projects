import random
def play():
    user=input("what is your choice, enter r for rock, s for scissors, p for paper : ")
    comp=random.choice(['r','s','p'])
    
    if(user==comp):
        return "its a tie !"
    if win(user,comp):
        return "you win!"
    return "you lose !"
def win(user,comp):
    if (user=='r' and comp=='s') or (user=='p' and comp=='r') or (user=='s' and comp=='p'):
        return True
    # r>s,p>r,s>p
print(play())
   
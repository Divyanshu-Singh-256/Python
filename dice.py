#dice 
global susu 
import random
print(" Welcome to Dice roller!!!!!!!")
command=input("Type Roll or roll to start ... ")
def dice_roll():
    dice=(1,2,3,4,5,6)
    x=random.randint(0,5)
    if command not in "RollrollStopstop":
        print("Please enter valid command..")
        return
    if command in "Rollroll":
        print(dice[x])
    
    

def further():
    dice_roll()
    susu=input(" To roll again - Roll or roll ....... To stop - Stop or stop-----")
    while susu in "Rollroll":
        dice_roll()
        susu=input("To roll again - Roll or roll ....... To stop - Stop or stop-----")
    if susu in"Stopstop":
        print("Bye!!! ")
    elif susu not in "RollrollStopstop":
        print("Please enter valid command")
        return 
        
further()

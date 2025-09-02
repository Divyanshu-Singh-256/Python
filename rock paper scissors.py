#rock paper scissors
import random
x=random.randint(1,3)
if x==1:
    computer_choice="rock"
if x==2:
    computer_choice="scisoors"
if x==3:
    computer_choice="paper"
player_choice=input(  "Please input your choice (Rock , Paper , Scissors)")
print("The first choice shown is of computer"
" ,the second choice shown is of player"
" .Finally the verdict is shown")
def two():
    if x==2 and player_choice=="Scissors" or player_choice=="scissors":
        print(computer_choice)
        print(player_choice)
        print("It is a draw")
    if x==2 and player_choice=="Paper" or player_choice=="paper":  
        print(computer_choice)
        print(player_choice)
        print("Computer wins")
    if x==2 and player_choice=="Rock" or player_choice=="rock":
        print(computer_choice)
        print(player_choice)
        print("Player wins")


def three():

    if x==3 and player_choice=="Scissors" or player_choice=="scissors":
        print(computer_choice)
        print(player_choice)
        print("Player wins")
    if x==3 and player_choice=="Paper" or player_choice=="paper":
        print(computer_choice)
        print(player_choice)
        print("It is a draw")
    if x==3 and player_choice=="Rock" or player_choice=="rock":
        print(computer_choice)
        print(player_choice)
        ("COmputer wins")

def one():

    if x==1 and player_choice=="Scissors" or player_choice=="scissors":
        print(computer_choice)
        print(player_choice)
        print("Computer wins")
    if x==1 and player_choice=="Paper" or player_choice=="paper":
        print(computer_choice)
        print(player_choice)
        print("Player wins")
    if x==1 and player_choice=="Rock" or player_choice=="rock":
        print(computer_choice)
        print(player_choice)
        print("It is a draw") 


if x==1:
    one()
if x==2:
    two()
if x==3:
    three()
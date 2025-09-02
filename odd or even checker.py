#odd or even
print("Welcome to Odd or Even checker!!!!")
input=int(input("Enter any number that you want to check odd or even for.....(Please enter only )integers as only they can be classified as Odd or Even...."))
x=input%2
if x!= 0 :
    print (" The number given is Odd")
elif x==0 :
    print("The number given is even")
else:
    print("Please enter valid number")
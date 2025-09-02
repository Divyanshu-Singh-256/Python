import random as rand # areee African currency not what you thought

characters="abcdefghikjlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

def passgen():
    password=""
    len=int(input("How many characters long do you want your password???   "))
    for i in range(len):
        x1=rand.randint(0,26+26+9+9+2-1)
        password += characters[x1]                                                          
        
    
    print(password +" is your random secure password")
gh=int(input("How many passwords do you want??  "))
for a in range(gh):
    passgen()
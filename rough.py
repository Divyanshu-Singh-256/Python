#lesson 1
name="beau"
print(type(name))
print(type(name)==str)

x=20.65
print(type(x))
print(x)
x=int(x)
print(x)
print(type(x))

age=float(2)
print(age)
print(type(age))

a=1
b=2
def rr(a,b):
    return a!=b
z=rr(a,b)
print(z)

#lesson 2
def nn():
    x=3
    if x is 3:
        print(x)
    c="Rough"
    if c in "RoughroughOUGH":
        print(c)

nn()


print("""oola lal la laenn

njrfbnr

vefkjbvv
      
      vnejbnv
                              bnrbroitnb
""")

x="""
lowe r 

to

ippper
"""

x1=x.upper()
print(x1) 

z34="bhgrguirhgb bhifervgberighb"
z35=z34.title()
print(z35)

# isalpha() to check if sttring contains only characters and is not empty
#isalnum()  same thing as above just with addition of numbers
#isdecimal()
#lower()
#upper()
#isupper()
#islower()
#title()
#startswith()
#endswith()
#replace()
#split()
#strip()
#join()
#find()


frhufhx="fguirehnfreufbier"
print(len(frhufhx))

#to use "" in ""
name="divdaddy/""''''''''"
#/n means new line

huhghh="jihfrbkwefnrebfrog"
print(huhghh[3])
print(huhghh[3:7])





complex222 = 2+3j
num=complex(2,3)

def hh():
    return True if num==complex222 else  False
ki=hh()
print(ki)
print(num.real)
print(num.imag)



#lesson 3 


# enum are readable names that are bound to a constant value

from enum import Enum

class state(Enum):
    INACTIVE=0
    ACTIVE=1

print(state.ACTIVE)
print(state.ACTIVE.value)
print(list(state))





# use rinput 


age= input ("What is your age?")
print(age + "is how old you are")  


#lists


ullu=["rf",24,45,7.0,False]
print(type(ullu))
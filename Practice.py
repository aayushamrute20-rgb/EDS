'''
#f string
name = input("Enter your name: ")
print(f"{name} is noted as your name")
age = int(input("Enter your age: "))
print(f"age is noted as {age}")

#Boolean
A = True
print(f"are you a student: {A}")

#Conditional Statement
online = True
if online:
    print("User is online")
else:
    print("User is offline")

#Typecasting
A = ""
B = 15
C = str(B)
print(C)
print(type(C))
print(bool(C))
print(bool(A))

#Reverse a String
D = "Your Name"
E = D[::-1]
print(E)

item = (input("What item would you like?: "))
price = int(input("What is the price?: "))
quantity = int(input("How many of them did you buy?: "))
Total = price*quantity
print("Your total is: ", Total)

q = 13
w = 12.4532
e = -12
# result = round(w, 2)
# result = abs(e)
# result = max(q, w, e)
result =  min(q, w, e)
print(result)

import math as m
a = 11.9
c = m.e
d = m.pi
f = m.ceil(a)
g = m.floor(a)
print(a, c, d, f, g)

# Pythagoras Theorem
import math as m
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = m.sqrt(pow(a, 2)+pow(b, 2))
print(c)

a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = input("Enter the operator(+,-,*,/,%): ")
if c == "+":
    print("The addition is: ", a+b)
elif c == "-":
    print("The subtraction is: ", a-b)
elif c == "*":
    print("The multiplication is: ", a*b)
elif c == "/":
    print("The division is: ", a/b)
elif c == "%":
    print("The remainder is: ", a%b)
else:
    print(f"{c} is not a valid operator.")

# Python Weight Converter
W = float(input("Enter the Weight: "))
U = input("Enter unit KIlogram or Pound (K or L): ")
if U == "K":
    W = W*2.205
    U = "Lbs"
    print(f"Weight is: {W}{U}")
elif U == "L":
    W = W/2.205
    U = "Kg"
    print(f"Weight is: {W}{U}")
else:
    print(f"{U} is not a valid input")

o = float(input("Enter the Temperature: "))
u = input("Enter the Unit;Fahrenheit or Celcius (F or C): ")
def temp(q):
    if u == "F":
        return f"{(o-32)/1.8} degree celcius"
    elif u == "C":
        return f"{(o*1.8)+32} degree fahrenheit"
    else:
        return "Unit not Valid"
print(temp(o))

s = float(input("Enter the Temp.: "))
if  15<s<=28:
    print("Fine,Get outside time to touch some grass")
elif 28<s<40:
    print("We're cooked!!")
else:
    print("Time to die")
    
# X if condition else Y
q = int(input("Enter number to check if its two digit: "))
def prime():
    r = "Valid" if 9<q<100 else "Not Valid"
    return r
print(prime())

#Some Functions
name = input("Enter your name: ")
r = len(name)
y = name.find("y")
e = name.rfind("a") #last recurrence of a character
l = name.rfind("d") #returns -1 if there  is no value
d = name.capitalize()
x = name.lower()
g = name.upper()
k = name.isdigit() #if only digits present returns True
j = name.isalpha() #if only alpha present returns True "Excluding spaces"
h = name.count("a")
s = name.replace("a", "stioc")
print(y,e,l,d,x,g,k,j,h,s)
# print(help(str))

a = input("Enter the username: ")
if not a.rfind(" ") == -1:
    print("Username contains space")
elif a.isalpha():
        if len(a) <= 12:
            print("Username Valid.")
        else:
            print("Username not Valid.(Contains more than 12 characters)")
else:
    print("Usernme not Valid.(Contains digit.)")

#Format Specifires
w = 1246.4556
s = 231.536
z = -422423.06797
print(f"the amount is $ {w:.2f}")
print(f"the amount is $ {s:+,.2f}")
print(f"the amount is $ {z:,}")
print(f"the amount is $ {z:^20}")
print(f"the amount is $ {z:<20}")

#While loop (Compount Intrest)
p = float(input("Enter the Principle amount: "))
while p<= 0:
    print("Principle cannot be negative or zero.")
    print("Enter the Principle amount: ")
r = float(input("enter the Rate: "))
while r<= 0:
    print("Rate cannot be negative or zero.")
    print("Enter the Rate: ")
t = float(input("enter the Time: "))
while t<= 0:
    print("Time cannot be negative or zero.")
    print("Enter the Time: ")
amt = p*pow((1+r/100),t)
print(f"Balance after {t} year/s: ${amt:.2f}")

# For Loop
import time as t
e = int(input("Enter the countdown: "))
for i in range(e, 0, -1):
    print(i)
    t.sleep(1)
print("Time's Up")
'''
#Nested Loop

#Python Collections
'''
kl = ["bruhh","nowwwwh","hewll","forp","larp"]
#print(dir(kl))
#print(help(kl))
#kl[1] = "holy"
#kl.append("moly")
print(len(kl))
#kl.remove("forp")
#kl.insert(3,"foid")
#kl.sort()
#kl.reverse()
#kl.count("foid")
#kl.clear()
print(kl)
'''
'''
kl = {"bruhh","nowwwwh","hewll","forp","larp"}
#kl.add("yoink")
#kl.add("larp")
#kl.remove("forp")
#kl.pop()
#kl.clear()
print(kl)
'''
'''
kl = ("bruhh","nowwwwh","hewll","forp","larp")
#print("bruhh" in kl)
print(kl.index("nowwwwh"))
print(kl.count("bruhh"))
print(kl)
'''
#2D collections
#Dictionary
'''
menu = {"pizza": 10.99, "burger": 7.99, "fries": 3.99, "soda": 1.99, "salad": 5.99}
total = 0
print("-----MENU-----")
for food, price in menu.items():
    print(f"{food:10}: ${price:.2f}")
print("--------------")

while True:
    order = input("What would you like to order?(q to quit): ").lower()
    if order == "q":
        break
    else:
        total += menu[order]
print(f"Your total is: ${total}")
'''
#Random module
'''
import random as rd
p = rd.randint(0,100)
print("**** Number Guessing Game ****")
print("Enter number between 1 to 100")
Totl = 0
while True:
    s = int(input("Guess the number: "))
    if 0<s<101:
        if s < round(p*0.7):
            print("Too low.Try again")
            Totl += 1
        elif s > round(p*1.3):
            print("Too high.Try again")
            Totl += 1
        elif round(p*0.7) < s < p:
            print("Low.Try again")
            Totl += 1
        elif p < s < round(p*1.3):
            print("High.Try again")
            Totl += 1
        else:
            print("Correct Guess")
            print(f"Total Guesses: {Totl}")
            break
    else:
        print("Number out of range.Try Again")

'''
#functions
'''
def addup(*asz):
    #print(type(asz)) #tuple
    total = 0
    for a in asz:
        total += a
    return total
print(addup(1,2,3,4,5,6,7,8,9))
'''
'''
def address(**kwargs):
    #print(type(kwargs)) #dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")
address(street= "Anand Nagar",
        landmark= "Flour Mill",
        city= "Betul",
        state= "M.P."
        )
'''
'''
def order_summary(*args, **kwargs):
    for arg in args:
        print(arg,end = " ")
    print()
    #for value in kwargs.values():
        #print(value, end=" ")
    print(f"{kwargs.get('order')} to {kwargs.get('house')}, {kwargs.get('city')}")
order_summary("Aayush","Amrute",
              order = "shipped",
              house = "Anand Nagar 062",
              city = "Betul")
'''
#iterables strings,lists,tuples,sets
'''
dictionary = {"a": 2,"b": 23,"c":234}
#for value in dictionary.values():
    #print(value, end = " ")
for key, value in dictionary.items():
    print(f"{key} = {value}")
'''
#membership operators in,not in returns boolean True or False

#List comprehension [expression for value in iterable if condition]
'''
fruits = ["apple","banana","pineapple","papaya","orange"]
names_fruit = [fruit[0].upper() for fruit in fruits]
print(names_fruit)
'''
'''
fruits = ["apple","banana","pineapple","papaya","orange"]
names_fruit = [fruit[0].upper() for fruit in fruits if fruit[0] == "p"] 
print(names_fruit)
'''
#Match case statements(switch)
'''
def weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return "This is weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Nice try diddi"
k = input("Enter the day: ")
print(weekend(k))
'''
#Module

#variable scope
#scope resolution(LEGB)

#if __name__ == '__main__':

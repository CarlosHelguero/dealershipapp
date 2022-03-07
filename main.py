import os 
from os import system 
import actions as Action
from sqlActions import insertcustomerdata
system('clear')

print(f'''
    Welcome to the dealership
    are you a existing customer 
    or a new customer?
''')
customerselector = int(input("pick a option"))

if customerselector == 1:
   person = Action.pickacustomer()
elif customerselector == 2:
   
    Action.addanewcustomer()
    print ("lets save your infomation")



customeractions = ['buy car','update info']
x = 1
for cAction in customeractions:
    print("     ", x, ".  ", cAction)
    x = x + 1
customerselector = int(input("pick a option >>>>  "))
if customerselector == 1:
    cars = Action.pickcar()
    print("proceed to check out?")
    selector=input("y/n  ")
    if selector == "y":
        Action.checkout(person, cars)
    elif selector == "n":
        print("integrate loop")

elif customerselector == 2:
    print("feature hasnt been done yet")
    
    



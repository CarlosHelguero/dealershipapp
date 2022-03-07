import os 
from os import system 
from customer import Customer
import sqlActions as sql


def showcustomers():
    sql.readcustomerdatabase()
def addanewcustomer():
    print("please insert the following information")
    customer = Customer()
    fname = input("What is your first name? >> ")
    customer.setfirstname(fname)
    lname = input("What is your last name? >> ")
    customer.setlastname(lname)
    email = input("What is your email? >> ")
    customer.setemail(email)
    phone = input("What is your phone number? >> ")
    customer.setphone(phone)
    discount= input("are you a veteran or disabled? T/F ")
    customer.setvetdisable(discount)
    
    sql.insertcustomerdata(customer.getfirstname(), customer.getlastname(), customer.getemail(
    ), customer.getphone(), customer.getvetdisable())
def pickacustomer():
    
    showcustomers()
    userinfo = input("pick your profile")
    person = sql.pickaprofile(userinfo)
    return person

def showcars():
    sql.getcarinfo()
def pickcar():
    cars = []
    total = 0
    numberofcars = int(input("how many cars do you want to buy"))
    for car in range(numberofcars):
        showcars()
        carselector = int(input("select using the car ID >>>> "))
        cars.append(sql.pickacar(carselector))
    print("   ALL Cars in shopping cart")
    for car in cars:
        print(f''' 
        make ....... {car[1]}
        model ...... {car[2]}
        year ....... {car[3]}
        color ...... {car[4]}
        price ...... {car[5]}
        
        ''')
        total = total + car[5]
    print("  subtotal is $",total)
    return cars, total
def checkout(customer, cars):
    print("soon")
    #discounts will be here
    carids = []
    customerid = customer[0]
    for car in cars:
        carids.apped(car[0])

    return customerid, carids





    

    




       
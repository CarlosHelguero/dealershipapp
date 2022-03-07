import connection as c
import mysql.connector

def readcustomerdatabase():
    connection = c.returnConnection()
    try:
        table = connection.cursor()
        table.execute('USE dealershipapp')
        table.execute('SELECT * FROM customer')
        for row in table:
            print(f'''
                  id .............. {row[0]}
                  First Name ...... {row[1]}
                  Last Name ....... {row[2]}
                  Email ........... {row[3]}
                  Phone ........... {row[4]}
                  Discount .........{row[5]}
                  ''')
        table.close()
        connection.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)

def insertcustomerdata(firstname, lastname, email, phone, discount):
    connection = c.returnConnection()
    try: 
        table = connection.cursor()
        table.execute('USE dealershipapp')
        table.execute(
            f"INSERT INTO customer (fname, lname, email, phone, vetdisabled) VALUES ('{firstname}', '{lastname}', '{email}' , '{phone}', '{discount}') ")
        connection.commit()
        table.close()
        connection.close()
        
    except (Exception, mysql.connector.Error) as error: 
        print('Error while fetching data from my MySQL', error)
def pickaprofile(customerid):
    connection = c.returnConnection()
    try: 
        table = connection.cursor()
        table.execute('USE dealershipapp')
        table.execute(f"SELECT * FROM customer WHERE customerID = '{customerid}' ")
        profile =table.fetchone()
        return profile

    except (Exception, mysql.connector.Error) as error: 
        print('Error while fetching data from my MySQL', error)


def getcarinfo():
    connection = c.returnConnection()
    try: 
        table = connection.cursor()
        table.execute('USE dealershipapp')
        table.execute('select * FROM product WHERE productID <= 5')
        for row in table:
            print(f'''
                id .............. {row[0]}
                Make ............ {row[1]}
                Model ........... {row[2]}
                year ............ {row[3]}
                color ........... {row[4]}
                price ............{row[5]}
                ''')
        table.close()
        connection.close()
             
    except (Exception, mysql.connector.Error) as error: 
        print('Error while fetching data from my MySQL', error)
def pickacar(productid):
    connection = c.returnConnection()
    try: 
        table = connection.cursor()
        table.execute('USE dealershipapp')
        table.execute(f"SELECT * FROM product WHERE productID = '{productid}' ")
        car =table.fetchone()
        return car

    except (Exception, mysql.connector.Error) as error: 
        print('Error while fetching data from my MySQL', error)


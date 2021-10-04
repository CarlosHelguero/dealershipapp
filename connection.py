import mysql.connector, os
from mysql.connector import connect 
def returnConnection():
    conn = connect(
        host = "mydatabasee.cphw5qnsj00k.us-east-1.rds.amazonaws.com",
        user = "admin",
        password = "rootroot",
        database = "mydatabaseaci"
    )
    return conn
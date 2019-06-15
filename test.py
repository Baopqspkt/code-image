import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
Name = "Uyen"

def login():
    try:
        connection = mysql.connector.connect(host = "103.95.197.126",
        user = "baopqspkt",
        passwd = "bao0985265185",
        database = "baopqspk_control")
    
        sql_insert_query = """ INSERT INTO `Door`
                          (`Day`,`Name`) VALUES (%s,%s)"""
        cursor = connection.cursor()
        result  = cursor.execute(sql_insert_query,(formatted_date,Name))
        connection.commit()
        print ("Record inserted successfully into python_users table")

    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
login()
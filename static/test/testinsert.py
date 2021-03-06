import csv
import psycopg2
import pandas as pd
from psycopg2 import Error
import datetime as dt
import time

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "plf@iot",
                                  host = "192.168.1.6",
                                  port = "5432",
                                  database = "postgres")


    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")



    with open('test.csv','r') as file:
        csv_reader = csv.reader(file)

        for line in csv_reader:
            cursor.execute(
            "INSERT INTO testdeploy VALUES (%s)",
            line
            )
            print(line)
            

    connection.commit()

    print("Data inserted successfully to PostgreSQL ")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL :", error)

finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# CREATE TABLE public.pl6_test (

# );
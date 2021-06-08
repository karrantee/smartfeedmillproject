# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# import operation
# from sqlalchemy import create_engine
# import pandas as pd

# db= SQLAlchemy(app)
# user = 'postgres'
# pwd = '12345'
# host = '127.0.0.1'
# port = '5432'
# dbname = 'test'


# con = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')


# print("Connected to database successfully")




# per = pd.read_sql('select "Performance" from showall order by "field1" Desc limit 1;',con)
# # per.head()
# print(per)

# ---------------------------------------

import csv
import psycopg2
from psycopg2 import Error
import datetime
import time

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "plf@iot",
                                  host = "192.168.1.6",
                                  port = "5432",
                                  database = "postgres")
#cursor
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

#     create_table_query = '''CREATE TABLE public.Test_2
# (
#     id serial, "timestamp" timestamp without time zone,
#     location character varying(20),
#     device character varying(10),
#     Temp_1 numeric(8,2),
#     Temp_2 numeric(8,2),
#     Temp_3 numeric(8,2),
#     Temp_4 numeric(8,2)
# ); '''

    test = ''' CREATE TABLE IF NOT EXISTS public.testdeploy (
    "Datetime" timestamp NOT NULL,
    "PL6_Formula_Name" VARCHAR(255) NOT NULL,
    "Shift" VARCHAR(2) NOT NULL,
    "PL6_Job_ID" VARCHAR(5) NOT NULL

    ); '''

    csv_file_name = "..//2021-05-29.csv"
    sql = "COPY Datetime,PL6_Formula_Name, Shift, PL6_Job_ID FROM STDIN DELIMITER ',' CSV HEADER"
    cursor.copy_expert(sql, open(csv_file_name, "r"))
    # cursor.execute(create_table_query)
    cursor.execute(test)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# CREATE TABLE public.pl6_test (

# );
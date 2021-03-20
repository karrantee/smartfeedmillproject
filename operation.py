from sqlalchemy import create_engine
import pandas as pd
import numpy as nd
import matplotlib.pyplot as plt


# def connectdb():

user = 'postgres'
pwd = '12345'
host = '127.0.0.1'
port = '5432'
dbname = 'test'
con = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')


print("Connected to database successfully")


def graph():

    df = pd.read_sql('select ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" from showall group by date("DateTime") order by date("DateTime") ASC;',con)
    df.head()
    # print(df)

    con.commit()

    con.close()

    df.plot(x='DateTime',y='Performance',figsize=(15,6),linestyle='--', marker='*', markerfacecolor='r',color='y',markersize=10)

    plt.xlabel('DateTime')
    plt.ylabel('Performance')

    plt.show()

def showPerformance():

    df = pd.read_sql('select "Performance" from showall order by "field1" Desc limit 1;',con)
    # df.head()
    print(df)


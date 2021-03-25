from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import operation
import psycopg2


# try with psycopg2
# conn = psycopg2.connect(
#     host="localhost",
#     database="test",
#     user="postgres",
#     password="12345")


# cur = conn.cursor()

# cur.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from showall where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) = $$2019-W22$$ group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$)')

# rows = cur.fetchall()

# print(rows)

# cur.close()
# conn.close()

user = 'postgres'
pwd = '12345'
host = '127.0.0.1'
port = '5432'
dbname = 'test'
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')

connection = engine.raw_connection()
cur = connection.cursor()

cur.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from showall where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) = $$2019-W22$$ group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$)')

rows = cur.fetchone()

print(rows)

cur.close()

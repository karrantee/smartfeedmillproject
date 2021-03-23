from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import operation
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="12345")


cur = conn.cursor()

cur.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime" from showall group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) order by "DateTime" ASC limit 1')

rows = cur.fetchall()

print(rows)

cur.close()
conn.close()
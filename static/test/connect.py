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
pwd = 'plf@iot'
host = '192.168.1.6'
port = '5432'
dbname = 'postgres'
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')

connection = engine.raw_connection()
cur = connection.cursor()

# cur.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from showall where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) = $$2019-W22$$ group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$)')

# rows = cur.fetchone()

# print(rows)

# cur.close()


db = scoped_session(sessionmaker(bind=engine))

# formula = db.execute('SELECT DISTINCT "FORMULA" from "PL6_Daily"')


# fo = formula.fetchall()
# for row in fo:
#     t = row['FORMULA']
#     # print(t)

# shift = db.execute('SELECT DISTINCT "SHIFT" from "PL6_Daily" ')
# shift = shift.fetchmany(1)
# # shift = shift.fetchall()
# print(shift)
# for i in shift:
#     shet = i['SHIFT']
# print(shet)

# performance = db.execute('SELECT DISTINCT "FORMULA","SHIFT", ("DATETIME"::timestamp::date) as "DateTime", "PERFORMANCE" FROM "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = $$2020-01-02$$ AND "FORMULA" = $$567SF-SWD$$  AND "SHIFT" = $$S3$$ GROUP BY "FORMULA", "SHIFT", date("DATETIME"),"PERFORMANCE" ORDER BY date("DATETIME")')
# pero= performance.fetchmany(3)
# print(performance)
# print(pero)
# for gg in pero:
#     ez = gg['FORMULA']
# print(ez)

# current = db.execute('SELECT "current" from showall order by "DateTime" DESC limit 1')

# for row in current:
#     cu = row['current']
#     print(cu)

# print(current)


# ex = db.execute('SELECT DISTINCT "FORMULA", "DATETIME","SHIFT", ("DATETIME"::timestamp::date) as "DateTime", "PERFORMANCE" from "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = $$2020-01-03$$ AND "FORMULA" = $$553LF-WD PIG FIN1$$ AND "SHIFT" = $$S3$$  ' ).fetchall()
# print(ex)
# for ed in ex:
#     er = ed['PERFORMANCE']

# print(er)

# date = cur.execute('SELECT TO_CHAR("DATETIME", $$YYYY-MM-DD$$) from "PL6_Daily" limit 1').fetchall()
# print(date)

tro = db.execute('SELECT TO_CHAR("DATETIME", $$DD-MM-YYYY HH24:MI:SS$$) as "Datetime", "PERFORMANCE" FROM "PL6_Daily" ORDER BY "DATETIME" DESC limit 10 ').fetchall()
print(tro)

for i in tro :
    damn = i['PERFORMANCE']
    print(damn)


cur.close()


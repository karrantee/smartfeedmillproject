from flask import Flask, render_template, request,json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import operation
# import psycopg2

user = 'postgres'
pwd = '12345'
host = '127.0.0.1'
port = '5432'
dbname = 'test'
# engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}',pool_size=100, max_overflow=0)
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
db = scoped_session(sessionmaker(bind=engine))

# conn = psycopg2.connect(
#     host="localhost",
#     database="test",
#     user="postgres",
#     password="12345")

# cur = conn.cursor()

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route('/')
def home():

    date = db.execute('SELECT "FORMULA","DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "PERFORMANCE" from "PL6_Daily" order by "DATETIME" DESC limit 1')

    for row in performance:
        id = row['PERFORMANCE']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "MOTOR CURRENT" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    
    for row in current:
        cu = row['MOTOR CURRENT']
        print(cu)


    econ = db.execute('SELECT TO_CHAR("ELECTRIC CONS", $$9999D99$$) AS "ELECTRIC CONS" from "PL6_Daily" order by "DATETIME" DESC limit 1')
        
    for row in econ:
        ec = row['ELECTRIC CONS']
        print(ec)

    print(ec)
    


    return render_template("home.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu,ec=ec)

@app.route('/realtime2')
def realtime2():

    date = db.execute('SELECT "FORMULA","DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "PERFORMANCE" from "PL6_Daily" order by "DATETIME" DESC limit 1')

    for row in performance:
        id = row['PERFORMANCE']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "MOTOR CURRENT" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    
    for row in current:
        cu = row['MOTOR CURRENT']
        print(cu)

    # print(current)
    
    econ = db.execute('SELECT TO_CHAR("ELECTRIC CONS", $$9999D99$$) AS "ELECTRIC CONS" from "PL6_Daily" order by "DATETIME" DESC limit 1')
        
    for row in econ:
        ec = row['ELECTRIC CONS']
        print(ec)

    print(ec)

    return render_template("realtime2.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu,ec=ec)

@app.route('/realtime3')
def realtime3():

    date = db.execute('SELECT "FORMULA","DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "PERFORMANCE" from "PL6_Daily" order by "DATETIME" DESC limit 1')

    for row in performance:
        id = row['PERFORMANCE']
        print(id)

    

    # print(performance.fetchall())

    current = db.execute('SELECT "MOTOR CURRENT" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    
    for row in current:
        cu = row['MOTOR CURRENT']
        print(cu)

    # print(current)
    
    econ = db.execute('SELECT TO_CHAR("ELECTRIC CONS", $$9999D99$$) AS "ELECTRIC CONS" from "PL6_Daily" order by "DATETIME" DESC limit 1')
        
    for row in econ:
        ec = row['ELECTRIC CONS']
        print(ec)

    print(ec)

    return render_template("realtime3.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu,ec=ec)

@app.route('/realtime4')
def realtime4():
    
    date = db.execute('SELECT "FORMULA","DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "PERFORMANCE" from "PL6_Daily" order by "DATETIME" DESC limit 1')

    for row in performance:
        id = row['PERFORMANCE']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "MOTOR CURRENT" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    
    for row in current:
        cu = row['MOTOR CURRENT']
        print(cu)

    # print(current)

    econ = db.execute('SELECT TO_CHAR("ELECTRIC CONS", $$9999D99$$) AS "ELECTRIC CONS" from "PL6_Daily" order by "DATETIME" DESC limit 1')
        
    for row in econ:
        ec = row['ELECTRIC CONS']
        print(ec)

    print(ec)

    return render_template("realtime4.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu,ec=ec)

@app.route('/realtime5')
def realtime5():
    
    date = db.execute('SELECT "FORMULA","DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "PERFORMANCE" from "PL6_Daily" order by "DATETIME" DESC limit 1')

    for row in performance:
        id = row['PERFORMANCE']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "MOTOR CURRENT" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    
    for row in current:
        cu = row['MOTOR CURRENT']
        print(cu)

    # print(current)

    econ = db.execute('SELECT TO_CHAR("ELECTRIC CONS", $$9999D99$$) AS "ELECTRIC CONS" from "PL6_Daily" order by "DATETIME" DESC limit 1')
        
    for row in econ:
        ec = row['ELECTRIC CONS']
        print(ec)

    print(ec)

    return render_template("realtime5.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu,ec=ec)

@app.route('/realtime6')
def realtime6():
    
    date = db.execute('SELECT "FORMULA","DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DATETIME" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "PERFORMANCE" from "PL6_Daily" order by "DATETIME" DESC limit 1')

    for row in performance:
        id = row['PERFORMANCE']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "MOTOR CURRENT" from "PL6_Daily" order by "DATETIME" DESC limit 1')
    
    for row in current:
        cu = row['MOTOR CURRENT']
        print(cu)

    # print(current)

    econ = db.execute('SELECT TO_CHAR("ELECTRIC CONS", $$9999D99$$) AS "ELECTRIC CONS" from "PL6_Daily" order by "DATETIME" DESC limit 1')
        
    for row in econ:
        ec = row['ELECTRIC CONS']
        print(ec)

    print(ec)

    return render_template("realtime6.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu,ec=ec)



@app.route('/test', methods=["POST", "GET"])
def test():

    atday=request.form.get("atday")
    atday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = :atday GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"atday":atday})
   

    startday=request.form.get("startday")
    endday=request.form.get("endday")
    per = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday AND :endday GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday": startday, "endday": endday}) 
    # per = per.first()[0]

    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    # print(maxday)

    percent=request.form.get("percent")

    db.commit()
    # print(startday) 
    # print(endday)
    # print(per)
    # print(percent)
    print(atday)

    return render_template("test.html",per=per,maxday=maxday,minday=minday,percent=percent,atday=atday)


@app.route('/selectDate', methods=["POST","GET"])
def selectDate():
    selectDate =  request.form['atday'];
    print(selectDate)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = :selectDate  GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC ',{"selectDate":selectDate})
    maxday = maxday.fetchall()

    return json.dumps({'status':'OK','DATA': maxday,'date' : selectDate})
    return request.form['atday']


@app.route('/testday', methods=["POST", "GET"])
def testday():


    # Show performance after query
    
    selectday =     request.form.get("atday")
    selectformula = request.form.get("formulavalue")
    selectshift =   request.form.get("shiftvalue")

    # Max and min day limit in calendar
    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    # print(maxday)

    # List formula in drop down list
    formula = db.execute('SELECT DISTINCT "FORMULA" , TO_CHAR("DATETIME", $$YYYY-MM-DD$$) AS "DATETIME" FROM "PL6_Daily" WHERE TO_CHAR("DATETIME", $$YYYY-MM-DD$$) = :selectdate',{"selectdate":selectday}).fetchall()

    # List shift in drop down list
    shift = db.execute('select DISTINCT "FORMULA", "SHIFT", TO_CHAR("DATETIME", $$YYYY-MM-DD$$) as "DATETIME" from "PL6_Daily" where TO_CHAR("DATETIME", $$YYYY-MM-DD$$) = :dayy AND "FORMULA" = :formula ',{"dayy":selectday,"formula":selectformula}).fetchall()
    
    # sentDate =      request.form.get("atday")

    print(selectday)

    # print("formula : "+selectformula)
    # print("shift : "+selectshift)
    # print("day : "+selectday)

    performance = db.execute('SELECT DISTINCT "FORMULA" ,"SHIFT", TO_CHAR("PERFORMANCE", $$999d99$$) AS "PERFORMANCE" from "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = $$2020-01-03$$ AND "FORMULA" = $$553LF-WD PIG FIN1$$ AND "SHIFT" = $$S3$$  ' ).fetchall()
    for d in performance:
        performance = d['PERFORMANCE']

    # print(performance)


    test = db.execute('SELECT DISTINCT "FORMULA", TO_CHAR("DATETIME", $$YYYY-MM-DD$$) as "DATETIME","SHIFT","PERFORMANCE", to_char("MOTOR CURRENT"::real, $$9999D99$$) as "MCUR", to_char("STEAM CONSUMPTION"::real, $$999D99$$) as "SCON",to_char("ELECTRIC CONS"::real, $$999D99$$) as "ECON", to_char("%LOAD"::real, $$999D99$$) as "LOAD", "TOTAL_FEED" FROM "PL6_Daily" WHERE "FORMULA" = :formula  AND TO_CHAR("DATETIME", $$YYYY-MM-DD$$) = :ezday  AND "SHIFT" = :shift ' , {"formula": selectformula,"shift":selectshift,"ezday":selectday} ).fetchall()
    # print(test)
    # for tz in test:
    #     test1 = tz['PERFORMANCE']

    # print(test1)

    # print(performance)
    # perform = db.execute('SELECT DISTINCT "FORMULA", "DATETIME","SHIFT", ("DATETIME"::timestamp::date) as "DATETIME", "PERFORMANCE" from "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = :selectday AND "FORMULA" = $$553LF-WD PIG FIN1$$ AND "SHIFT" = $$S3$$  ',{"selectday": selectday, "selectshift": selectshift, "selectformula": selectformula} )
    # print(perform)
    # for p in perform:
    #     performa = p['PERFORMANCE']

    # print(performa)
   
    db.commit()
    db.close()

    return render_template("testday.html",maxday=maxday,minday=minday,selectday=selectday,selectformula=selectformula,selectshift=selectshift,formula=formula,shift=shift,performance=performance,test=test)
    return request.form['formulavalue','shiftvalue']

@app.route('/testweek', methods=["POST", "GET"])
def testweek():
    
    startweek=request.form.get("startweek")
    endweek=request.form.get("endweek")
    atweek=request.form.get("atweek")

    connection = engine.raw_connection()
    cur = connection.cursor()

    # theweek = cur.execute('SELECT TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) as "DATETIME", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from "PL6_Daily" where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) = $$:atweek$$ group by TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$)',{"atweek": atweek})

    # theweek = cur.fetchone()

    # print(theweek)

    theweek = db.execute('SELECT TO_CHAR("DATETIME"::timestamp::date, $$YYYY-"W"WW$$),"FORMULA", ROUND(AVG("PERFORMANCE"::BIGINT),2) AS "PERFORMANCE" from "PL6_Daily" where TO_CHAR("DATETIME"::timestamp::date, $$YYYY-"W"WW$$) = :atweek group by TO_CHAR("DATETIME"::timestamp::date, $$YYYY-"W"WW$$),"FORMULA"ORDER BY TO_CHAR("DATETIME"::timestamp::date, $$YYYY-"W"WW$$) ',{"atweek": atweek})
    # theweek = theweek.first()[0]
    for i in theweek:
        daweek = i['PERFORMANCE']

    # cur.execute('SELECT TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) as "DATETIME", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from "PL6_Daily" where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) = $$atweek$$ group by TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) ',{"atweek": atweek})
    # theweek = cur.fetchall()

    minweek = db.execute('SELECT TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) as "DATETIME" from "PL6_Daily" group by TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) order by "DATETIME" ASC limit 1')
    minweek = minweek.first()[0]
    # print(minweek)

    maxweek = db.execute('SELECT TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) as "DATETIME" from "PL6_Daily" group by TO_CHAR("DATETIME" :: DATE, $$YYYY-"W"WW$$) order by "DATETIME" DESC limit 1 ')
    maxweek = maxweek.first()[0]
    # print(maxweek)


    

    db.commit()
    # print(startday) 
    # print(endday)
    print(theweek)
    print(atweek)
    
   

    # return render_template("testweek.html",per=per,maxweek=maxweek,minweek=minweek,percent=per,atweek=atweek)
    return render_template("testweek.html",atweek=atweek,minweek=minweek,maxweek=maxweek,theweek=theweek)

@app.route('/testmonth', methods=["POST", "GET"])
def testmonth():
    selectmonth = request.form.get('pickmonth')

    print(selectmonth)



    return render_template("testmonth.html")



@app.route('/machine13', methods=["POST", "GET"])
def machine13():

    startday13=request.form.get("startday13")
    endday13=request.form.get("endday13")
    per13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday13 AND :endday13 GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday13": startday13, "endday13": endday13}) 
    
    # per = per.first()[0]

    minday13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday13 = minday13.first()[0]
    # print(minday)

    maxday13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday13 = maxday13.first()[0]

    
    return render_template("machine13.html",per13=per13,maxday13=maxday13,minday13=minday13)


@app.route('/machine46', methods=["POST", "GET"])
def machine46():

    startday46=request.form.get("startday46")
    endday46=request.form.get("endday46")
    per46 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday46 AND :endday46 GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday46": startday46, "endday46": endday46}) 
    
    # per = per.first()[0]

    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    
    return render_template("machine46.html",per46=per46,maxday=maxday,minday=minday)


@app.route('/machine13day', methods=["POST", "GET"])
def machine13day():

    atday=request.form.get("atday")
    atday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = :atday GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"atday":atday})
    # atdayy = atday
    # for d in atdayy:
    #     atdayy = d['Performance']

    startday=request.form.get("startday")
    endday=request.form.get("endday")
    
    per = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday AND :endday GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday": startday, "endday": endday}) 
    # per = per.first()[0]

    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    # print(maxday)

    percent=request.form.get("percent")

    db.commit()
    # print(startday) 
    # print(endday)
    # print(per)
    # print(percent)
    print(atday)

    
    return render_template("machine13day.html",per=per,maxday=maxday,minday=minday,percent=percent,atday=atday)
    
@app.route('/machine13week', methods=["POST", "GET"])
def machine13week():

    startday13=request.form.get("startday13")
    endday13=request.form.get("endday13")
    per13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday13 AND :endday13 GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday13": startday13, "endday13": endday13}) 
    
    # per = per.first()[0]

    minday13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday13 = minday13.first()[0]
    # print(minday)

    maxday13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday13 = maxday13.first()[0]

    
    return render_template("machine13week.html",per13=per13,maxday13=maxday13,minday13=minday13)

@app.route('/machine13month', methods=["POST", "GET"])
def machine13month():

    startday13=request.form.get("startday13")
    endday13=request.form.get("endday13")
    per13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday13 AND :endday13 GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday13": startday13, "endday13": endday13}) 
    
    # per = per.first()[0]

    minday13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday13 = minday13.first()[0]
    # print(minday)

    maxday13 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday13 = maxday13.first()[0]

    
    return render_template("machine13month.html",per13=per13,maxday13=maxday13,minday13=minday13)

@app.route('/machine46day', methods=["POST", "GET"])
def machine46day():

   # Show performance after query
    
    selectday =     request.form.get("atday")
    selectformula = request.form.get("formulavalue")
    selectshift =   request.form.get("shiftvalue")

    # Max and min day limit in calendar
    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    # print(maxday)

    # List formula in drop down list
    formula = db.execute('SELECT DISTINCT "FORMULA" , TO_CHAR("DATETIME", $$YYYY-MM-DD$$) AS "DATETIME" FROM "PL6_Daily" WHERE TO_CHAR("DATETIME", $$YYYY-MM-DD$$) = :selectdate',{"selectdate":selectday}).fetchall()

    # List shift in drop down list
    shift = db.execute('select DISTINCT "FORMULA", "SHIFT", TO_CHAR("DATETIME", $$YYYY-MM-DD$$) as "DATETIME" from "PL6_Daily" where TO_CHAR("DATETIME", $$YYYY-MM-DD$$) = :dayy AND "FORMULA" = :formula ',{"dayy":selectday,"formula":selectformula}).fetchall()
    
    # sentDate =      request.form.get("atday")

    print(selectday)

    # print("formula : "+selectformula)
    # print("shift : "+selectshift)
    # print("day : "+selectday)

    performance = db.execute('SELECT DISTINCT "FORMULA" ,"SHIFT", TO_CHAR("PERFORMANCE", $$999d99$$) AS "PERFORMANCE" from "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = $$2020-01-03$$ AND "FORMULA" = $$553LF-WD PIG FIN1$$ AND "SHIFT" = $$S3$$  ' ).fetchall()
    for d in performance:
        performance = d['PERFORMANCE']

    # print(performance)
    # print(type(performance))
    # perf = float(performance)
    # print(perf)
    # print(type(perf))

    # perfbar = int((perf * 100) / 19)
    # print(perfbar)
    

    test = db.execute('SELECT DISTINCT "FORMULA", TO_CHAR("DATETIME", $$YYYY-MM-DD$$) as "DATETIME","SHIFT","PERFORMANCE", to_char("MOTOR CURRENT"::real, $$9999D99$$) as "MCUR", to_char("STEAM CONSUMPTION"::real, $$999D99$$) as "SCON",to_char("ELECTRIC CONS"::real, $$999.99$$) as "ECON", to_char("%LOAD"::real, $$999D99$$) as "LOAD", "TOTAL_FEED" FROM "PL6_Daily" WHERE "FORMULA" = :formula  AND TO_CHAR("DATETIME", $$YYYY-MM-DD$$) = :ezday  AND "SHIFT" = :shift ' , {"formula": selectformula,"shift":selectshift,"ezday":selectday} ).fetchall()
    for x in test:
        pera = x['PERFORMANCE']
    
    


    db.commit()
    db.close()
    
    return render_template("machine46day.html",maxday=maxday,minday=minday,selectday=selectday,selectformula=selectformula,selectshift=selectshift,formula=formula,shift=shift,performance=performance,test=test)
    return request.form['formulavalue','shiftvalue']

@app.route('/machine46week', methods=["POST", "GET"])
def machine46week():

    startday46=request.form.get("startday46")
    endday46=request.form.get("endday46")
    per46 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday46 AND :endday46 GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday46": startday46, "endday46": endday46}) 
    
    # per = per.first()[0]

    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    
    return render_template("machine46week.html",per46=per46,maxday=maxday,minday=minday)

@app.route('/machine46month', methods=["POST", "GET"])
def machine46month():

    startday46=request.form.get("startday46")
    endday46=request.form.get("endday46")
    per46 = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME", ROUND(AVG("Performance"),2) as "Performance" FROM "PL6_Daily" WHERE "DATETIME" BETWEEN :startday46 AND :endday46 GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC LIMIT 1',{"startday46": startday46, "endday46": endday46}) 
    
    # per = per.first()[0]

    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    
    return render_template("machine46month.html",per46=per46,maxday=maxday,minday=minday)


if __name__ == "__main__":
    app.run(debug=True)

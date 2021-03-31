from flask import Flask, render_template, request
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

    date = db.execute('SELECT "Formula","DateTime" from showall order by "DateTime" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DateTime" from showall order by "DateTime" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "Performance" from showall order by "DateTime" DESC limit 1')

    for row in performance:
        id = row['Performance']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "current" from showall order by "DateTime" DESC limit 1')
    
    for row in current:
        cu = row['current']
        print(cu)

    print(current)


    
    


    return render_template("home.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu)

@app.route('/realtime2')
def realtime2():

    date = db.execute('SELECT "Formula","DateTime" from showall order by "DateTime" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DateTime" from showall order by "DateTime" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "Performance" from showall order by "DateTime" DESC limit 1')

    for row in performance:
        id = row['Performance']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "current" from showall order by "DateTime" DESC limit 1')
    
    for row in current:
        cu = row['current']
        print(cu)

    print(current)
    


    return render_template("realtime2.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu)

@app.route('/realtime3')
def realtime3():

    date = db.execute('SELECT "Formula","DateTime" from showall order by "DateTime" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DateTime" from showall order by "DateTime" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "Performance" from showall order by "DateTime" DESC limit 1')

    for row in performance:
        id = row['Performance']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "current" from showall order by "DateTime" DESC limit 1')
    
    for row in current:
        cu = row['current']
        print(cu)

    print(current)
    


    return render_template("realtime3.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu)

@app.route('/realtime4')
def realtime4():
    
    date = db.execute('SELECT "Formula","DateTime" from showall order by "DateTime" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DateTime" from showall order by "DateTime" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "Performance" from showall order by "DateTime" DESC limit 1')

    for row in performance:
        id = row['Performance']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "current" from showall order by "DateTime" DESC limit 1')
    
    for row in current:
        cu = row['current']
        print(cu)

    print(current)


    return render_template("realtime4.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu)

@app.route('/realtime5')
def realtime5():
    
    date = db.execute('SELECT "Formula","DateTime" from showall order by "DateTime" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DateTime" from showall order by "DateTime" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "Performance" from showall order by "DateTime" DESC limit 1')

    for row in performance:
        id = row['Performance']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "current" from showall order by "DateTime" DESC limit 1')
    
    for row in current:
        cu = row['current']
        print(cu)

    print(current)


    return render_template("realtime5.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu)

@app.route('/realtime6')
def realtime6():
    
    date = db.execute('SELECT "Formula","DateTime" from showall order by "DateTime" DESC limit 1')
    date = date.first()[0]
    print(date)

    time = db.execute('SELECT "DateTime" from showall order by "DateTime" DESC limit 1')
    time = time.first()[0]
    print(time)

    performance = db.execute('SELECT "Performance" from showall order by "DateTime" DESC limit 1')

    for row in performance:
        id = row['Performance']
        print(id)



    # print(performance.fetchall())

    current = db.execute('SELECT "current" from showall order by "DateTime" DESC limit 1')
    
    for row in current:
        cu = row['current']
        print(cu)

    print(current)


    return render_template("realtime6.html",date=date,time=time,per=performance,cur=current,id=id,cu=cu)



@app.route('/test', methods=["POST", "GET"])
def test():

    atday=request.form.get("atday")
    atday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE ("DateTime"::timestamp::date) = :atday GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"atday":atday})
   

    startday=request.form.get("startday")
    endday=request.form.get("endday")
    per = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday AND :endday GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday": startday, "endday": endday}) 
    # per = per.first()[0]

    minday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
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


@app.route('/testday', methods=["POST", "GET"])
def testday():

    # Max and min day limit in calendar
    startday =      request.form.get("startday")
    endday =        request.form.get("endday")

    minday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DATETIME"::timestamp::date) as "DATETIME" FROM "PL6_Daily" GROUP BY date("DATETIME") ORDER BY date("DATETIME") DESC limit 1 ')
    maxday = maxday.first()[0]
    # print(maxday)

    # List formula in drop down list
    formula = db.execute('SELECT DISTINCT "FORMULA" FROM "PL6_Daily"').fetchall()

    # List shift in drop down list
    shift = db.execute('SELECT DISTINCT "SHIFT" FROM "PL6_Daily"').fetchall()
    
    # Show performance after query
    
    selectday =     request.form.get("atday")
    selectformula = request.form.get("formulavalue")
    selectshift =   request.form.get("shiftvalue")

    print("formula : "+selectformula)
    print("shift : "+selectshift)
    print("day : "+selectday)

    performance = db.execute('SELECT DISTINCT "FORMULA" ,"SHIFT", "PERFORMANCE" from "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = $$2020-01-03$$ AND "FORMULA" = $$553LF-WD PIG FIN1$$ AND "SHIFT" = $$S3$$  ' ).fetchall()
    for d in performance:
        performance = d['PERFORMANCE']

    print(performance)


    test = db.execute('SELECT DISTINCT "FORMULA", TO_CHAR("DATETIME", $$YYYY-MM-DD$$) as "DATETIME","SHIFT","PERFORMANCE" FROM "PL6_Daily" WHERE "FORMULA" = :formula AND "SHIFT" = :shift ' , {"formula": selectformula,"shift":selectshift} ).fetchall()
    print(test)
    # perform = db.execute('SELECT DISTINCT "FORMULA", "DATETIME","SHIFT", ("DATETIME"::timestamp::date) as "DateTime", "PERFORMANCE" from "PL6_Daily" WHERE ("DATETIME"::timestamp::date) = :selectday AND "FORMULA" = $$553LF-WD PIG FIN1$$ AND "SHIFT" = $$S3$$  ',{"selectday": selectday, "selectshift": selectshift, "selectformula": selectformula} )
    # print(perform)
    # for p in perform:
    #     performa = p['PERFORMANCE']

    # print(performa)
   
    db.commit()
    db.close()

    return render_template("testday.html",maxday=maxday,minday=minday,formula=formula,shift=shift,performance=performance)
    return request.form['formulavalue','shiftvalue']

@app.route('/testweek', methods=["POST", "GET"])
def testweek():
    
    startweek=request.form.get("startweek")
    endweek=request.form.get("endweek")
    atweek=request.form.get("atweek")

    connection = engine.raw_connection()
    cur = connection.cursor()

    # theweek = cur.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from showall where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) = $$:atweek$$ group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$)',{"atweek": atweek})

    # theweek = cur.fetchone()

    # print(theweek)

    theweek = db.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from showall where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) = TO_CHAR("DateTime" :: DATE, :atweek) group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) ',{"atweek": atweek})
    # theweek = theweek.first()[0]

    # cur.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime", "Formula", ROUND(AVG("Performance"),2) as "Performance", "Status" from showall where "Status" NOT IN ($$Stop$$, $$MinnorStop$$, $$IdleRun$$, $$Startup&Cleanline$$) AND TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) = $$atweek$$ group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$), "Status","Formula" order by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) ',{"atweek": atweek})
    # theweek = cur.fetchall()

    minweek = db.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime" from showall group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) order by "DateTime" ASC limit 1')
    minweek = minweek.first()[0]
    # print(minweek)

    maxweek = db.execute('SELECT TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) as "DateTime" from showall group by TO_CHAR("DateTime" :: DATE, $$YYYY-"W"WW$$) order by "DateTime" DESC limit 1 ')
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
    startday=request.form.get("startday")
    endday=request.form.get("endday")
    per = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday AND :endday GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday": startday, "endday": endday}) 
    # per = per.first()[0]

    minday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday = maxday.first()[0]
    # print(maxday)

    percent=request.form.get("percent")

    db.commit()
    # print(startday) 
    # print(endday)
    # print(per)
    # print(percent)

    
   

    return render_template("testmonth.html",per=per,maxday=maxday,minday=minday,percent=percent)


@app.route('/machine13', methods=["POST", "GET"])
def machine13():

    startday13=request.form.get("startday13")
    endday13=request.form.get("endday13")
    per13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday13 AND :endday13 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday13": startday13, "endday13": endday13}) 
    
    # per = per.first()[0]

    minday13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday13 = minday13.first()[0]
    # print(minday)

    maxday13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday13 = maxday13.first()[0]

    
    return render_template("machine13.html",per13=per13,maxday13=maxday13,minday13=minday13)


@app.route('/machine46', methods=["POST", "GET"])
def machine46():

    startday46=request.form.get("startday46")
    endday46=request.form.get("endday46")
    per46 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday46 AND :endday46 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday46": startday46, "endday46": endday46}) 
    
    # per = per.first()[0]

    minday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday = maxday.first()[0]
    
    return render_template("machine46.html",per46=per46,maxday=maxday,minday=minday)


@app.route('/machine13day', methods=["POST", "GET"])
def machine13day():

    atday=request.form.get("atday")
    atday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE ("DateTime"::timestamp::date) = :atday GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"atday":atday})
    # atdayy = atday
    # for d in atdayy:
    #     atdayy = d['Performance']

    startday=request.form.get("startday")
    endday=request.form.get("endday")
    
    per = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday AND :endday GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday": startday, "endday": endday}) 
    # per = per.first()[0]

    minday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
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
    per13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday13 AND :endday13 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday13": startday13, "endday13": endday13}) 
    
    # per = per.first()[0]

    minday13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday13 = minday13.first()[0]
    # print(minday)

    maxday13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday13 = maxday13.first()[0]

    
    return render_template("machine13week.html",per13=per13,maxday13=maxday13,minday13=minday13)

@app.route('/machine13month', methods=["POST", "GET"])
def machine13month():

    startday13=request.form.get("startday13")
    endday13=request.form.get("endday13")
    per13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday13 AND :endday13 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday13": startday13, "endday13": endday13}) 
    
    # per = per.first()[0]

    minday13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday13 = minday13.first()[0]
    # print(minday)

    maxday13 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday13 = maxday13.first()[0]

    
    return render_template("machine13month.html",per13=per13,maxday13=maxday13,minday13=minday13)

@app.route('/machine46day', methods=["POST", "GET"])
def machine46day():

    startday46=request.form.get("startday46")
    endday46=request.form.get("endday46")
    atday46=request.form.get("atday46")

    atday46 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE ("DateTime"::timestamp::date) = :atday46 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"atday46":atday46})

    per46 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday46 AND :endday46 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday46": startday46, "endday46": endday46}) 
    
    # per = per.first()[0]

    minday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday = maxday.first()[0]
    
    return render_template("machine46day.html",per46=per46,maxday=maxday,minday=minday,atday46=atday46)

@app.route('/machine46week', methods=["POST", "GET"])
def machine46week():

    startday46=request.form.get("startday46")
    endday46=request.form.get("endday46")
    per46 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday46 AND :endday46 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday46": startday46, "endday46": endday46}) 
    
    # per = per.first()[0]

    minday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday = maxday.first()[0]
    
    return render_template("machine46week.html",per46=per46,maxday=maxday,minday=minday)

@app.route('/machine46month', methods=["POST", "GET"])
def machine46month():

    startday46=request.form.get("startday46")
    endday46=request.form.get("endday46")
    per46 = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime", ROUND(AVG("Performance"),2) as "Performance" FROM showall WHERE "DateTime" BETWEEN :startday46 AND :endday46 GROUP BY date("DateTime") ORDER BY date("DateTime") DESC LIMIT 1',{"startday46": startday46, "endday46": endday46}) 
    
    # per = per.first()[0]

    minday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") ASC limit 1 ')
    minday = minday.first()[0]
    # print(minday)

    maxday = db.execute('SELECT ("DateTime"::timestamp::date) as "DateTime" FROM showall GROUP BY date("DateTime") ORDER BY date("DateTime") DESC limit 1 ')
    maxday = maxday.first()[0]
    
    return render_template("machine46month.html",per46=per46,maxday=maxday,minday=minday)


if __name__ == "__main__":
    app.run(debug=True)

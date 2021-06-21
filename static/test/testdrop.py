import psycopg2
from psycopg2 import Error

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

    drop = ''' ALTER TABLE "testdeploy" DROP COLUMN "PL6_Formula_Name", 
    DROP COLUMN "Shift",
    DROP COLUMN "PL6_Job_ID";
    
    '''

    cursor.execute(drop)
    connection.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
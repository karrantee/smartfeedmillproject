from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import operation
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

db= SQLAlchemy(app)
user = 'postgres'
pwd = '12345'
host = '127.0.0.1'
port = '5432'
dbname = 'test'


con = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')


print("Connected to database successfully")




per = pd.read_sql('select "Performance" from showall order by "field1" Desc limit 1;',con)
# per.head()
print(per)


import csv
import pandas as pd
import datetime as dt

#up2date_______________________________________________________
# #date
# current_date = dt.date.today()
# print("\n current date = "+ current_date.strftime('%Y-%m-%d') +" \n")

# #raw
# print("\n raw file \n")
# with open('./static/test/{}.csv'.format(current_date), 'r') as file:
#     csv_reader = csv.reader(file)

#     for line in csv_reader:
#         print(line)

#pandas
# print("\n after changing to dataframe \n")

# df = pd.read_csv('./static/test/{}.csv'.format(current_date), index_col=False) #, names=["Index","Datetime","PL6_Formula_Name","Performance"]

# print(df, "\n")
# print(df.columns, "\n")

#___________________________________________________________________

#raw
print("\n raw file \n")
with open('./static/test/2021-06-14.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for line in csv_reader:
        print(line)


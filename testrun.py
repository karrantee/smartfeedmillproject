import csv
import pandas as pd
import datetime as dt

#date
current_date = dt.date.today()
print("\n current date = "+ current_date.strftime('%Y-%m-%d') +" \n")

#raw
print("\n raw file \n")
with open('./static/test/{}.csv'.format(current_date), 'r') as file:
    csv_reader = csv.reader(file)

    for line in csv_reader:
        print(line)


#pandas
print("\n after changing to dataframe \n")

df = pd.read_csv('./static/test/{}.csv'.format(current_date), index_col=False) #, names=["Index","Datetime","PL6_Formula_Name","Performance"]

print(df, "\n")
print(df.columns, "\n")

#insert to new 
df.to_csv('./static/test/test.csv', columns=['Datetime','PL6_Formula_Name','Performance'] , index=False)

print(df, "\n")
print(df.dtypes)


#remove index
df1 = pd.read_csv('./static/test/test.csv',header=0)
print(df1)


# Write to new file
# with open('./static/test/test.csv', 'r') as file:
#     csv_reader = csv.reader(file)

#     with open('./static/test/test2.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter=',')
#         for line in csv_reader:
#             csv_writer.writerow(line[0:3])
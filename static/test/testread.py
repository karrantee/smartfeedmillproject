import csv

try:
    with open('./test.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

        
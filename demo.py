import psycopg2
import pandas as pd
import tabulate as tb
import csv
import os

fileName = 'test.csv'
hostName = input('Enter host name :')
portNumber = input('Enter port number :')
databaseName = input('Enter database Name :')
userName = input('Enter user name :')
passwordOfDb = input('Enter password :')
tableName = input('Enter table name: ')

connect = None
if os.path.exists(fileName):
    connect = psycopg2.connect(host=hostName, port=portNumber, database=databaseName, user=userName, password=passwordOfDb)
    cursor = connect.cursor()
    sqlSelect = "SELECT * FROM "+tableName
    try:
        cursor.execute(sqlSelect)
        results = cursor.fetchall()
        headers = [i[0] for i in cursor.description]
        print(pd.read_sql(sqlSelect, connect))
        csvFile = csv.writer(open(fileName, 'w', newline=''),
            delimiter=',', lineterminator='\r\n',
            quoting=csv.QUOTE_ALL, escapechar='\\')
        csvFile.writerow(headers)
        for row in results:
            csvFile.writerow(row)
        print("Data export successful.")
    except psycopg2.DatabaseError as e:
        print("Data export unsuccessful.")
        quit()
    finally:
        cursor.close()
        connect.close()
else:
    print("File path does not exist.")
cursor.close()
connect.close()




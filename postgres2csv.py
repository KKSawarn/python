import psycopg2
import pandas as pd
import tabulate as tb
import csv
import os
# File path and name.
fileName = 'test.csv'
# hostName = input('Enter host name :')
# portNumber = input('Enter port number :')
# databaseName = input('Enter database Name :')
# userName = input('Enter user name :')
# passwordOfDb = input('Enter password :')
tableName = input('Enter table name: ')
# Database connection variable.
connect = None

# Check if the file path exists.
if os.path.exists(fileName):

    # try:

        # Connect to database.
    connect = psycopg2.connect(host=" your host", port="5432", database="your db name", user="your user name", password="your password")

    cursor = connect.cursor()
    # SQL to select data from the person table.
    sqlSelect = "SELECT * FROM "+tableName
    try:
        # Execute query.
        cursor.execute(sqlSelect)

        # Fetch the data returned.
        results = cursor.fetchall()
        # Extract the table headers.
        headers = [i[0] for i in cursor.description]

        #Print the results
        print(pd.read_sql(sqlSelect, connect))
        print(tb.tabulate(results, headers=headers, tablefmt='psql', showindex="always", floatfmt=".10f"))

        # Open CSV file for writing.
        csvFile = csv.writer(open(fileName, 'w', newline=''),
            delimiter=',', lineterminator='\r\n',
            quoting=csv.QUOTE_ALL, escapechar='\\')

        # Add the headers and data to the CSV file.
        csvFile.writerow(headers)

        for row in results:
            csvFile.writerow(row)

        # Message stating export successful.
        print("Data export successful.")

        # csvFile.close()

    except psycopg2.DatabaseError as e:

        # Message stating export unsuccessful.
        print("Data export unsuccessful.")
        quit()

    finally:

        # Close database connection.
        cursor.close()
        connect.close()

else:

    # Message stating file path does not exist.
    print("File path does not exist.")


cursor.close()
connect.close()


# import datetime

# date_object = datetime.datetime.today()
# print('date_object.year  ', date_object.year)
# print('date_object.month  ', date_object.month)
# print('date_object.day  ', date_object.day)
# # year = 
# # month =
# # date =
# # datetime_object = datetime.date()
# # date_str= str(datetime_object)
# # # print(datetime_object)
# # print(date_str)
# # date = date_str.split('-')
# # print(date)
# # print(date[1])



import csv
import pymysql
import requests
from itertools import islice

#############################################################################
def print_dob_table():
    try:
        select_table_sql = "SELECT * FROM DOB limit 5;"
        cursor = dob_db.cursor()
        cursor.execute(select_table_sql)
        result = cursor.fetchall()
        print(result)
        return
    except Exception as error:
        print(error)
        return

##############################################################################

## DOWNLOAD CSV  AND WRITE IT TO A LOCAL FILE 
CSV_URL = "https://data.cityofnewyork.us/resource/ic3t-wcy2.csv"
response = requests.get(CSV_URL)
with open('ic3t-wcy2.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))

## CONNECT TO THE DATABASE
dob_db = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'CkCeEd7MP2w0JKHz', db = 'hw2',                     cursorclass = pymysql.cursors.DictCursor)
cursor = dob_db.cursor()

#Delete data from rows in a table 
delete_sql = "DELETE FROM DOB;"
cursor.execute(delete_sql)
dob_db.commit()
print_dob_table()

#Insert into table
insert_sql = """
             INSERT INTO DOB SET Job = %s, 
                                 Doc = %s, 
                                 Borough = %s, 
                                 House = %s, 
                                 StreetName =%s, 
                                 JobType = %s, 
                                 JobStatus = %s, 
                                 JobStatusDescrp = %s, 
                                 LatestActionDate = %s;
             """

## Reading the file
with open('ic3t-wcy2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    count = 0
    next(reader, None) #skips headers
    for row in reader:
        if count >=100:
            break
        else:
            #insert first 100  rows, replace characters
            cursor.execute(insert_sql, (row['"job__"'].replace('"',''), 
                                        row['"doc__"'].replace('"', ''), 
                                        row['"borough"'].replace('"',''),
                                        row['"house__"'].replace('"',''), 
                                        row['"street_name"'].replace('"',''),
                                        row['"job_type"'].replace('"',''),
                                        row['"job_status"'].replace('"',''),
                                        row['"job_status_descrp"'].replace('"',''),
                                        row['"latest_action_date"'].replace('"',''),))
            count = count + 1
dob_db.commit()
print_dob_table()
    
## CLOSE DB CONNECTION
dob_db.close()


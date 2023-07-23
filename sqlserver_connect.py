# Reading data from a SQL-SERVER/Oracle database
import pyodbc as pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'Server=LAPTOP-MOSHUKNL\SQLEXPRESS;' 
                        'UID=sqladmin;'
                        'PWD=test@1234;'
                        'DataBase=master;'
                        'Trusted_Connection=yes')
#print(conn)

# Fetching the data from the selected table using SQL query
cursor=conn.cursor()
cursor.execute('select top 10 [map_id] mapid,\
       [src_dbms_id] sourcedbmsid,\
       [dest_dbms_id] destinationdbmsid,\
       [src_datatype_id] datatype,\
       [src_len_min] lenght FROM [msdb].[dbo].[MSdbms_map]')
for row in cursor:
    print(row)

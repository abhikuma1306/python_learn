# Reading data from a SQL-SERVER/Oracle database
import pyodbc as pyodbc
import pandas as pd

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=LAPTOP-MOSHUKNL\SQLEXPRESS;'
                      'UID=sqladmin;'
                      'PWD=test@1234;'
                      'DataBase=master;'
                      'Trusted_Connection=yes')
# print(conn)

# Fetching the data from the selected table using SQL query
cursor = conn.cursor()
# result= cursor.execute
result = (
    'select top 5 [map_id] mapid,[src_dbms_id] sourcedbmsid,[dest_dbms_id] destinationdbmsid,[src_datatype_id] datatype,[src_len_min] lenght FROM [msdb].[dbo].[MSdbms_map]')

df = pd.read_sql(result, conn)
print(df.head(26))

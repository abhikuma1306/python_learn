# Reading data from a SQL-SERVER/Oracle database


import pyodbc as pyodbc

# Defining the connection string
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'Server=127.0.0.1;' 
                        'UID=sqladmin;'
                        'PWD=test@1234;'
                        'DataBase=master;'
                        'Trusted_Connection=yes')

print(conn)

# Fetching the data from the selected table using SQL query
#RawData= pd.read_sql_query('''select * from [master].[dbo].[MSreplication_options]''', conn)
#RawData.head()

import pyodbc
server = 'localhost'
database = 'SampleDB'
username = 'sa'
password = '123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

class SqlServerHelper:
    @staticmethod
    def Select(sql):
        tsql=sql
        print(tsql)
        cursor.execute(tsql)
        lst=[]
        rows=cursor.fetchall()
        for row in rows:
          lst.append(row)
        for obj in lst:
          print(obj)
        return lst
    def get_cursor(sql):
        return cursor
         

          
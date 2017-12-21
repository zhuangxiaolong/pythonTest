import pyodbc
server = 'localhost'
database = 'SampleDB'
username = 'sa'
password = '123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

class SqlServerHelper:
    def __init__(self,server="localhost", database="SampleDB", uid="sa", pwd="123"):  
        ''''' initialization '''  
        self.server = server  
        self.database = database  
        self.uid = uid  
        self.pwd = pwd 
    #@staticmethod
    def __get_cursor(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+self.server+';PORT=1443;DATABASE='+self.database+';UID='+self.uid+';PWD='+ self.pwd)
        cur = self.conn.cursor()  
        if not cur:  
            raise(NameError,"connected failed!")  
        else:  
            return cur
    def execute4lst(self,sql):
        cursor = self.__get_cursor()
        tsql=sql
        cursor.execute(tsql)
        lst=[]
        rows=cursor.fetchall()
        for row in rows:
          lst.append(row)
        cursor.close()
        self.conn.close()
        return lst
    def execute(self,sql):
        cursor = self.__get_cursor()
        tsql=sql
        cursor.execute(tsql)
        rows=cursor.fetchall()
        cursor.close()
        self.conn.close()
        return rows
    def executeNoQuery(self,sql):
        cnxn=self.__get_conn()
        cursor = cnxn.cursor()
        tsql=sql
        #print(tsql)
        cursor.execute(tsql)
        self.conn.commit()
        cursor.Close()
        self.conn.Close()
    def insert(self,sql,args):
        cursor=self.__get_cursor()
        tsql=sql
        #print(tsql)
        cursor.execute(tsql,args)
        self.conn.commit()
        cursor.close()
        self.conn.close()
         

          
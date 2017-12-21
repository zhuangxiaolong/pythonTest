import pyodbc
server = 'localhost'
database = 'SampleDB'
username = 'sa'
password = '123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
with cursor.execute(tsql,'colin','china'):
    print ('Successfuly Inserted!')


#Update Query
print ('Updating Location for Nikita')
tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
with cursor.execute(tsql,'Sweden','Nikita'):
    print ('Successfuly Updated!')


#Delete Query
print ('Deleting user Jared')
tsql = "DELETE FROM Employees WHERE Name = ?"
with cursor.execute(tsql,'Jared'):
    print ('Successfuly Deleted!')

tsql="select * from employees"
cursor.execute(tsql)
#while 1:
#  row=cursor.fetchone()
#  if not row:
#    break
# print(row)

rows=cursor.fetchall()
#for row in rows:
#  print(row)
    
lst=[]
for row in rows:
    lst.append(row)

for obj in lst:
   print(obj)


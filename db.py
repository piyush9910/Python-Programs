"""
1 Start Python
2 Import Libraries
3 Create a Database
4 Open and connect to database
5 Create a Cursosr object
6 Execute a query
7 Extract Data result
8 Close the database
"""
"""# Show Tables of MYSQL Using Database Connectivity.
import mysql.connector as sql
mydb=sql.connect(host="localhost", user="root", passwd="1234", database="School")
mycursor=mydb.cursor()
adm=int(input("Admission No : "))
roll=int(input("Roll Number: "))
name=input("Name : ")
city=input("City : ")
clas=int(input("Class : "))
Str=input("Stream : ")
gen=input("Gender : ")
mycursor.execute("INSERT INTO STUDENT_INFO VALUES({}, {}, '{}', '{}', {}, '{}', '{}')".format(adm,roll,name,city,clas,Str, gen))
mydb.commit()
print("Data Succesfully Recorded...")"""

import mysql.connector as sql
mydb=sql.connect(host="localhost", user="root", passwd="1234", database="School")
mycursor=mydb.cursor()
mycursor.execute("Select * from Student_Info")
for i in mycursor:
    print(i)
mydb.close()
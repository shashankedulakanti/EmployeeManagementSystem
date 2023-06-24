import mysql.connector

# making Connection
con = mysql.connector.connect(host="localhost", user="root", password="root")

cur = con.cursor()

# creating database name with empd
sql1 = "create database emp"
cur.execute(sql1)

# using database  emp
sq12 = "use emp"
cur.execute(sq12)

# table query
sql3 = "create table empd(id int,name varchar(20),post varchar(50),salary int)"
cur.execute(sql3)

con.commit()


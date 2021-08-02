import mysql.connector
from mysql.connector.errors import DatabaseError

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Adminpass123#",
  database="ip_data"
)


def ipv4_a():
  var1 = input("col: ")

  mycursor = mydb.cursor()

  mycursor.execute("SELECT {} FROM ipv4_class_a".format(var1))

  results = mycursor.fetchone()

  for x in results:
    print(x)
import mysql.connector
database = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = 'root'
)
cusrdorob = database.cursor()

cusrdorob.execute("CREATE DATABASE elderco")

print("Done")
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="fuqianshan",#input your username here
    passwd="KRPCGroup"#also, your passwd here
)

print(mydb)
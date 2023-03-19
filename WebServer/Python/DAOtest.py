import mysql.connector


mydb = mysql.connector.connect(
    host = 'fuqianshan.asuscomm.com',
    user = 'fuqianshan',
    password = 'KRPCGroup',
    database = 'smartbin'
)

print(mydb)
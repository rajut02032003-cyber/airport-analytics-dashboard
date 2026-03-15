import pymysql

def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Raju@1234",
        database="aerodata"
    )
    return connection
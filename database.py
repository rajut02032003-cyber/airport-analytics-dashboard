# database connection file
import pymysql
def get_db_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="aero_data"
    )
    return conn
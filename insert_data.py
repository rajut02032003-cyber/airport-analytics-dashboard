import pandas as pd
from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

def insert_airport(data):

    sql = """
    INSERT INTO airport
    (iata_code,name,city,country,timezone)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(sql,(
        data["iata"],
        data["name"],
        data["municipalityName"],
        data["countryCode"],
        data["timeZone"]
    ))

    conn.commit()
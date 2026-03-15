import streamlit as st
import pandas as pd

from python_project_01.db_connection import get_connection

#from python_project_01.db_connection import get_connection

#from python_project_01.db_connection import get_connection
df = pd.read_csv("flight.csv")
#from db_connection import get_connection

st.title("🔍 Flight Search")

conn = get_connection()

flight_number = st.text_input("Enter Flight Number")

query = "SELECT * FROM flight"

if flight_number:
    query += f" WHERE flight_number='{flight_number}'"

data = pd.read_sql(query, conn)

st.dataframe(data)
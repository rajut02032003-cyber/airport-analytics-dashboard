import streamlit as st
import pandas as pd
from db_connection import get_connection

st.title("🏢 Airport Details")

conn = get_connection()

airports = pd.read_sql("SELECT name FROM airport", conn)

airport = st.selectbox("Select Airport", airports)

query = f"""
SELECT * FROM airport
WHERE name='{airport}'
"""

data = pd.read_sql(query, conn)

st.dataframe(data)
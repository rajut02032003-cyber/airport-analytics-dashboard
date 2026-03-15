import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.title("🏆 Route Leaderboard")

# database connection
conn = get_connection()

# fetch flight data
query = """
SELECT flight_number, airport, type, status, aircraft
FROM flight
"""

df = pd.read_sql(query, conn)

st.subheader("Flight Data")

st.dataframe(df)

# -----------------------------
# Busiest Airports
# -----------------------------

airport_count = df.groupby("airport").size().reset_index(name="total_flights")

st.subheader("✈️ Busiest Airports")

fig = px.bar(
    airport_count.sort_values("total_flights", ascending=False).head(10),
    x="airport",
    y="total_flights",
    title="Top 10 Busiest Airports"
)

st.plotly_chart(fig)

# -----------------------------
# Aircraft Usage
# -----------------------------

st.subheader("🛫 Aircraft Usage")

aircraft_count = df["aircraft"].value_counts().reset_index()
aircraft_count.columns = ["aircraft", "count"]

fig2 = px.pie(
    aircraft_count,
    names="aircraft",
    values="count",
    title="Aircraft Distribution"
)

st.plotly_chart(fig2)

# -----------------------------
# Flight Status Analysis
# -----------------------------

st.subheader("📊 Flight Status Distribution")

status_count = df["status"].value_counts().reset_index()
status_count.columns = ["status", "count"]

fig3 = px.bar(
    status_count,
    x="status",
    y="count",
    title="Flight Status Distribution"
)

st.plotly_chart(fig3)
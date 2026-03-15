import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.title("⏱ Airport Delay Analysis")

# connect database
conn = get_connection()

# fetch data
query = """
SELECT airport_iata, total_flights, delayed_flights
FROM airport_delay
"""

df = pd.read_sql(query, conn)

# calculate delay percentage
df["delay_percentage"] = (df["delayed_flights"] / df["total_flights"]) * 100

st.subheader("Airport Delay Data")

st.dataframe(df)

# bar chart
fig = px.bar(
    df,
    x="airport_iata",
    y="delay_percentage",
    title="Delay Percentage by Airport",
    labels={
        "airport_iata": "Airport",
        "delay_percentage": "Delay %"
    }
)

st.plotly_chart(fig)

# leaderboard
st.subheader("Most Delayed Airports")

top_delay = df.sort_values(by="delay_percentage", ascending=False).head(10)

st.dataframe(top_delay)
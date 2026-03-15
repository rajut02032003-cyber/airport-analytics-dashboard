'''import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.set_page_config(page_title="Airport Analytics Dashboard", layout="wide")

st.title("✈️ Airport and Flight Analytics Dashboard")

import streamlit as st
import pandas as pd
from db_connection import get_connection

st.title("✈️ Airport Analytics Dashboard")

conn = get_connection()

# Summary statistics
total_airports = pd.read_sql("SELECT COUNT(*) as total FROM airport", conn)
total_flights = pd.read_sql("SELECT COUNT(*) as total FROM flight", conn)

st.subheader("Summary Statistics")

col1, col2 = st.columns(2)

col1.metric("Total Airports", total_airports["total"][0])
col2.metric("Total Flights", total_flights["total"][0])

st.subheader("Go to Pages")

st.page_link("pages/flight_search.py", label="🔍 Flight Search")
st.page_link("pages/airport_details.py", label="🏢 Airport Details")
st.page_link("pages/delay_analysis.py", label="⏱ Delay Analysis")
st.page_link("pages/route_leaderboard.py", label="🏆 Route Leaderboard")'''

import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.set_page_config(page_title="Airport Analytics Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Flight Search", "Airport Details", "Delay Analysis", "Route Leaderboard"]
)

conn = get_connection()

# ---------------- HOME PAGE ----------------
if page == "Home":

    st.title("✈ Airport Analytics Dashboard")
    st.write("Welcome to the Flight Analytics System")

# ---------------- FLIGHT SEARCH ----------------
elif page == "Flight Search":

    st.title("🔍 Flight Search")

    flight_number = st.text_input("Enter Flight Number")

    query = "SELECT * FROM flight"

    if flight_number:
        query += f" WHERE flight_number='{flight_number}'"

    df = pd.read_sql(query, conn)

    st.dataframe(df)

# ---------------- AIRPORT DETAILS ----------------
elif page == "Airport Details":

    st.title("🏢 Airport Details")

    query = "SELECT * FROM airport"

    df = pd.read_sql(query, conn)

    st.dataframe(df)

# ---------------- DELAY ANALYSIS ----------------
elif page == "Delay Analysis":

    st.title("⏱ Delay Analysis")

    query = """
    SELECT airport_iata, total_flights, delayed_flights
    FROM airport_delays
    """

    df = pd.read_sql(query, conn)

    df["delay_percentage"] = (df["delayed_flights"] / df["total_flights"]) * 100

    st.dataframe(df)

    fig = px.bar(
        df,
        x="airport_iata",
        y="delay_percentage",
        title="Delay Percentage by Airport"
    )

    st.plotly_chart(fig)

# ---------------- ROUTE LEADERBOARD ----------------
elif page == "Route Leaderboard":

    st.title("🏆 Route Leaderboard")

    query = """
    SELECT flight_number, airport, type, status, aircraft
    FROM flight
    """

    df = pd.read_sql(query, conn)

    st.subheader("Flight Data")

    st.dataframe(df)

    busiest = df.groupby("airport").size().reset_index(name="total_flights")

    st.subheader("Top Busiest Airports")

    st.bar_chart(busiest.set_index("airport"))


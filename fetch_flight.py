import requests
import pandas as pd
from datetime import datetime, timedelta

API_HOST = "aerodatabox.p.rapidapi.com"
API_KEY = "75a00d105cmsh84dc899642b1224p144b59jsn5a839a34876b"

headers = {
    "x-rapidapi-key": "75a00d105cmsh84dc899642b1224p144b59jsn5a839a34876b",
    "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
}

airport_codes = [
"DEL","BOM","BLR","HYD","MAA",
"CCU","DXB","LHR","JFK","SIN"
]

# Dynamic time (current UTC time)
start_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M")
end_time = (datetime.utcnow() + timedelta(hours=12)).strftime("%Y-%m-%dT%H:%M")

flight_list = []

for code in airport_codes:

    print("\nFetching flights for:", code)

    url = f"https://{API_HOST}/flights/airports/iata/{code}/{start_time}/{end_time}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("API error:", response.status_code)
        continue

    data = response.json()

    departures = data.get("departures", [])
    arrivals = data.get("arrivals", [])

    print("Departures:", len(departures))
    print("Arrivals:", len(arrivals))

    for flight in departures:
        flight_list.append({
            "flight_number": flight.get("number"),
            "airport": code,
            "type": "Departure",
            "status": flight.get("status"),
            "aircraft": flight.get("aircraft", {}).get("reg")
        })

    for flight in arrivals:
        flight_list.append({
            "flight_number": flight.get("number"),
            "airport": code,
            "type": "Arrival",
            "status": flight.get("status"),
            "aircraft": flight.get("aircraft", {}).get("reg")
        })

df = pd.DataFrame(flight_list)
df.to_csv("flights.csv", index=False)

print("\nflights.csv created successfully")
import requests
import pandas as pd

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

start_time = "2026-03-11T00:00"
end_time = "2026-03-11T12:00"

aircraft_list = []

for code in airport_codes:

    print("\nFetching flights for:", code)

    url = f"https://{API_HOST}/flights/airports/iata/{code}/{start_time}/{end_time}"

    response = requests.get(url, headers=headers)
    data = response.json()

    departures = data.get("departures", [])

    for flight in departures:

        aircraft = flight.get("aircraft", {})

        aircraft_list.append({
            "airport": code,
            "flight_number": flight.get("number"),
            "aircraft_model": aircraft.get("model"),
            "aircraft_reg": aircraft.get("reg")
        })

# Convert to dataframe
df = pd.DataFrame(aircraft_list)

# Save file
df.to_csv("fetch_aircraft.csv", index=False)

print("\nfetch_aircraft.csv created successfully")
print("Total records saved:", len(df))
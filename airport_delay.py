import requests
import pandas as pd

API_HOST = "aerodatabox.p.rapidapi.com"
API_KEY = "75a00d105cmsh84dc899642b1224p144b59jsn5a839a34876b"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}

airport_codes = [
"DEL","BOM","BLR","HYD","MAA",
"CCU","DXB","LHR","JFK","SIN"
]

start_time = "2026-03-11T00:00"
end_time = "2026-03-11T12:00"

delay_data = []

for code in airport_codes:

    print("\nAirport:", code)

    url = f"https://{API_HOST}/flights/airports/iata/{code}/{start_time}/{end_time}"

    response = requests.get(url, headers=headers)

    data = response.json()

    departures = data.get("departures", [])

    delayed_flights = 0

    for flight in departures:

        status = flight.get("status")

        if status == "Delayed":
            delayed_flights += 1

    total_flights = len(departures)

    print("Total Flights:", total_flights)
    print("Delayed Flights:", delayed_flights)

    delay_data.append({
        "airport_code": code,
        "total_flights": total_flights,
        "delayed_flights": delayed_flights
    })

# Convert to dataframe
df = pd.DataFrame(delay_data)

# Save to CSV
df.to_csv("airport_delay.csv", index=False)

print("\nFile airport_delay.csv created successfully!")
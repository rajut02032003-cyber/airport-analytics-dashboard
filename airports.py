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

airport_list = []

for code in airport_codes:

    url = f"https://{API_HOST}/airports/iata/{code}"

    response = requests.get(url, headers=headers)

    data = response.json()

    airport_info = {
        "iata_code": data.get("iata", code),
        "name": data.get("shortName", "Unknown"),
        "city": data.get("municipalityName", "Unknown"),
        "country": data.get("countryCode", "Unknown"),
        "timezone": data.get("timeZone", "Unknown")
    }

    airport_list.append(airport_info)

# Convert to dataframe
df = pd.DataFrame(airport_list)

# Save CSV file
df.to_csv("airports.csv", index=False)

print("airports.csv file created successfully")
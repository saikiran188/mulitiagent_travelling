import requests
from api_keys.config import SKRAPIDAPI_KEY, SKRAPIDAPI_HOST

def get_transport_options(from_city: str, to_city: str, limit: int = 5) -> str:
    url = "https://skyscanner44.p.rapidapi.com/search"

    querystring = {
        "adults": "1",
        "origin": from_city,
        "destination": to_city,
        "departureDate": "2025-06-10",
        "currency": "USD"
    }

    headers = {
        "X-RapidAPI-Key": SKRAPIDAPI_KEY,
        "X-RapidAPI-Host": SKRAPIDAPI_HOST
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        flights = data.get("data", {}).get("flights", [])
        if not flights:
            return "❌ No transport options found."

        results = ""
        for flight in flights[:limit]:
            carrier = flight.get("carrier", "Unknown")
            price = flight.get("price", {}).get("raw", "N/A")
            from_code = flight.get("origin")
            to_code = flight.get("destination")
            dep_time = flight.get("departureTime")
            results += f"✈️ {carrier} | {from_code} → {to_code}\n🕒 {dep_time} | 💰 ${price}\n\n"

        return results.strip()

    except Exception as e:
        return f"❌ Error fetching transport info: {str(e)}"

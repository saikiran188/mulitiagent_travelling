import requests
from api_keys.config import GOOGLE_MAPS_API_KEY

def get_attractions(location: str, limit: int = 5) -> str:
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"top attractions in {location}",
        "key": GOOGLE_MAPS_API_KEY
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("status") != "OK":
            return f"❌ No attractions found for {location}."

        results = ""
        for place in data["results"][:limit]:
            name = place.get("name")
            address = place.get("formatted_address")
            rating = place.get("rating")
            results += f"🏞️ {name}\n⭐ Rating: {rating} | 📍 {address}\n\n"

        return results if results else "No attractions found."

    except Exception as e:
        return f"❌ Error fetching attractions: {str(e)}"

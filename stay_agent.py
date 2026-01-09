import requests
from api_keys.config import RAPIDAPI_KEY, RAPIDAPI_HOST

def get_stays(location: str, limit: int = 5) -> str:
    url = "https://hotels-com-provider.p.rapidapi.com/v2/hotels/search"
    
    querystring = {
        "region_id": location,
        "adults_number": "1",
        "checkin_date": "2025-06-10",
        "checkout_date": "2025-06-12",
        "locale": "en_US",
        "currency": "USD",
        "sort_order": "REVIEW",
        "guest_rating_min": "3.5",
        "page_number": "1",
        "page_size": str(limit)
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if "properties" not in data:
            return "❌ No hotels found."

        results = ""
        for hotel in data["properties"][:limit]:
            name = hotel.get("name")
            rating = hotel.get("guestReviews", {}).get("rating")
            price = hotel.get("price", {}).get("lead", {}).get("formatted")
            address = hotel.get("address", {}).get("streetAddress")
            results += f"🏨 {name}\n⭐ Rating: {rating} | 💰 Price: {price}\n📍 {address}\n\n"

        return results if results else "No results found."

    except Exception as e:
        return f"❌ Error fetching hotel data: {str(e)}"

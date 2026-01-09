from api_keys.config import GOOGLE_MAPS_API_KEY

def generate_map_url(location: str) -> str:
    base_url = "https://www.google.com/maps/embed/v1/place"
    map_url = f"{base_url}?key={GOOGLE_MAPS_API_KEY}&q={location.replace(' ', '+')}"
    return map_url

import openai
from api_keys.config import OPENAI_API_KEY, OPENAI_API_BASE
from agents.weather_agent import get_weather
from agents.map_agent import generate_map_url
from agents.stay_agent import get_stays
from agents.transport_agent import get_transport_options
from agents.attraction_agent import get_attractions

openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_API_BASE

def route_query(query: str, user_from_city="Mumbai") -> str:
    system_prompt = """
You are a smart router for a travel assistant AI. Your job is to classify the user's intent into one of the following categories:

1. weather
2. map
3. accommodation
4. transport
5. attractions

Return ONLY the category name in lowercase. Do NOT explain.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4o"
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
        )
        intent = response['choices'][0]['message']['content'].strip().lower()
        
        # Route to appropriate agent
        if intent == "weather":
            return get_weather(query)
        elif intent == "map":
            return generate_map_url(query)
        elif intent == "accommodation":
            return get_stays(query)
        elif intent == "transport":
            return get_transport_options(user_from_city, query)
        elif intent == "attractions":
            return get_attractions(query)
        else:
            return "🤖 Sorry, I couldn't understand your request."

    except Exception as e:
        return f"❌ Router error: {str(e)}"

import streamlit as st
from agents.weather_agent import get_weather
from agents.map_agent import generate_map_url
from agents.stay_agent import get_stays
from agents.transport_agent import get_transport_options
from agents.attraction_agent import get_attractions
from orchestrator.router_agent import route_query

st.set_page_config(page_title="🌍 Agentic AI Travel Assistant", layout="centered")
st.title("🌍 Agentic AI Travel Assistant")

st.markdown(
    """
Welcome to your smart travel companion powered by **Agentic AI**!  
Ask anything like:
- `"What’s the weather in Shimla?"`
- `"Show me hotels in Manali"`
- `"I want to see a map of Delhi"`
- `"How can I go from Mumbai to Jaipur?"`
- `"Top attractions in Paris"`
"""
)

query = st.text_input("📝 Ask your travel question here:", placeholder="e.g., Show me hotels in Goa")
user_from_city = st.text_input("📍 Your departure city (used for transport):", "Mumbai")

if st.button("✨ Get Info"):
    if query:
        with st.spinner("Thinking..."):
            result = route_query(query, user_from_city)

            if result.startswith("https://www.google.com/maps"):
                st.subheader("🗺 Map")
                st.components.v1.iframe(result, width=700, height=450)
            else:
                st.subheader("📍 Response")
                st.info(result)
    else:
        st.warning("Please enter a query above to continue.")

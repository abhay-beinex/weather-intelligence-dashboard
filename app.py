import streamlit as st
import pandas as pd
import plotly.express as px

from utils.geocoding import get_coordinates
from utils.weather import get_weather
from utils.country import get_country_info


st.set_page_config(
    page_title="Weather Dashboard",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------

st.title("🌦 Weather Intelligence Dashboard")

st.markdown("""
Monitor live weather conditions across multiple cities
using real-time public REST APIs.
""")

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("Dashboard Info")

st.sidebar.markdown("""
### Features
- Multi-city weather monitoring
- 7-day forecast
- Country enrichment
- Error handling
- Real-time API data
""")

# -------------------------------
# User Input
# -------------------------------

st.info(
    "Enter up to 5 cities separated by commas.\n"
    "Example: Kochi, Delhi, Madrid"
)

city_input = st.text_input(
    "",
    "Kochi, Dubai"
)

# -------------------------------
# Locality Mapping
# -------------------------------

fallback_cities = {
    "edappally": "Kochi",
    "kakkanad": "Kochi",
    "aluva": "Kochi"
}

# -------------------------------
# Main Dashboard Logic
# -------------------------------

if city_input:

    with st.spinner("Fetching weather data..."):

        cities = [
            city.strip()
            for city in city_input.split(",")
        ][:5]

        cols = st.columns(len(cities))

        for idx, city in enumerate(cities):

            original_city = city

            # Locality normalization
            if city.lower() in fallback_cities:

                st.info(
                    f"{city} mapped to nearby city: "
                    f"{fallback_cities[city.lower()]}"
                )

                city = fallback_cities[city.lower()]

            # Get coordinates
            location = get_coordinates(city)

            if not location:
                st.error(
                    f"Could not find city: {original_city}"
                )
                continue

            # Get weather
            weather = get_weather(
                location["latitude"],
                location["longitude"]
            )

            if not weather:
                st.error(
                    f"Could not fetch weather data "
                    f"for {original_city}"
                )
                continue

            # Get country info
            country = get_country_info(
                location["country"]
            )

            if not country:
                st.error(
                    f"Could not fetch country data "
                    f"for {location['country']}"
                )
                continue

            current = weather["current"]

            # -------------------------------
            # Weather Cards
            # -------------------------------

            with cols[idx]:

                st.subheader(location["city"])

                st.image(
                    country["flag"],
                    width=80
                )

                st.metric(
                    "Temperature",
                    f"{current['temperature_2m']} °C"
                )

                st.metric(
                    "Wind Speed",
                    f"{current['wind_speed_10m']} km/h"
                )

                st.metric(
                    "Humidity",
                    f"{current['relative_humidity_2m']}%"
                )

                st.write(
                    "Timezone:",
                    country["timezone"]
                )

                st.write(
                    "Currency:",
                    country["currency"]
                )

            # -------------------------------
            # Forecast Chart
            # -------------------------------

            daily = weather["daily"]

            df = pd.DataFrame({
                "Date": daily["time"],
                "Max Temp": daily["temperature_2m_max"],
                "Min Temp": daily["temperature_2m_min"]
            })

            fig = px.line(
                df,
                x="Date",
                y=["Max Temp", "Min Temp"],
                markers=True,
                title=f"7-Day Forecast - {location['city']}"
            )

            st.plotly_chart(
                fig,
                width="stretch",
                key=f"chart_{idx}_{city}"
            )

# -------------------------------
# Footer
# -------------------------------

st.caption(
    "Built with Streamlit, Open-Meteo API, "
    "and REST Countries API"
)
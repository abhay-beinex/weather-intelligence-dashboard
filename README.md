# 🌦 Weather Intelligence Dashboard

A multi-city weather monitoring dashboard built using Python and Streamlit.

This project integrates multiple public REST APIs to provide:

- Current weather conditions
- 7-day weather forecasts
- Country information enrichment
- Multi-city monitoring dashboard

---

# Features

- Search and monitor up to 5 cities
- Current temperature, wind speed, and humidity
- 7-day forecast visualization
- Country information:
  - Flag
  - Timezone
  - Currency
- Error handling for invalid cities
- Locality normalization for unsupported areas
- Interactive dashboard using Streamlit

---

# APIs Used

## 1. Open-Meteo Forecast API

Provides:
- Current weather
- Daily forecast

Endpoint:
https://api.open-meteo.com/v1/forecast

Documentation:
https://open-meteo.com/en/docs

---

## 2. Open-Meteo Geocoding API

Converts city names into:
- Latitude
- Longitude

Endpoint:
https://geocoding-api.open-meteo.com/v1/search

Documentation:
https://open-meteo.com/en/docs/geocoding-api

---

## 3. REST Countries API

Provides:
- Country flags
- Timezones
- Currency information

Endpoint:
https://restcountries.com/v3.1/name/{country}

Documentation:
https://restcountries.com

---

# Libraries Used

- streamlit
- requests
- pandas
- plotly

---

# Project Structure

weather-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
└── utils/
    ├── geocoding.py
    ├── weather.py
    └── country.py

---

# Challenges Faced

- Handling ambiguous city names returned by geocoding APIs
- Managing API failures gracefully
- Preventing duplicate Streamlit chart keys
- Supporting localities not directly recognized by APIs

---

# Example Locality Handling

Some localities such as:

- Edappally
- Kakkanad
- Aluva

are normalized to nearby major cities to improve API compatibility.

Example:

Edappally → Kochi

---




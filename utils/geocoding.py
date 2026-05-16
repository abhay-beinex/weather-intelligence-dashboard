import requests

def get_coordinates(city):

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search?"
        f"name={city}&count=10"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if "results" not in data:
        return None

    results = data["results"]

    city_lower = city.lower()

    # Exact name matches
    exact_matches = [
        item for item in results
        if item["name"].lower() == city_lower
    ]

    if exact_matches:

        # Sort by population if available
        exact_matches.sort(
            key=lambda x: x.get("population", 0),
            reverse=True
        )

        result = exact_matches[0]

    else:
        result = results[0]

    return {
        "city": result["name"],
        "country": result["country"],
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }
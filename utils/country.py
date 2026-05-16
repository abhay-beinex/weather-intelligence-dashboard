import requests

def get_country_info(country):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data_list = response.json()

    if not data_list:
        return None

    data = data_list[0]

    currency = list(data["currencies"].keys())[0]

    return {
        "flag": data["flags"]["png"],
        "timezone": data["timezones"][0],
        "currency": currency
    }
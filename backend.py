import requests

API_KEY = "9dc64eedf51a2888e5b8c79757c3902f"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "list" not in data:
        print(f"Error: 'list' key not found in response. Data received: {data}")
        return None

    filtered_data = data["list"]
    nr_values = min(8 * forecast_days, len(filtered_data))  # Prevent over-slicing
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Delhi", forecast_days=3))

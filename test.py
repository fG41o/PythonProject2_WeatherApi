import pandas as pd
import requests


# Function to get location key from AccuWeather API from user input
def get_location_key(city: str) -> int:
    api_key = '4nyShYGdfmuAcVsHg2CuyxYbvXDmMFNW'  # Replace with your AccuWeather API key
    url = f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        data = response.json()
        if data:
            return data[0]['Key']  # Return the first location key
        else:
            print("No data found for the specified city.")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Print general request error
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any other exception
    return None


# Function to get weather data from AccuWeather API using location key
def get_weather(location_key: int) -> dict[str]:
    api_key = '4nyShYGdfmuAcVsHg2CuyxYbvXDmMFNW'
    url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&language=en-us' \
          f'&details=true&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        data = response.json()
        if data:
            weather_info = {
                'temperature': data[0]['Temperature']['Metric']['Value'],  # Temperature in Celsius
                'humidity': data[0]['RelativeHumidity'],  # Humidity percentage
                'wind_speed': data[0]['Wind']['Speed']['Metric']['Value'],  # Wind speed in m/s
                'weather_text': data[0]['WeatherText'],  # Weather description
                'precipitation_value': data[0].get('PrecipitationSummary', {}).get('Precipitation', {}).get('Metric',
                                                                                                            {}).get(
                    'Value', 0)  # Precipitation value in mm
            }
            return weather_info
        else:
            print("No weather data found.")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Print general request error
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any other exception
    return None


# function for deciding if weather is good
def check_bad_weather(weather_data: dict[str]) -> bool:
    go_away = False
    if weather_data['temperature'] > 35 or weather_data['temperature'] < 0 or weather_data['wind_speed'] > 50 or \
            weather_data['precipitation_value'] > 2:
        go_away = True
    return go_away


Key_testing_df = pd.DataFrame({
    'CityName': ['Berlin', 'Tokyo', 'AFJOSFJKAOSF', "-34.4415900 -58.7086067"],
    'ExpectedKey': [178087, 226396, None, None],  # Key value for corresponding city name from AccuWeather documentation
    'OutputKey': [0, 0, 0, 0],  # Key value that tested function outputs

})

weather_info_1 = {
    'temperature': 35,  # Temperature in Celsius
    'humidity': 50,  # Humidity percentage
    'wind_speed': 200,  # Wind speed in m/s
    'weather_text': " ",  # Weather description
    'precipitation_value': 2  # Precipitation value in mm
}

weather_info_2 = {
    'temperature': 20,  # Temperature in Celsius
    'humidity': 25,  # Humidity percentage
    'wind_speed': 10,  # Wind speed in m/s
    'weather_text': " ",  # Weather description
    'precipitation_value': 0  # Precipitation value in mm
}

Weather_testing_df = pd.DataFrame({
    'WeatherData': [weather_info_1, weather_info_2],
    'ExpectedAns': [True, False],  # expected bool value, showing weather is bad
    'OutputAns': [False, False],  # bool value, showing weather is good, that tested function outputs

})

Weather_testing_df['OutputAns'] = Weather_testing_df['WeatherData'].apply(check_bad_weather)
Key_testing_df['OutputKey'] = Key_testing_df['CityName'].apply(get_location_key)

# Display results for verification
print(Weather_testing_df[['ExpectedAns', 'OutputAns']])
print(Key_testing_df[['CityName','ExpectedKey', 'OutputKey']])

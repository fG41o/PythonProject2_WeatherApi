# PythonProject2_WeatherApi

# Weather App

## Overview

This web application retrieves current weather conditions for specified cities using the AccuWeather API. It provides users with temperature, humidity, wind speed, and precipitation information.

## Error Handling

The application includes comprehensive error handling to ensure a smooth user experience. Below are the types of errors handled:

1. **City Not Found**: 
   - If a user inputs an invalid city name, the application responds with a message: 
     - "Could not find one or both cities."

2. **API Request Errors**: 
   - If there are issues connecting to the AccuWeather API (e.g., network issues or server downtime), the application will display an appropriate message indicating that it could not retrieve weather data.

3. **HTTP Errors**: 
   - The application checks for HTTP errors (like 404 or 500) and informs users that there was an issue retrieving data.

4. **Unexpected Errors**: 
   - Any unexpected exceptions during execution are caught and logged, providing feedback to users without crashing the application.

## Testing Scenarios

- **Valid City Names**: Test with known city names to ensure accurate weather retrieval.
- **Invalid City Names**: Input incorrect names to verify that proper error messages are displayed.
- **Differenet Weather Conditions**: Testong logic of function by inputing different weather conditions
- **Network Issues**: Disconnect from the internet and observe how the application handles connectivity problems.



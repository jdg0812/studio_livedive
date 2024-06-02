from requests import get
import numpy as np
import envVariable

API_KEY = envVariable.api_key
MAX_SCORE = 100
MIN_SCORE = 0

TEMP_SHIFT = 273.15 + 25 
SHIFT_VECTOR = np.array([-TEMP_SHIFT, 0, 0, 0, 0])
COEFFICIENT_VECTOR = np.array([1.1, -2, -0.75, -1, 0])

def get_input_vector(latitude: float, longitude: float, 
                     report: bool = False) -> np.array:
    
    # API link for CURRENT weather data
    current_api_link = (
        'https://api.openweathermap.org/data/2.5/onecall?'
        f'lat={latitude}&lon={longitude}'
        f'&exclude=hourly,daily,minutely&appid={API_KEY}'
    )

    current_response = get(current_api_link)
    curr_response_data = current_response.json()['current']
    # print(response.json())
    
    if report:
        print(curr_response_data)
    
    # temp, uvi, clouds, wind_speed, weatherid
    return np.array([max(curr_response_data['temp'], TEMP_SHIFT),
            curr_response_data['uvi'], curr_response_data['clouds'], 
            curr_response_data['wind_speed'], 
            curr_response_data['weather'][0]['id']]) + SHIFT_VECTOR

def get_score(input_vector: np.array) -> int:
    score = 100 + np.dot(COEFFICIENT_VECTOR, input_vector)
    
    weather_category = int(str(input_vector[-1])[0])
    weather_intensity = int(str(input_vector[-1])[-1])
    
    if weather_category == 8:
        weather_adjustment = 0 # clear or cloudy, cloudy taken into account
    elif weather_category in [2, 6, 7]: 
        weather_adjustment = 100 # snow, thunderstorm, atmosphere
    elif weather_category in [3, 5]: # intensity based
        weather_adjustment = 3 * max(weather_intensity, 1) * weather_category
    else:
        weather_adjustment = 0
        
    weather_adjusted_score = score - weather_adjustment
    return int(max(min(weather_adjusted_score, MAX_SCORE), MIN_SCORE))

def score_calculator(lat: float, long : float) -> int:
    input_vector = get_input_vector(lat, long)
    return get_score(input_vector)

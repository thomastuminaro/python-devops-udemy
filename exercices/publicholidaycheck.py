import requests
from datetime import date

def is_today_a_public_holiday(country_code: str) -> bool:
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a string")
    if not country_code:
        raise ValueError("country_code must be set.")
    
    endpoint = "https://api.example.com/v1/holidays"
    current_date = str(date.today())
    params = {
        'country': country_code,
        'year': current_date.split("-")[0]
    }
    
    response = requests.get(endpoint, params=params, timeout=10)
    for holiday in response:
        if holiday.get("date", "") == current_date:
            return True
    return False
    

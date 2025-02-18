import requests
from config import EDAMAM_APP_ID, EDAMAM_APP_KEY

def get_nutritional_info(ingredient):
    url = "https://api.edamam.com/api/nutrition-data"
    params = {"app_id": EDAMAM_APP_ID, "app_key": EDAMAM_APP_KEY, "ingr": ingredient}
    response = requests.get(url, params=params)
    return response.json()

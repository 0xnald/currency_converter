import requests
from .base import BaseCurrencyConverterSkill

class CurrencyConverterSkill(BaseCurrencyConverterSkill):
    def __init__(self, config):
        self.api_key = config["api_key"]

    def convert_currency(self, amount, from_currency, to_currency):
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()
        if data.get("result") == "success":
            return data["conversion_result"]
        else:
            raise Exception(f"API error: {data.get('error-type', 'unknown error')}")

skill = CurrencyConverterSkill

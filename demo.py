from currency_converter.currency_converter import CurrencyConverterSkill

config = {
    "api_key": "YOUR_API_KEY"
}

skill = CurrencyConverterSkill(config)
result = skill.convert_currency(100, "USD", "EUR")
print(f"100 USD is approximately {result} EUR")

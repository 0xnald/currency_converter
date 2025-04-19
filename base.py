from intentkit import Skill

class BaseCurrencyConverterSkill(Skill):
    def convert_currency(self, amount, from_currency, to_currency):
        raise NotImplementedError("Subclasses must implement this method.")

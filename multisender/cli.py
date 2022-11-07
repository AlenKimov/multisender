import questionary
from questionary import Validator, ValidationError
import re

# Скрипты проекта
from config import settings, save_settings
from multisend import multisend


class FloatValidator(Validator):
    def validate(self, document):
        if not re.fullmatch(r"\d*\.\d+|\d+", document.text):
            raise ValidationError(
                message="Please enter a float value",
                cursor_position=len(document.text),
            )


class ConsoleMenu:
    def __init__(self):
        self.is_started = False

    def stop(self):
        self.is_started = False

    def set_amount(self):
        amount = questionary.text("Set amount: ", validate=FloatValidator).ask()
        settings.amount = float(amount)
        save_settings()

    def start(self):
        self.is_started = True
        while self.is_started:
            funcs = dict()
            funcs.update({"Start multisend": multisend})
            funcs.update({f"Amount: {settings.amount}": self.set_amount})
            funcs[questionary.select("MENU", choices=funcs).ask()]()


def main():
    menu = ConsoleMenu()
    menu.start()

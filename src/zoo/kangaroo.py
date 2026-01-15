# penguin.py

from .animal import Animal


class Penguin(Animal):
    def __init__(self, name="stumpy"):
        super().__init__(name, species="Penguin")

    def sound(self):
        return "fish"

    def action(self):
        return "nom nom"

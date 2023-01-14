from cards import Card
from dataclasses import dataclass
import time

@dataclass
class Deck:
    "This class is representing a deck of flashcards."
    def __init__(self, id, name: str, flashcard_list: list = None) -> None:
        if flashcard_list:
            self._flashcards = flashcard_list
        else:
            self._flashcards = []
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def flashcards(self):
        return self._flashcards

    @property
    def id(self):
        return self._id

    def get_due_cards():
        return [
            card for card in self._flashcards if card.due < time.time()
        ]


    def add_card(self, new_card: Card) -> None:
        self.flashcards.append(new_card)

    def remove_card(self, removed_card: Card) -> None:
        self.flashcards.remove(removed_card)

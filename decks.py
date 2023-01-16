from cards import Card
from dataclasses import dataclass, field
import time


@dataclass(order=False)
class Deck:
    name: str
    flashcards: list = field(default_factory=list)

    def get_due_cards(self):
        return [
            card for card in self.flashcards if card.review_date <= time.time() # NOQA
        ]

    def add_card(self, new_card: Card) -> None:
        self.flashcards.append(new_card)

    def remove_card(self, removed_card: Card) -> None:
        self.flashcards.remove(removed_card)

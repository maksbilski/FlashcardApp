from source.cards import Card
from dataclasses import dataclass, field
import time


@dataclass
class Deck:
    """
    A class representing a flashcard deck.
    A Deck has a name and a list of flashcards.
    """
    name: str
    flashcards: list = field(default_factory=list)

    def get_due_cards(self) -> list:
        """
        Returns a list of flashcards whose review date is
        less than or equal to the current time in UNIX Timestamp format.

        :return: list, list of all decks that are due for review
        """
        return [
            card for card in self.flashcards if card.review_date <= time.time() # NOQA
        ]

    def add_card(self, new_card: Card) -> None:
        """
        Add a flashcard to the deck
        :param new_card: flashcard object to be added to the deck
        """
        self.flashcards.append(new_card)

    def remove_card(self, removed_card: Card) -> None:
        """
        Remove a flashcard from the deck
        :param removed_card: flashcard object to be removed from the deck
        """
        self.flashcards.remove(removed_card)

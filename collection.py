from cards import Card
from decks import Deck
import json

DECKS_DATABASE_PATH = "data/decks.json"


def load_decks_data(path=DECKS_DATABASE_PATH):
    with open(path, 'r') as filehandle:
        data = json.load(filehandle)
        return data


class Collection:
    def __init__(self) -> None:
        self.serialized_data = load_decks_data()
        self.decklist = self.load_decklist()

    def export_deck_to_json(self, deck: Deck, filepath: str):
        """
        Exports the specified deck to a JSON file at the specified filepath.
        :param deck: The Deck object to be exported
        :param filepath: The filepath to save the JSON file
        """
        deck_data = {
            'name': deck.name,
            'flashcards': [card.to_json() for card in deck.flashcards]
        }
        with open(filepath, 'w') as filehandle:
            json.dump(deck_data, filehandle)

    def load_decklist(self):
        decklist = [
            Deck(deck_data['name'], [
                Card.from_json(json_data)
                for json_data in deck_data['flashcards']
            ])
            for deck_data in self.serialized_data
            ]
        return decklist

    def update_serialized_data(self):
        self.serialized_data = [
                {
                    'name': deck.name,
                    'flashcards': [card.to_json() for card in deck.flashcards]
                } for deck in self.decklist
            ]

    def update_source_file(self):
        with open(DECKS_DATABASE_PATH, 'w') as filehandle:
            json.dump(self.serialized_data, filehandle)

    def remove_deck(self, removed_deck: Deck):
        self.decklist.remove(removed_deck)

    def add_deck(self, new_deck):
        self.decklist.append(new_deck)

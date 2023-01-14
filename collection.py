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

    def load_decklist(self):
        decklist = [
            Deck(id, deck_data['name'], [
                Card.from_json(json_data)
                for json_data in deck_data['flashcards']
            ])
            for id, deck_data in self.serialized_data['decks'].items()
            ]
        return decklist

    def update_serialized_data(self):
        self.serialized_data['decks'] = {
            deck.id: {
                'name': deck.name,
                'flashcards': [card.to_json() for card in deck.flashcards]
            } for deck in self.decklist
        }

    def update_source_file(self):
        with open(DECKS_DATABASE_PATH, 'w') as filehandle:
            json.dump(self.serialized_data, filehandle)

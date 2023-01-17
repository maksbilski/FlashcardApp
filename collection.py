from errors import MalformedDeckDataError
from cards import Card
from decks import Deck
import json


DECKS_SOURCEFILE_PATH = "data/decks.json"


def load_decks_data(path=DECKS_SOURCEFILE_PATH):
    with open(path, 'r') as filehandle:
        data = json.load(filehandle)
        return data


class Collection:
    '''
    Class representing a collection of all the decks that are
    being currently used in the application.
    It provides
    '''
    def __init__(self) -> None:
        self.decklist = self.load_decklist()

    def import_deck_from_json(self, filepath: str) -> Deck:
        """
        Imports a Deck object from a JSON file at the specified filepath.
        :param filepath: The filepath of the JSON file to be imported
        :return: The imported Deck object
        """
        try:
            with open(filepath, 'r') as filehandle:
                data = json.load(filehandle)
            name = data['name']
            flashcards = [
                Card.from_json(card_data)
                for card_data in data['flashcards']
                ]
            self.decklist.append(Deck(name, flashcards))
        except (json.decoder.JSONDecodeError, KeyError) as e:
            raise MalformedDeckDataError(e)

    def export_deck_to_json(self, deck: Deck, filepath: str) -> dict:
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

    def load_decklist(self) -> list:
        """
        Loads the decks data from a JSON file
        and returns a list of Deck objects.
        :return: list of Deck objects
        """
        serialized_data = load_decks_data()
        decklist = [
            Deck(deck_data['name'], [
                Card.from_json(json_data)
                for json_data in deck_data['flashcards']
            ])
            for deck_data in serialized_data
            ]
        return decklist

    def get_serialized_json_data(self) -> list:
        """
        Returns a list of dictionaries
        that contains the serialized data of all decks.
        :return: list of dictionaries in JSON format
        """
        return [
                {
                    'name': deck.name,
                    'flashcards': [card.to_json() for card in deck.flashcards]
                } for deck in self.decklist
            ]

    def update_source_file(self, path=DECKS_SOURCEFILE_PATH):
        """
        Updates the decks data in the JSON file at the specified path
        :param path: The filepath to the decks data file
        """
        with open(path, 'w') as filehandle:
            json.dump(self.get_serialized_json_data(), filehandle)

    def remove_deck(self, removed_deck: Deck):
        """
        Removes a deck from the collection
        :param removed_deck: The deck object to be removed
        """
        self.decklist.remove(removed_deck)

    def add_deck(self, new_deck: Deck):
        """
        Adds a new deck to the collection
        :param new_deck: The deck object to be added
        """
        self.decklist.append(new_deck)

from classes.collection import Collection, load_decks_data
from classes.cards import Card
from classes.decks import Deck
import os
import tempfile
import json
import pytest # NOQA


@pytest.fixture(autouse=True)
def json_data_setup():
    json_data = [
        {
            "name": "Fruits and their colors",
            "flashcards": [
                {
                    "front": "What color is a banana?",
                    "back": "Yellow",
                    "review_date": 1674581553,
                    "interval": 6,
                    "ease_factor": 3,
                    "reps": 2
                },
                {
                    "front": "What color is a strawberry?",
                    "back": "Red",
                    "review_date": 1674581557,
                    "interval": 6,
                    "ease_factor": 2,
                    "reps": 2
                }
            ]
        }
    ]
    yield json_data
    json_data = None


def test_load_decks_data(tmpdir, json_data_setup):
    test_json_data = json_data_setup
    filepath = tmpdir.join("test_decks.json")
    with open(filepath, 'w') as f:
        json.dump(test_json_data, f)
    decks_data = load_decks_data(filepath)
    assert decks_data == test_json_data


def test_import_deck_from_json(tmpdir, json_data_setup):
    test_json_data = json_data_setup
    filepath = tmpdir.join("test_deck.json")
    with open(filepath, 'w') as f:
        json.dump(test_json_data[0], f)
    collection = Collection()
    collection.decklist = []
    collection.import_deck_from_json(filepath)
    assert len(collection.decklist) == 1
    assert collection.decklist[0].name == test_json_data[0]['name']
    assert len(collection.decklist[0].flashcards) == 2
    assert collection.decklist[0].flashcards[0].front == "What color is a banana?" # NOQA
    assert collection.decklist[0].flashcards[1].back == "Red"
    assert collection.decklist[0].flashcards[0].review_date == 1674581553
    assert collection.decklist[0].flashcards[1].interval == 6
    assert collection.decklist[0].flashcards[0].ease_factor == 3
    assert collection.decklist[0].flashcards[1].reps == 2


def test_export_deck_to_json(monkeypatch, json_data_setup):
    temp_file = tempfile.NamedTemporaryFile()
    filepath = temp_file.name
    flashcards = [Card.from_json(data) for data in json_data_setup[0]['flashcards']] # NOQA
    deck = Deck(json_data_setup[0]['name'], flashcards)
    collection = Collection()
    monkeypatch.setattr(collection, 'decklist', [deck])
    collection.export_deck_to_json(deck, filepath)
    assert os.path.exists(filepath)
    with open(filepath, 'r') as f:
        exported_data = json.load(f)
    assert exported_data == json_data_setup[0]
    temp_file.close()


def test_load_decklist(monkeypatch):
    json_data = [
        {
            "name": "Fruits and their colors",
            "flashcards": [
                {
                    "front": "What color is a banana?",
                    "back": "Yellow",
                    "review_date": 1674581553,
                    "interval": 6,
                    "ease_factor": 3,
                    "reps": 2
                },
                {
                    "front": "What color is a strawberry?",
                    "back": "Red",
                    "review_date": 1674581557,
                    "interval": 6,
                    "ease_factor": 2,
                    "reps": 2
                }
            ]
        }
    ]
    monkeypatch.setattr('collection.load_decks_data', lambda: json_data)
    collection = Collection()
    assert collection.decklist == [
        Deck("Fruits and their colors", [
            Card("What color is a banana?", "Yellow", review_date=1674581553, interval=6, ease_factor=3, reps=2), # NOQA
            Card("What color is a strawberry?", "Red", review_date=1674581557, interval=6, ease_factor=2, reps=2) # NOQA
        ])
    ]


def test_get_serialized_json_data(json_data_setup):
    collection = Collection()
    collection.decklist = [
        Deck("Fruits and their colors", [
            Card("What color is a banana?", "Yellow", review_date=1674581553, interval=6, ease_factor=3, reps=2), # NOQA
            Card("What color is a strawberry?", "Red", review_date=1674581557, interval=6, ease_factor=2, reps=2) # NOQA
        ])
    ]
    assert collection.get_serialized_json_data() == json_data_setup


def test_update_source_file(tmpdir, json_data_setup):
    collection = Collection()
    collection.decklist = [
        Deck("Fruits and their colors", [
            Card("What color is a banana?", "Yellow", review_date=1674581553, interval=6, ease_factor=3, reps=2), # NOQA
            Card("What color is a strawberry?", "Red", review_date=1674581557, interval=6, ease_factor=2, reps=2) # NOQA
        ])
    ]
    test_file_path = tmpdir.join('test_path.json')
    collection.update_source_file(test_file_path)
    with open(test_file_path, "r") as filehandle:
        test_file_data = json.load(filehandle)
    assert test_file_data == json_data_setup


def test_add_deck():
    collection = Collection()
    collection.decklist = [
        Deck("Fruits and their colors", [
            Card("What color is a banana?", "Yellow", review_date=1674581553, interval=6, ease_factor=3, reps=2), # NOQA
        ])
    ]
    deck2 = Deck("Fruits and their colors2", [
            Card("What color is a strawberry?", "Red", review_date=1674581557, interval=6, ease_factor=2, reps=2), # NOQA
        ])
    assert len(collection.decklist) == 1
    collection.add_deck(deck2)
    assert len(collection.decklist) == 2
    assert collection.decklist[1] == deck2


def test_remove_deck():
    collection = Collection()
    deck1 = Deck("Fruits and their colors", [
            Card("What color is a banana?", "Yellow", review_date=1674581553, interval=6, ease_factor=3, reps=2)]) # NOQA
    deck2 = Deck("Fruits and their colors2", [
            Card("What color is a strawberry?", "Red", review_date=1674581557, interval=6, ease_factor=2, reps=2)]) # NOQA

    collection.decklist = [deck1, deck2]
    assert len(collection.decklist) == 2
    collection.remove_deck(deck2)
    assert len(collection.decklist) == 1
    assert collection.decklist[0] == deck1

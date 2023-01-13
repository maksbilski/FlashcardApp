from decks import EmptyDeckNameError
from decks import Deck
from cards import Card
from pytest import raises


def test_create_deck():
    card1 = Card('Apple', 'Jabłko')
    card2 = Card('Banana', 'Banan')
    deck1 = Deck('Name', [card1, card2])
    assert deck1.name == 'Name'
    assert deck1.flashcards == [card1, card2]


def test_create_deck_default_list():
    deck1 = Deck('Name')
    assert deck1.name == 'Name'
    assert deck1.flashcards == []


def test_create_deck_empty_name_error():
    with raises(EmptyDeckNameError):
        _ = Deck(' ')

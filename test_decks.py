from collection import Deck
from cards import Card


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


def test_add_card_to_deck():
    deck1 = Deck('Name')
    deck1.add_card('Apple', 'Jabłko')
    assert deck1.flashcards == [Card('Apple', 'Jabłko')]

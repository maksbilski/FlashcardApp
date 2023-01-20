import time
import pytest # NOQA
from cards import Card
from decks import Deck


def test_get_due_cards(monkeypatch):
    monkeypatch.setattr(time, "time", lambda: 1623456789)
    card1 = Card("What is the capital of France?", "Paris", review_date=1623456788)
    card2 = Card("What is the capital of Russia?", "Moscow", review_date=1623456789)
    card3 = Card("What is the capital of Germany?", "Berlin", review_date=1623456790)
    flashcards = [card1, card2, card3]
    deck = Deck("deck_name", flashcards)
    assert len(deck.get_due_cards()) == 2
    assert deck.get_due_cards()[0] == card1
    assert deck.get_due_cards()[1] == card2


def test_add_card():
    card = Card("What is the capital of France?", "Paris", review_date=1623456789, interval=5, ease_factor=2.5, reps=3) # NOQA
    deck = Deck("deck_name")
    assert len(deck.flashcards) == 0
    deck.add_card(card)
    assert len(deck.flashcards) == 1
    assert deck.flashcards[0] == card


def test_remove_card():
    card = Card("What is the capital of France?", "Paris", review_date=1623456789, interval=5, ease_factor=2.5, reps=3) # NOQA
    deck = Deck("deck_name", [card])
    assert len(deck.flashcards) == 1
    deck.remove_card(card)
    assert len(deck.flashcards) == 0

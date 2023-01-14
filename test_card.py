from cards import Card
import pytest

@pytest.fixture()
def card():
    return Card("What is the capital of France?", "Paris", due=1623456789, interval=5, ease_factor=2.5, reps=3)


@pytest.fixture()
def card_default():
    return Card("What is the capital of France?", "Paris")


def test_str(card):
    assert str(card) == 'Card Front: What is the capital of France?\nCard back: Paris\nCard is due: 1623456789\nCurrent interval: 5\nCurrent ease_factor: 2.5\nTimes this card has been answered correctly in a row: 3'


def test_str_default_values(card_default):
    assert str(card_default) == 'Card Front: What is the capital of France?\nCard back: Paris\nCard is due: 0\nCurrent interval: 1\nCurrent ease_factor: 2.5\nTimes this card has been answered correctly in a row: 0'


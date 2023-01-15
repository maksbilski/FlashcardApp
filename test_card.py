from cards import Card
from datetime import datetime


def test_card_str_method():
    card = Card("What is the capital of France?", "Paris", review_date=1623456789, interval=5, ease_factor=2.5, reps=3) # NOQA
    readable_time = datetime.fromtimestamp(1623456789).strftime('%Y-%m-%d %H:%M:%S') # NOQA
    expected_output = (f"Card Front: What is the capital of France?\n"
                       f"Card back: Paris\n"
                       f"Card's next review date is: {readable_time}\n"
                       f"Current interval: 5\n"
                       f"Current ease_factor: 2.5\n"
                       f"Times this card has been answered correctly in a row: 3") # NOQA
    assert str(card) == expected_output

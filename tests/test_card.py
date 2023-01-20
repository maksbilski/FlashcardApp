from classes.cards import Card
from datetime import datetime
import time


def test_card_initialization():
    card = Card("What is the capital of France?", "Paris")
    assert card.front == "What is the capital of France?"
    assert card.back == "Paris"
    assert card.review_date == 0
    assert card.interval == 1
    assert card.ease_factor == 2.5
    assert card.reps == 0


def test_card_from_json():
    json_data = {
        'front': "What is the capital of France?",
        'back': "Paris",
        'review_date': int(datetime.now().timestamp()),
        'interval': 7,
        'ease_factor': 2.5,
        'reps': 3
    }
    card = Card.from_json(json_data)
    assert card.front == "What is the capital of France?"
    assert card.back == "Paris"
    assert card.review_date == json_data['review_date']
    assert card.interval == 7
    assert card.ease_factor == 2.5
    assert card.reps == 3


def test_card_to_json():
    card = Card("What is the capital of France?", "Paris", int(datetime.now().timestamp()), 7, 2.5, 3) # NOQA
    json_data = card.to_json()
    assert json_data['front'] == "What is the capital of France?"
    assert json_data['back'] == "Paris"
    assert json_data['review_date'] == card.review_date
    assert json_data['interval'] == 7
    assert json_data['ease_factor'] == 2.5
    assert json_data['reps'] == 3


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


def test_calculate_review_date_quality_3():
    card = Card("What is the capital of France?", "Paris")
    card.calculate_review_date(3)
    assert card.interval == 1
    assert card.ease_factor == 3
    assert card.reps == 1
    assert card.review_date == int(time.time() + 86400)


def test_calculate_review_date_quality_4():
    card = Card("What is the capital of France?", "Paris", review_date=int(time.time()), interval=1, ease_factor=2.5, reps=1) # NOQA
    card.calculate_review_date(4)
    assert card.interval == 6
    assert card.ease_factor == 3
    assert card.reps == 2
    assert card.review_date == int(time.time() + 6 * 86400)


def test_calculate_review_date_quality_2():
    card = Card("What is the capital of France?", "Paris", review_date=int(time.time()), interval=6, ease_factor=2.5, reps=2) # NOQA
    card.calculate_review_date(2)
    assert card.interval == 1
    assert card.ease_factor == 3
    assert card.reps == 0
    assert card.review_date == int(time.time() + 86400)

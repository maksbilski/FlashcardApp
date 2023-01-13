from cards import Card


def test_card_create():
    front = "Apple"
    back = "Jabłko"
    card1 = Card(front, back)
    assert card1.front == front
    assert card1.back == back
    assert card1.due == 0
    assert card1.interval == 1
    assert card1.ease_factor == 2.5
    assert card1.reps == 0

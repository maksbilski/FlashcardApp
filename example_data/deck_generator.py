import json
import random
import time


def main():
    flashcards = [
        {"front": "What is the capital of Germany?", "back": "Berlin", "review_date": 0, "interval": 0, "ease_factor": 2, "reps": 0},
        {"front": "What is the capital of Italy?", "back": "Rome", "review_date": 0, "interval": 0, "ease_factor": 2, "reps": 0},
        {"front": "What is the capital of Poland?", "back": "Warsaw", "review_date": 0, "interval": 0, "ease_factor": 2, "reps": 0},
        {"front": "What is the capital of Russia?", "back": "Moscow", "review_date": 0, "interval": 0, "ease_factor": 2, "reps": 0},
        {"front": "What is the capital of Japan?", "back": "Tokyo", "review_date": 0, "interval": 0, "ease_factor": 2, "reps": 0},
        {"front": "What is the capital of China?", "back": "Beijing", "review_date": 0, "interval": 0, "ease_factor": 2, "reps": 0}
    ]

    for card in flashcards:
        card["review_date"] = int(time.time()) - random.randint(1, 10365246060)  # 10 years in seconds

    deck_data = {
        'name': "Capital cities of the world",
        'flashcards': flashcards
    }

    with open("deck.json", "w") as filehandle:
        json.dump(deck_data, filehandle)

    print("Deck data generated and saved to deck.json")

if __name__ == "__main__":
    main()
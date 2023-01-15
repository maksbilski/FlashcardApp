from datetime import datetime
from dataclasses import dataclass
from math import ceil
import time

STARTING_EASE = 2.5
SECONDS_IN_A_DAY = 86400


@dataclass(order=True)
class Card:
    front: str
    back: str
    review_date: int = 0
    interval: int = 1
    ease_factor: float = STARTING_EASE
    reps: int = 0

    @classmethod
    def from_json(cls, json_data):
        front = json_data['front']
        back = json_data['back']
        review_date = json_data['review_date']
        interval = json_data['interval']
        ease_factor = json_data['ease_factor']
        reps = json_data['reps']
        return cls(front, back, review_date, interval, ease_factor, reps)

    def to_json(self) -> dict:
        card_data = {
            'front': self.front,
            'back': self.back,
            'review_date': self.review_date,
            'interval': self.interval,
            'ease_factor': self.ease_factor,
            'reps': self.reps
        }
        return card_data

    def __str__(self):
        readable_time = datetime.fromtimestamp(self.review_date).strftime('%Y-%m-%d %H:%M:%S') # NOQA
        return (f"Card Front: {self.front}\n"
                f"Card back: {self.back}\n"
                f"Card's next review date is: {readable_time}\n"
                f"Current interval: {self.interval}\n"
                f"Current ease_factor: {self.ease_factor}\n"
                f"Times this card has been answered correctly in a row: {self.reps}")  # NOQA

    def calculate_review_date(self, quality: int) -> None:
        if quality >= 3:
            self.interval = 1 if self.reps == 0 else 6 if self.reps == 1 else round(self.interval * self.ease_factor) # NOQA
            self.reps += 1
        else:
            self.reps = 0
            self.interval = 1
        self.ease_factor += (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)) # NOQA
        self.ease_factor = max(1.3, ceil(self.ease_factor))
        self.review_date = int(time.time() + self.interval * SECONDS_IN_A_DAY)

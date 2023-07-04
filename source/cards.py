from datetime import datetime
from dataclasses import dataclass
from math import ceil
import time

STARTING_EASE = 2.5
SECONDS_IN_A_DAY = 86400


@dataclass
class Card:
    """
    A data class representing a flashcard with a front and back side.
    The class contains various attributes that are used in the SM-2 algorithm
    to calculate the next review_date, including current review_date,
    interval, ease_factor, and reps.
    :param front: str, the text displayed on the front side of the card
    :param back: str, the text displayed on the back side of the card
    :param review_date: int, the date when the card is scheduled
        to be reviewed next, it is hold in UNIX Timestamp format, default is 0
    :param interval: int, the number of days between reviews, default is 1
    :param ease_factor: float, the ease factor used in the SM-2 algorithm,
        default is STARTING_EASE
    :param reps: int, the number of consecutive times the card
        has been answered correctly, default is 0
    """
    front: str
    back: str
    review_date: int = 0
    interval: int = 1
    ease_factor: float = STARTING_EASE
    reps: int = 0

    @classmethod
    def from_json(cls, json_data):
        """
        Creates a Card object from a JSON data.
        :param json_data: JSON data containing the card information
        :return: a Card object
        """
        front = json_data['front']
        back = json_data['back']
        review_date = json_data['review_date']
        interval = json_data['interval']
        ease_factor = json_data['ease_factor']
        reps = json_data['reps']
        return cls(front, back, review_date, interval, ease_factor, reps)

    def to_json(self) -> dict:
        """
        Returns a JSON object containing the card information
        :return: a dictionary in JSON format
        """
        card_data = {
            'front': self.front,
            'back': self.back,
            'review_date': self.review_date,
            'interval': self.interval,
            'ease_factor': self.ease_factor,
            'reps': self.reps
        }
        return card_data

    def __str__(self) -> str:
        """
        Returns a string representation of the card object,
        including the card's front, back, next review date,
        interval, ease factor, and number of reps.
        :return: str
        """
        if self.review_date == 0:
            readable_time = "card hasn't been reviewed yet."
        else:
            readable_time = datetime.fromtimestamp(self.review_date).strftime('%Y-%m-%d %H:%M:%S') # NOQA
        return (f"Card Front: {self.front}\n"
                f"Card back: {self.back}\n"
                f"Card's next review date is: {readable_time}\n"
                f"Current interval: {self.interval}\n"
                f"Current ease_factor: {self.ease_factor}\n"
                f"Times this card has been answered correctly in a row: {self.reps}")  # NOQA

    def calculate_review_date(self, quality: int) -> None:
        """
        Calculates the next review date for a flashcard
        based on the SM-2 algorithm.
        :param quality: int, a value between 0 and 5 representing the quality
            of user's familiarity of the card, the higher the quality
            the more user is familiar with the card.
        """
        if quality >= 3:
            if self.reps == 0:
                self.interval = 1
            elif self.reps == 1:
                self.interval = 6
            else:
                self.interval = round(self.interval * self.ease_factor)
            self.reps += 1
        else:
            self.reps = 0
            self.interval = 1

        self.ease_factor += (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)) # NOQA
        self.ease_factor = max(1.3, ceil(self.ease_factor))
        self.review_date = int(time.time() + self.interval * SECONDS_IN_A_DAY)

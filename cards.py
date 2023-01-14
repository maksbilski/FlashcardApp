from dataclasses import dataclass

STARTING_EASE = 2.5


@dataclass(order=True)
class Card:
    front: str
    back: str
    due: int = 0
    interval: int = 1
    ease_factor: float = STARTING_EASE
    reps: int = 0

    @classmethod
    def from_json(cls, json_data):
        front = json_data['front']
        back = json_data['back']
        due = json_data['due']
        interval = json_data['interval']
        ease_factor = json_data['ease_factor']
        reps = json_data['reps']
        return cls(front, back, due, interval, ease_factor, reps)

    def to_json(self):
        card_data = {
            'front': self.front,
            'back': self.back,
            'due': self.due,
            'interval': self.interval,
            'ease_factor': self.ease_factor,
            'reps': self.reps
        }
        return card_data

    def __str__(self):
        return (f'Card Front: {self.front}\n'
                f'Card back: {self.back}\n'
                f'Card is due: {self.due}\n'
                f'Current interval: {self.interval}\n'
                f'Current ease_factor: {self.ease_factor}\n'
                f'Times this card has been answered correctly in a row: {self.reps}')  # NOQA
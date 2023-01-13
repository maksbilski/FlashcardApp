from dataclasses import dataclass

STARTING_FACTOR_FRACTION = 2.5


@dataclass(order=True)
class Card:
    front: str
    back: str
    due: int = 0
    interval: int = 1
    ease_factor: float = STARTING_FACTOR_FRACTION
    reps: int = 0

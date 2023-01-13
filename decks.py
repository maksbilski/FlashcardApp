class EmptyDeckNameError(Exception):
    """Exception raised for an error when user
    tries to create a deck with an empty string.
    """

    def __init__(self, name, message="Deck name can't be an empty string"):
        self.name = name
        self.message = message
        super().__init__(self.message)


class Deck:
    "This class is representing a deck of flashcards."
    def __init__(self, name: str, flashcard_list: list = None) -> None:
        if name.isspace():
            raise EmptyDeckNameError(name)
        if flashcard_list:
            self.flashcards = flashcard_list
        else:
            self.flashcards = []
        self.name = name



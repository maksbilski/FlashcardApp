class NotExistingDeckError(Exception):
    def __init__(self, deck_name, message="There is no deck of given name."):
        self.name = deck_name
        self.message = message
        super().__init__(self.message)

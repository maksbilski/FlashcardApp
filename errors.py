

class EmptyUserInputError(Exception):
    def __init__(self, message):
        super().__init__(str(message))

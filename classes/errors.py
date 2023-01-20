

class EmptyUserInputError(Exception):
    def __init__(self, message):
        super().__init__(str(message))


class MalformedDeckDataError(Exception):
    def __init__(self, e):
        super().__init__(str(e))

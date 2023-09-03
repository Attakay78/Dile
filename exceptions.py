class ColumnDoesNotExist(Exception):
    def __init__(self, message):
        super().__init__(self, message)

class FieldTypeError(Exception):
    def __init__(self, message):
        super().__init__(self, message)

class MaxLengthExceeded(Exception):
    def __init__(self, message):
        super().__init__(self, message)

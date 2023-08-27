from exceptions import FieldTypeError


# Field descriptor for setting fields for columns
class Field:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__["fields"].get(self.name).field_value

    def __set__(self, instance, value):
        instance.__dict__["fields"][self.name].field_value = value


class CharField(Field):
    def __init__(self, max_length=10, **options):
        self.max_length = max_length

    def __set__(self, instance, value):
        if type(value) != str:
            msg = f"{value} expected type is str but {type(value)} given."
            raise FieldTypeError(msg)
        super().__set__(instance, value)


class TextField(Field):
    pass


class IntField(Field):
    def __set__(self, instance, value):
        if type(value) != int:
            msg = f"{value} expected type is int but {type(value)} given."
            raise FieldTypeError(msg)
        super().__set__(instance, value)

from exceptions import FieldTypeError, MaxLengthExceeded, FieldCantBeNull
from typing import Any


# Field descriptor for setting fields for columns
class Field:
    def __init__(
        self,
        name: str = None,
        max_length: int = None,
        nullable: bool = True,
        default: Any = None,
        editable: bool = True,  # TODO
        serialize: bool = True,  # TODO
        choices: Any = None,  # TODO
    ):
        self.field_name = name
        self.max_length = max_length
        self.is_nullable = nullable
        self.default = default
        self.is_editable = editable
        self.is_serializable = serialize
        self.choices = choices

    def __check_max_length(self, value: Any):
        if self.max_length and len(value) > self.max_length:
            msg: str = f"Maximum length exceeded, expected max of {self.max_length}, but got {len(value)}"
            raise MaxLengthExceeded(msg)

    def __check_is_nullable(self, value: Any):
        if self.is_nullable == False and value == None:
            msg: str = f"Field {self.name} can't be null"
            raise FieldCantBeNull(msg)

    def __set_name__(self, owner, name: str):
        if self.field_name:
            self.name = self.field_name
        else:
            self.name = name

    def __get__(self, instance, owner) -> Any:
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value: Any):
        self.__check_max_length(value)
        self.__check_is_nullable(value)
        instance.__dict__[self.name] = value


class CharField(Field):
    def __set__(self, instance, value: str):
        if type(value) != str and value != None:
            msg: str = f"{value} expected type is str but {type(value)} given."
            raise FieldTypeError(msg)
        super().__set__(instance, value)


class TextField(Field):
    pass


class IntField(Field):
    def __set__(self, instance, value: int):
        if type(value) != int and value != None:
            msg: str = f"{value} expected type is int but {type(value)} given."
            raise FieldTypeError(msg)
        super().__set__(instance, value)

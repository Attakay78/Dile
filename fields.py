from exceptions import FieldTypeError, MaxLengthExceeded


# Field descriptor for setting fields for columns
class Field:
    def __init__(
        self,
        name=None,
        max_length=None,
        null=False, #Yet to
        unique=False, #Yet to
        default=None,
        editable=True, #Yet to
        serialize=True, #Yet to
        choices=None, #Yet to
    ):
        self.field_name = name
        self.max_length = max_length
        self.is_nullable = null
        self._unique = unique
        self.default = default
        self.is_editable = editable
        self.is_serializable = serialize
        self.choices = choices
    
    def check_max_length(self, value):
        if self.max_length and len(value) > self.max_length:
            raise MaxLengthExceeded(f"Maximum length exceeded, expected max of {self.max_length}, but got {len(value)}")

    def __set_name__(self, owner, name):
        if self.field_name:
            self.name = self.field_name
        else:
            self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        self.check_max_length(value)
        instance.__dict__[self.name]= value


class CharField(Field):

    def __set__(self, instance, value):
        if type(value) != str and value != None:
            msg = f"{value} expected type is str but {type(value)} given."
            raise FieldTypeError(msg)
        super().__set__(instance, value)


class TextField(Field):
    pass


class IntField(Field):
    def __set__(self, instance, value):
        if type(value) != int and value != None:
            msg = f"{value} expected type is int but {type(value)} given."
            raise FieldTypeError(msg)
        super().__set__(instance, value)

from exceptions import ColumnDoesNotExist
from fields import Field


class Model_Subclass:
    def __init__(self, field_type=None, field_value=None):
        self.field_type = field_type
        self.field_value = field_value


# Model metaclass for creating the Model class
class ModelBase(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        return super().__new__(cls, name, bases, attrs, **kwargs)


# Model class with ModelBase as metaclass
class Model(metaclass=ModelBase):
    def __init__(self, **kwargs):
        # get dict value of subclasses
        subclass_dict = self.__class__.__dict__
        instance_dict = self.__dict__
        instance_dict["fields"] = {}
        
        # check the base classes of all the props in subclass_dict and add to the instance dict 
        # all props with base Field
        for prop, value in subclass_dict.items():
            base_classes = value.__class__.__bases__
            if base_classes and (Field in base_classes):
                instance_dict["fields"][prop] = Model_Subclass(field_type=value)
        
        for key, value in kwargs.items():
            if key in instance_dict["fields"]:
                instance_dict["fields"][key].field_type.__set__(self, value)
                pass
            else:
                raise ColumnDoesNotExist(f"{key} not a field in {self.__class__.__name__}")

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
        subclass_dict = self.__class__.__dict__.copy()
        instance_dict = self.__dict__
        
        # check the base classes of all the props in subclass_dict and add to the instance dict 
        # all props with base Field
        for prop, value in subclass_dict.items():
            base_classes = value.__class__.__bases__
            if base_classes and (Field in base_classes):
                instance_dict[prop] = value

                field_name = instance_dict[prop].field_name
                if field_name:
                    instance_dict[field_name] = instance_dict.pop(prop)
                    setattr(self.__class__, field_name, value)
        
        # Set key, value from model fields provided. Raise error if column does not exist
        for key, value in kwargs.items():
            if key in instance_dict:
                instance_dict[key].__set__(self, value)
            else:
                raise ColumnDoesNotExist(f"{key} not a field in {self.__class__.__name__}")
        
        # Set Default fields values
        if len(kwargs) < len(instance_dict):
            for field, value in instance_dict.items():
                if field not in kwargs.keys() and value.default != None:
                    instance_dict[field].__set__(self, value.default)
                elif field not in kwargs.keys():
                    instance_dict[field].__set__(self, None)

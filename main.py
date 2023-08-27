from model import Model
from fields import CharField, IntField

class Student(Model):
    first_name = CharField()
    last_name = CharField()
    age = IntField()

    def __str__(self):
        return f"Firstname: {self.first_name}, Lastname: {self.last_name}, Age: {self.age}"


class Employee(Model):
    name = CharField()
    age = IntField()

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

john = Student(first_name="John", last_name="Ron", age=34)

james = Student(first_name="James", last_name="Achon", age=25)

print(john)
print(james)

# Model -> List, List -> Model
# import pickle 

# serialized_data = pickle.dumps(john)
# deserialized_data = pickle.loads(serialized_data)

# # print(serialized_data)
# # print(deserialized_data)
# # print(john)

# def serialize(obj):
#     obj_fields = obj.__dict__["fields"]
#     serialize_data = []

#     for prop in obj_fields.keys():
#         if prop in obj.__dict__:
#             serialize_data.append(obj.__dict__[prop])
    
#     print(serialize_data)

# serialize(john)
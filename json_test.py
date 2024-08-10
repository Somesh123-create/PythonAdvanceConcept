import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

#load dict into json
personjson = json.dumps(person, indent=4, sort_keys=True)  # we can use sort

#how to load back json into python object
# persondict = json.loads(personjson)
# print(persondict)

#how to dump json into file
# with open('person.json', 'w') as f:
#     json.dump(person, f, indent=4)

#load json file in to python
# with open('person.json', 'r') as f:
#     data = json.load(f)
#     print(data)

#how to dump json from custom User class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# own function handler
def user_encode(o):
    if isinstance(o, User):
        return {'name':o.name, 'age': o.age, o.__class__.__name__:True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

# user_obj = User("john", 25)
# userjs = json.dumps(user_obj, default=user_encode)
# print(userjs)

#using json encoder base class
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name':o.name, 'age': o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self, o)

user_obj = User("john", 25)
# userjs = json.dumps(user_obj, cls=UserEncoder)
userjs = UserEncoder().encode(user_obj) #without json dumps
print(userjs)


#how to decode into User object
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct["age"])
    else:
        return dct



decode_user_obj = json.loads(userjs, object_hook=decode_user)
print(decode_user_obj)
print(decode_user_obj.name)
print(decode_user_obj.age)

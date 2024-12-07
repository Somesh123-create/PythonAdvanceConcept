"""
Metaclasses are classes of classes that define how classes themselves behave.
They allow customization of class creation and modification.
For example, you might use a metaclass to enforce coding standards by automatically adding certain methods or attributes to all classes created with it.
"""

# Define the metaclass
class SaveEnforcer(type):
    def __init__(cls, name, bases, dct):
        print("Name:",name)
        print("Base:",bases)
        print("Dict:",dct)
        super().__init__(name, bases, dct)
        # Check if 'save' method is not in the class dictionary
        if 'save' not in dct:
            # Add a default save method that raises NotImplementedError
            def default_save(self):
                raise NotImplementedError(f"{name}.save() must be implemented")
            cls.save = default_save

# Use the metaclass in a class definition
class BaseModel(metaclass=SaveEnforcer):
    pass

# Define a class without a 'save' method
class User(BaseModel):
    def __init__(self, username):
        self.username = username

# Define a class with a 'save' method
class Product(BaseModel):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        print(f"Saving product {self.name}")

# Test the classes
user = User("somesh")
try:
    user.save()  # This will raise NotImplementedError
except NotImplementedError as e:
    print(e)

product = Product("Laptop", 1200)
product.save()  # This will call the custom save method and print the message

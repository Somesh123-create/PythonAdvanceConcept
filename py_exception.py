#How to create custom exception from base Exception class

class ValueToHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

class ValueToLowError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueToHighError("Value to high", x)
    if x < 4:
        raise ValueToLowError("Value to low", x)

try:
    test_value(200)
except ValueToHighError as e:
    print(e.message, e.value)
except ValueToLowError as e:
    print(e.message, e.value)
else:
    print("Everything cool.")
finally:
    print("cleaning up memory.")

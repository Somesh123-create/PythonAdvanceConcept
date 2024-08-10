#implemente in class
class ManageFile:
    def __init__(self, filename):
        print("Init")
        self.filename = filename

    def __enter__(self):
        print("Entered")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("Handled exception")
        print("exit")
        return True



with ManageFile('new_text.txt') as file:
    file.write("Hello Somesh")


#implemente in function
from contextlib import contextmanager

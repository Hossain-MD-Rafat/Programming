import ctypes


# element = (10*ctypes.py_object)()
# print(len(element))

class DynamicArray(object):

    def __init__(self):
        self.index = 0
        self.capacity = 1
        self.arr = self.makeArray(self.capacity)

    def makeArray(self, size):
        return (ctypes.py_object * size)()

    def append(self, data):
        if not 0 <= self.index < self.capacity:
            self.capacity *= 2
        self.arr[self.index] = data
        self.index += 1

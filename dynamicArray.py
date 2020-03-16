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
        if not self.index < self.capacity:
            self.capacity *= 2
            arr1 =  self.makeArray(self.capacity)
            self.arr = [*self.arr, arr1]
        self.arr[self.index] = data
        self.index += 1
    def __len__(self):
        return self.index
    def __getitem__(self, indx):
        if 0 <= indx < self.index:
            return self.arr[indx]
        else:
            print("array is out of bound")
    def print(self):
        for i in range(self.index):
            print(self.arr[i])


a = DynamicArray()
a.append(5)
a.append(9)
a.append(8)
a.print()

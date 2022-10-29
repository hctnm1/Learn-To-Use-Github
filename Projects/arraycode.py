import ctypes
import random
class Array:
    def __init__(self,size):
        assert size> 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)
    def __len__(self):
        return self._size
    def __getitem__(self, index):
        assert index >= 0 and index < len(self),"Array subscript out of range"
        return self._elements[index]
    def __setitem__(self, index, value):
        assert index>=0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value
    def clear(self,value):
        for i in range(len(self)):
            self._elements[i]= value
    def _iter_(self):
        return _ArrayIterator(self._elements)
class ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx= 0
    def __iter__(self):
        return self._arrayRef
    def __next__(self):
        if self._curNdx<len(self._arrayRef):
            entry=self._arrayRef[self._curNdx]
            self._curNdx+=1
            return entery
        else:
            raise StopIteration



myarray = Array(10)
print("myarray legth is: ",len(myarray))
for i in range(len(myarray)):
    item =random.random()
    print("{} --> {:.2f}".format(i,item))
    myarray[i]=item
print ("myarray initialized upto {} values".format(len(myarray)))
aindex = int(input("Enter the index value of array element: "))
print("The array index '{}' contains item {:.2f}".format(aindex,myarray[aindex]))

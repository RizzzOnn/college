import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < len(self), "Index out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Index out of range"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

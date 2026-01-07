class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imag - other.imag)

    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return ComplexNumber(r, i)

    def __truediv__(self, other):
        d = other.real**2 + other.imag**2
        r = (self.real * other.real + self.imag * other.imag) / d
        i = (self.imag * other.real - self.real * other.imag) / d
        return ComplexNumber(r, i)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def magnitude(self):
        return (self.real**2 + self.imag**2) ** 0.5

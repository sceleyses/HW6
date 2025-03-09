
import math

class Circle:
    def __init__(self, r):
        self.r = r

    def isReal(self):
        return self.r > 0

    def perimeter(self): #ця частина є довжиною кола
        if self.isReal():
            return math.pi * (2*self.r)
        else:
            return []

    def plosha(self):
        if self.isReal():
            return math.pi*self.r**2
        else:
            return []


    def __str__(self):
        return f"Circle: {self.r}"

if __name__ == "__main__":
    c = Circle(10)
    print(c)
    print(c.perimeter())
    print(c.plosha())

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def isReal(self):
        return self.a > 0 and self.b > 0

    def perimeter(self):
        if self.isReal():
            return 2* (self.a + self.b)
        else:
            return []

    def plosha(self):
        if self.isReal():
            return self.a * self.b
        else:
            return []

    def __str__(self):
        return f"Rectangle: {self.a}, {self.b}"

if __name__ == "__main__":
    r = Rectangle(3, 4)
    print(r)
    print(r.perimeter())
    print(r.plosha())
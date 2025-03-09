
class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def isReal(self):
        return self.a > 0 and self.b > 0 and self.c > 0 and self.d > 0 and self.a != self.b

    def perimeter(self):
        if self.isReal():
            return self.a + self.b +self.c + self.d
        else:
            return []

    def plosha(self):
        if self.isReal():
            a, b, c, d = self.a, self.b, self.c, self.d
            h = (c**2 - (((b - a)**2 + c**2 - d**2) / (2 * (b - a)))**2)
            if h < 0:
                return []
            else:
                return ((a + b)/2) * (h**0.5)
        else:
            return []


    def __str__(self):
        return f"Trapeze: {self.a}, {self.b}, {self.c}, {self.d}"

if __name__ == "__main__":
    t = Trapeze(2, 4, 6, 8)
    print(t)
    print(t.perimeter())
    print(t.plosha())
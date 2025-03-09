
class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def isReal(self):
        return self.a > 0 and self.b > 0 and self.h > 0

    def perimeter(self):
        if self.isReal():
            return 2 * self.a + 2 * self.b
        else:
            return []

    def plosha(self):
        if self.isReal():
            return self.a * self.h
        else:
            return []

    def __str__(self):
        return f"Paralelogram: {self.a}, {self.b}, {self.h}"

if __name__ == "__main__":
    p = Parallelogram(5, 8, 21)
    print(p)
    print(p.perimeter())
    print(p.plosha())
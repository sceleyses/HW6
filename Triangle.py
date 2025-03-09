
class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def isReal(self):
        return (self.a > 0 and self.b > 0 and 0 < self.c < self.a + self.b and
                self.a + self.c > self.b and
                self.b + self.c > self.a)


    def perimeter(self):
        if self.isReal():
            return self.a + self.b + self.c
        else:
            return []


    def plosha(self):
        if self.isReal():
            P = self.perimeter()
            p = P / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            return []

    def __str__(self):
        return f"Triangle: {self.a}, {self.b}, {self.c}"


if __name__ == '__main__':
    t = Triangle(3, 4 ,5)
    print(t)
    print(t.perimeter())
    print(t.plosha())

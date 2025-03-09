class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def plosha(self):
        P = self.perimeter()
        p = P / 2
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            return None

    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}"


if __name__ == '__main__':
    t = Triangle(3, 4 ,5)
    print(t)
class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b +self.c + self.d

    def plosha(self):
        a, b, c, d = self.a, self.b, self.c, self.d

        if a == b:
            return None
        else:
            h = (c**2 - (((b - a)**2 + c**2 - d**2) / (2 * (b - a)))**2)**0.5
            return ((a + b)/2) * h


    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}, {self.d}"

if __name__ == "__main__":
    t = Trapeze(2, 4, 6, 8)
    print(t)
class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # def perimeter(self):

    # def plosha(self):

    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}, {self.d}"

if __name__ == "__main__":
    t = Trapeze(2, 4, 6, 8)
    print(t)
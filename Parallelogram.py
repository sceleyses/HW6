class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    # def perimeter(self):

    # def plosha(self):

    def __str__(self):
        return f"{self.a}, {self.b}, {self.h}"

if __name__ == "__main__":
    p = Parallelogram(5, 8, 21)
    print(p)
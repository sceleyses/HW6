class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def perimeter(self):

    # def plosha(self):

    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}"


if __name__ == '__main__':
    t = Triangle(3, 4 ,5)
    print(t)
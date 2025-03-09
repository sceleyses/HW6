class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def perimeter(self):
        return 2* (self.a + self.b)

    def plosha(self):
        return self.a * self.b

    def __str__(self):
        return f"{self.a}, {self.b}"

if __name__ == "__main__":
    r = Rectangle(3, 4)
    print(r)
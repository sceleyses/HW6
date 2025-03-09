import math

class Circle:
    def __init__(self, r):
        self.r = r

    def length(self):
        return math.pi * (2*self.r)

    def plosha(self):
        return math.pi*self.r**2


    def __str__(self):
        return f"{self.r}"

if __name__ == "__main__":
    c = Circle(10)
    print(c)
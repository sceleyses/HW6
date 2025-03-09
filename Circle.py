class Circle:
    def __init__(self, r):
        self.r = r

    # def length(self):

    # def plosha(self):

    def __str__(self):
        return f"{self.r}"

if __name__ == "__main__":
    c = Circle(10)
    print(c)
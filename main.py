from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
from Parallelogram import Parallelogram
from Circle import Circle


def sort_shapes(shape, bill):
    if shape == "Triangle":
        return Triangle(*bill)
    elif shape == "Rectangle":
        return Rectangle(*bill)
    elif shape == "Trapeze":
        return Trapeze(*bill)
    elif shape == "Parallelogram":
        return Parallelogram(*bill)
    elif shape == "Circle":
        return Circle(*bill)


def read_shapes(filename):
    shapes = []
    try:
        with open(filename) as f:
            for line in f:
                parts = line.strip().split()
                shape = parts[0]
                bill = [float(el) for el in parts[1:]]
                shape_type = sort_shapes(shape, bill)
                shapes.append(shape_type)
    except FileNotFoundError:
        return []
    return shapes


def max_perimeter(shapes):
    MaxShape = None
    MaxPerimeter = -1

    for shape in shapes:
        perimeter = shape.perimeter()
        if perimeter == []:
            continue
        if perimeter > MaxPerimeter:
            MaxPerimeter = perimeter
            MaxShape = shape
    return MaxShape


def max_plosha(shapes):
    MaxShape = None
    MaxPlosha = -1

    for shape in shapes:
        Plosha = shape.plosha()
        if Plosha == []:
            continue
        if Plosha > MaxPlosha:
            MaxPlosha = Plosha
            MaxShape = shape
    return MaxShape


def write_shapes(MaxPerimeter, MaxPlosha):
    with open("output.txt", "w") as f:
        if MaxPerimeter:
            f.write(f"max perimeter: {MaxPerimeter}\n")
        if MaxPlosha:
            f.write(f"max plosha: {MaxPlosha}\n")


shapes = []
input_files = ["input01.txt", "input02.txt", "input03.txt" ]

for file in input_files:
    shapes.extend(read_shapes(file))

MaxPerimeter = max_perimeter(shapes)
MaxPlosha = max_plosha(shapes)
write_shapes(MaxPerimeter, MaxPlosha)

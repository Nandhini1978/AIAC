def calculate_area(shape, *args):
    shape = shape.lower()
    if shape == "rectangle":
        if len(args) == 2:
            length, width = args
            return length * width
        else:
            raise ValueError("Rectangle requires length and width.")
    elif shape == "square":
        if len(args) == 1:
            side = args[0]
            return side * side
        else:
            raise ValueError("Square requires one side length.")
    elif shape == "circle":
        if len(args) == 1:
            radius = args[0]
            return 3.14 * radius * radius
        else:
            raise ValueError("Circle requires radius.")
    else:
        raise ValueError("Unknown shape")

# Example usage:
print(calculate_area("rectangle", 5, 10))
print(calculate_area("square", 4))
print(calculate_area("circle", 3))

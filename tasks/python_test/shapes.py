""" Shapes Module"""

PI = 3.14159

def circle_area(radius: float) -> float:
    """Gets the area of a circle"""
    area = PI * radius ** 2
    return area

def main(radius):
    results = circle_area(radius)
    print(f"{results:.2f}")


if __name__ == "__main__":
    main(5)
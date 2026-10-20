
def get_grade(score: int) -> str:
    """Return the letter grade for a score."""
    match score:
        case n if n >= 80:
            return "A"
        case n if n >= 70:
            return "B"
        case n if n >= 60:
            return "C"
        case _:
            return "F"

print(get_grade(85), get_grade(72), get_grade(60), get_grade(10))
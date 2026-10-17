def get_grade(score: int) -> str:
    """ Grading function"""
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


print(get_grade(85), get_grade(72), get_grade(60), get_grade(10))
PASS_MARK = 50


def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def get_stats(scores):
    lowest = min(scores)
    highest = max(scores)
    average = sum(scores) / len(scores)
    return lowest, highest, average


def main():
    names = ["Ama", "Kofi", "Yaw", "Esi", "Kwame"]
    raw_scores = ["90", "45", "72", "45", "58"]

    int_scores = [int(score) for score in raw_scores]
    results = dict(zip(names, int_scores))

    failed = []
    for name, score in results.items():
        grade = get_grade(score)
        if score >= PASS_MARK:
            status = "PASS"
        else:
            status = "FAIL"
            failed.append(name)
        print(f"{name}: {score} ({grade}) - {status}")

    lowest, highest, average = get_stats(int_scores)
    print(f"Lowest: {lowest}, Highest: {highest}, Average: {average:.2f}")

    unique_scores = set(int_scores)
    print(f"Unique scores: {len(unique_scores)}")

    print(f"Failed: {', '.join(failed)}")

    top_student = max(results, key=results.get)
    print(f"Top student: {top_student}")


if __name__ == "__main__":
    main()
import random
import statistics


def generate_grades(count):
    """Повертає список випадкових оцінок від 1 до 12."""
    return [random.randint(1, 12) for _ in range(count)]


def average_grade(grades):
    """Повертає середній бал зі списку оцінок."""
    if not grades:
        return 0.0
    return round(statistics.mean(grades), 2)


def get_level(average):
    """Визначає навчальний рівень за середнім балом."""
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатній"
    elif average >= 4:
        return "середній"
    else:
        return "початковий"


if __name__ == "__main__":
    test_grades = generate_grades(5)
    avg = average_grade(test_grades)
    print("Тест модуля:", test_grades, "->", avg, "->", get_level(avg))
import math
import random
import statistics
from datetime import date



# Завдання 1. Геометричні обчислення з math

def task1():
    print("--- Завдання 1: Геометричні обчислення ---")
    radius = float(input("Радіус: "))
    cathetus_a = float(input("Перший катет: "))
    cathetus_b = float(input("Другий катет: "))
    items = int(input("Предметів: "))
    capacity = int(input("В упаковці: "))

    circle_area = round(math.pi * (radius ** 2), 2)
    hypotenuse = round(math.sqrt(cathetus_a ** 2 + cathetus_b ** 2), 2)
    packages = math.ceil(items / capacity)

    print(f"Площа круга: {circle_area}")
    print(f"Гіпотенуза: {hypotenuse}")
    print(f"Потрібно упаковок: {packages}")



# Завдання 2. Генератор оцінок і статистичний звіт

def task2():
    print("\n--- Завдання 2: Генератор оцінок ---")
    n = int(input("Введіть кількість оцінок N: "))
    if n <= 0:
        print("Помилка: значення N повинно бути додатним.")
        return

    grades = [random.randint(1, 12) for _ in range(n)]
    high_grades_count = sum(1 for g in grades if 10 <= g <= 12)

    print(f"Оцінки: {grades}")
    print(f"Min: {min(grades)}")
    print(f"Max: {max(grades)}")
    print(f"Середнє: {round(statistics.mean(grades), 2)}")
    print(f"Медіана: {statistics.median(grades)}")
    print(f"Оцінок 10–12: {high_grades_count}")



# Завдання 3. Дата події

def task3():
    print("\n--- Завдання 3: Дата події ---")
    year = int(input("Рік події: "))
    month = int(input("Місяць події: "))
    day = int(input("День події: "))

    event_date = date(year, month, day)
    today = date.today()
    difference = (event_date - today).days

    if difference > 0:
        print(f"До події залишилося: {difference} днів")
    elif difference < 0:
        print(f"Після події минуло: {abs(difference)} днів")
    else:
        print("Подія відбувається сьогодні!")


if __name__ == "__main__":
    task1()
    task2()
    task3()
import math
import random
import statistics
from datetime import date, datetime
import tkinter as tk


# Приклад 1. math: гіпотенуза і площа круга

print("--- Приклад 1 ---")
a = 6
b = 8
hypotenuse = math.sqrt(a ** 2 + b ** 2)
radius = 5
circle_area = math.pi * radius ** 2

print("Гіпотенуза:", hypotenuse)
print("Площа круга:", round(circle_area, 2))



# Приклад 2. ceil() і floor()

print("\n--- Приклад 2 ---")
items = 25
capacity = 6
print("Повних упаковок:", math.floor(items / capacity))
print("Упаковок потрібно:", math.ceil(items / capacity))



# Приклад 3. random.randint(): 10 випадкових чисел

print("\n--- Приклад 3 ---")
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)



# Приклад 4. random.choice(): випадковий вибір

print("\n--- Приклад 4 ---")
students = ["Anna", "Ivan", "Olha", "Maksym"]
selected = random.choice(students)
print("Обрано:", selected)



# Приклад 5. random.shuffle(): перемішування списку

print("\n--- Приклад 5 ---")
questions = [1, 2, 3, 4, 5]
random.shuffle(questions)
print("Новий порядок:", questions)



# Приклад 6. statistics.mean() і median()

print("\n--- Приклад 6 ---")
grades = [10, 8, 12, 9, 11, 10]
print("Середнє:", statistics.mean(grades))
print("Медіана:", statistics.median(grades))


# Приклад 7. Поточна дата і час

print("\n--- Приклад 7 ---")
print("Дата:", date.today())
print("Дата і час:", datetime.now())



# Приклад 8. Кількість днів між датами

print("\n--- Приклад 8 ---")
date1 = date(2026, 10, 1)
date2 = date(2026, 12, 31)
difference = date2 - date1
print("Днів:", difference.days)



# Приклади 9 і 10. Імітація роботи власного модуля

print("\n--- Приклади 9-10 ---")
def square(number):
    return number ** 2

def is_even(number):
    return number % 2 == 0

def average(nums):
    return sum(nums) / len(nums)

nums_list = [4, 8, 10, 12]
print(square(5))
print(is_even(8))
print(average(nums_list))



# Приклад 11. import math та from math import sqrt

print("\n--- Приклад 11 ---")
print(math.sqrt(100))
from math import sqrt
print(sqrt(100))



# Приклад 12. Міні-проєкт: випадкові оцінки + статистика

print("\n--- Приклад 12 ---")
rand_grades = []
for i in range(20):
    rand_grades.append(random.randint(1, 12))

print("Оцінки:", rand_grades)
print("Min:", min(rand_grades))
print("Max:", max(rand_grades))
print("Середнє:", round(statistics.mean(rand_grades), 2))
print("Медіана:", statistics.median(rand_grades))

high = 0
for grade in rand_grades:
    if grade >= 10:
        high += 1
print("Оцінок 10–12:", high)



# Приклад 13. Перше вікно Tkinter

window13 = tk.Tk()
window13.title("Лабораторна №6")
window13.geometry("400x200")

label13 = tk.Label(window13, text="Модулі та бібліотеки Python")
label13.pack(pady=20)

button13 = tk.Button(window13, text="Закрити", command=window13.destroy)
button13.pack(pady=10)

window13.mainloop()



# Приклад 14. Поле введення та кнопка

def greet():
    name = name_entry.get().strip()
    if name == "":
        result14.configure(text="Введіть ім’я")
    else:
        result14.configure(text="Вітаю, " + name + "!")

window14 = tk.Tk()
window14.title("Привітання")
window14.geometry("400x250")

tk.Label(window14, text="Ваше ім’я:").pack(pady=5)
name_entry = tk.Entry(window14, width=30)
name_entry.pack(pady=5)

tk.Button(window14, text="Привітатися", command=greet).pack(pady=10)

result14 = tk.Label(window14, text="")
result14.pack(pady=5)

window14.mainloop()



# Приклад 15. Tkinter разом із random та statistics

def generate_report():
    value = count_entry.get().strip()
    if not value.isdecimal():
        result15.configure(text="Введіть ціле число від 1 до 100")
        return

    count = int(value)
    if count < 1 or count > 100:
        result15.configure(text="Кількість має бути від 1 до 100")
        return

    grades_list = []
    for i in range(count):
        grades_list.append(random.randint(1, 12))

    avg = statistics.mean(grades_list)
    med = statistics.median(grades_list)

    text = "Оцінки: " + str(grades_list)
    text += "\nСереднє: " + str(round(avg, 2))
    text += "\nМедіана: " + str(med)
    result15.configure(text=text)

window15 = tk.Tk()
window15.title("Генератор оцінок")
window15.geometry("500x350")

tk.Label(window15, text="Кількість оцінок (1–100):").pack(pady=5)
count_entry = tk.Entry(window15)
count_entry.pack(pady=5)

tk.Button(window15, text="Згенерувати", command=generate_report).pack(pady=10)

result15 = tk.Label(window15, text="", wraplength=460, justify="left")
result15.pack(pady=10)

window15.mainloop()
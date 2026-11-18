
# Завдання 1. Аналіз і фільтрація списку

print("=== Завдання 1 ===")
numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]

positive = []
negative = []
even = []
multiples_of_3 = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

    if num % 2 == 0:
        even.append(num)

    if num % 3 == 0:
        multiples_of_3.append(num)

min_val = min(numbers)
max_val = max(numbers)
total_sum = sum(numbers)
average_val = round(total_sum / len(numbers), 2)

print("Додатні:", positive)
print("Від’ємні:", negative)
print("Парні:", even)
print("Кратні 3:", multiples_of_3)
print(f"Min: {min_val}; Max: {max_val}; Sum: {total_sum}; Average: {average_val}")



# Завдання 2. Дві групи учасників

print("\n=== Завдання 2 ===")
group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}

common = sorted(group1 & group2)
only_group1 = sorted(group1 - group2)
only_group2 = sorted(group2 - group1)
all_unique = sorted(group1 | group2)

print("Спільні:", ", ".join(common))
print("Тільки group1:", ", ".join(only_group1))
print("Тільки group2:", ", ".join(only_group2))
print("Усі:", ", ".join(all_unique))



# Завдання 3. Каталог товарів

print("\n=== Завдання 3 ===")
catalog = {
    "bread": 35,
    "milk": 48,
    "cheese": 120
}

# Додавання нового товару та зміна ціни існуючого
catalog["tea"] = 75
catalog["bread"] = 38

# Безпечний пошук за назвою через get()
search_item = "milk"
price_found = catalog.get(search_item)
if price_found is not None:
    print(f"Пошук '{search_item}': {price_found} грн")
else:
    print(f"Товар '{search_item}' не знайдено")

print("Пошук 'coffee':", catalog.get("coffee", "Товар не знайдено"))

# Виведення товарів у заданому ціновому діапазоні (40..100 грн)
min_price, max_price = 40, 100
print(f"Товари у діапазоні {min_price}..{max_price} грн:")
for product, price in catalog.items():
    if min_price <= price <= max_price:
        print(f"{product} — {price} грн")



# Завдання 4. Журнал групи

print("\n=== Завдання 4 ===")
group_info = ('10-IT', '2026/2027')
journal = {}


def add_student(db, name, grades):
    if len(grades) != 5:
        print(f"Помилка для {name}: потрібно рівно 5 оцінок.")
        return
    for g in grades:
        if not (1 <= g <= 12):
            print(f"Помилка для {name}: оцінка {g} поза межами 1–12.")
            return
    db[name] = grades


add_student(journal, "Anna", [10, 11, 12, 9, 10])
add_student(journal, "Ivan", [8, 9, 10, 11, 9])
add_student(journal, "Olha", [11, 12, 11, 12, 10])

# Друк інформації про групу та всього журналу
group_name, academic_year = group_info
print(f"{group_name} — {academic_year}")
for student, grades in journal.items():
    print(f"{student}: {grades}")

# Обчислення середнього балу кожного учня
averages = {}
print("\nСередній бал учнів:")
for student, grades in journal.items():
    avg = round(sum(grades) / len(grades), 2)
    averages[student] = avg
    print(f"{student} — {avg}")

# Рейтинг учнів за середнім балом
rating = sorted(averages.items(), key=lambda item: item[1], reverse=True)
print("\nРейтинг учнів:")
for place, (student, avg) in enumerate(rating, start=1):
    print(f"{place}. {student} — {avg}")

# Пошук учня з найвищим середнім балом
best_student, best_avg = rating[0]
print(f"\nНайкращий результат: {best_student} — {best_avg}")



# Додаткове завдання

print("\n=== Додаткове завдання ===")
extended_journal = {
    "Anna": {
        "Python": [11, 12, 12],
        "Math": [10, 11, 10]
    },
    "Ivan": {
        "Python": [9, 10, 9],
        "Math": [8, 9, 10]
    }
}

for student, subjects in extended_journal.items():
    print(f"Учень: {student}")
    for subject, grades in subjects.items():
        subj_avg = round(sum(grades) / len(grades), 2)
        print(f"  {subject}: {subj_avg}")
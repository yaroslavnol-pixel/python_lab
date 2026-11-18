
# Завдання 1. Площі геометричних фігур


def area_circle(radius):
    """Обчислює площу круга за радіусом."""
    pi = 3.14159
    return pi * (radius ** 2)


def area_rectangle(width, height):
    """Обчислює площу прямокутника."""
    return width * height


def area_triangle(base, height):
    """Обчислює площу трикутника за основою та висотою."""
    return 0.5 * base * height


def task1_main():
    print("--- Завдання 1: Площі фігур ---")
    shape = input("Фігура (круг / прямокутник / трикутник): ").strip().lower()

    if shape == "круг":
        r = float(input("Радіус: "))
        print(f"Площа круга: {round(area_circle(r), 2)}")
    elif shape == "прямокутник":
        w = float(input("Ширина: "))
        h = float(input("Висота: "))
        result = area_rectangle(w, h)
        # Виводимо ціле число, якщо дробова частина нульова (як у прикладі: 40)
        print(f"Площа прямокутника: {int(result) if result.is_integer() else result}")
    elif shape == "трикутник":
        base = float(input("Основа: "))
        h = float(input("Висота: "))
        result = area_triangle(base, h)
        print(f"Площа трикутника: {int(result) if result.is_integer() else result}")
    else:
        print("Невідома фігура.")



# Завдання 2. Функції для аналізу числа


def is_prime(n):
    """Визначає, чи є натуральне число n простим."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divisors(n):
    """Повертає список усіх дільників числа n."""
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def digit_sum(n):
    """Повертає суму цифр натурального числа n."""
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


def task2_main():
    print("\n--- Завдання 2: Аналіз числа ---")
    n = int(input("Введіть натуральне число N: "))
    prime_text = "так" if is_prime(n) else "ні"
    print(f"Просте число: {prime_text}")
    print(f"Дільники: {divisors(n)}")
    print(f"Сума цифр: {digit_sum(n)}")



# Завдання 3. Звіт за списком оцінок (3 б.)


def average(grades):
    """Повертає середній бал зі списку оцінок."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def minimum(grades):
    """Повертає мінімальну оцінку."""
    return min(grades)


def maximum(grades):
    """Повертає максимальну оцінку."""
    return max(grades)


def count_above(grades, value):
    """Повертає кількість оцінок, строго більших за value."""
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count


def print_grades_report(grades, threshold):
    """Формує та виводить звіт за оцінками."""
    print(f"Оцінки: {grades}")
    print(f"Середній бал: {round(average(grades), 2)}")
    print(f"Мінімальна: {minimum(grades)}")
    print(f"Максимальна: {maximum(grades)}")
    print(f"Вище {threshold}: {count_above(grades, threshold)}")


def task3_main():
    print("\n--- Завдання 3: Звіт за списком оцінок ---")
    grades = [10, 8, 12, 9, 11]
    threshold = 9
    print_grades_report(grades, threshold)



# Завдання 4. Перевірка надійності пароля


def has_min_length(password, min_len=8):
    """Перевіряє мінімальну довжину пароля."""
    return len(password) >= min_len


def has_digit(password):
    """Перевіряє наявність хоча б однієї цифри."""
    return any(char.isdigit() for char in password)


def has_uppercase(password):
    """Перевіряє наявність хоча б однієї великої літери."""
    return any(char.isupper() for char in password)


def has_lowercase(password):
    """Перевіряє наявність хоча б однієї малої літери."""
    return any(char.islower() for char in password)


def has_special_char(password):
    """Перевіряє наявність спеціального символу (не літери і не цифри)."""
    return any(not char.isalnum() for char in password)


def validate_password(password):
    """Перевіряє пароль за всіма правилами та повертає (bool, list_of_errors)."""
    errors = []

    if not has_min_length(password):
        errors.append("довжина менше 8 символів")
    if not has_digit(password):
        errors.append("немає цифри")
    if not has_uppercase(password):
        errors.append("немає великої літери")
    if not has_lowercase(password):
        errors.append("немає малої літери")
    if not has_special_char(password):
        errors.append("немає спеціального символу")

    is_valid = len(errors) == 0
    return is_valid, errors


def task4_main():
    print("\n--- Завдання 4: Перевірка пароля ---")
    password = input("Введіть пароль для перевірки: ")
    is_valid, missing_requirements = validate_password(password)

    if is_valid:
        print("Пароль надійний і відповідає всім вимогам.")
    else:
        print("Пароль не відповідає вимогам.")
        print("Не виконано:", ", ".join(missing_requirements))



# Додаткове завдання. «Щасливі квитки»


def is_lucky_ticket(number):
    """Перевіряє, чи є шестизначний номер щасливим квитком."""
    ticket_str = f"{number:06d}"
    first_half = sum(int(d) for d in ticket_str[:3])
    second_half = sum(int(d) for d in ticket_str[3:])
    return first_half == second_half


def find_lucky_tickets(start, end):
    """Знаходить усі щасливі квитки у заданому діапазоні [start, end]."""
    lucky_list = []
    for num in range(start, end + 1):
        if 0 <= num <= 999999 and is_lucky_ticket(num):
            lucky_list.append(f"{num:06d}")
    return lucky_list


def bonus_task_main():
    print("\n--- Додаткове завдання: Щасливі квитки ---")
    tickets = find_lucky_tickets(100000, 100500)
    print(f"Щасливі квитки у діапазоні 100000–100500 ({len(tickets)} шт.):")
    print(", ".join(tickets))



# Головна точка входу


def main():
    task1_main()
    task2_main()
    task3_main()
    task4_main()
    bonus_task_main()


if __name__ == "__main__":
    main()
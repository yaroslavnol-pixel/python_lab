# 1 завдання

n = int(input('N = '))
total = 0
count = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        count += 1

print("Сума:", total)
print("Кількість:", count)

if count > 0:
    average = total / count
    print("Середнє арифметичне:", average)
else:
    print("Таких чисел немає, тому ділення на нуль не виконується.")



# 2 завдання

n = int(input('N = '))

if n == 0:
    print("Кількість цифр: 1")
    print("Сума цифр: 0")
    print("Найбільша цифра: 0")
    print("Найменша цифра: 0")
else:
    count = sum_digits = 0
    max_digit = min_digit = n % 10
    temp = n

    while temp > 0:
        a = temp % 10
        sum_digits += a
        count += 1
        if a > max_digit:
            max_digit = a
        if a < min_digit:
            min_digit = a
        temp //= 10

    print("Кількість цифр:", count)
    print("Сума цифр:", sum_digits)
    print("Найбільша цифра:", max_digit)
    print("Найменша цифра:", min_digit)


# 3 завдання


n = int(input("N = "))

for i in range(1, n + 1):
    temp = i
    ok = True

    while temp > 0:
        a = temp % 10

        if a != 0:
            if i % a != 0:
                ok = False
                break

        temp = temp // 10

    if ok:
        print(i, end=" ")


# 4 завдання

width = int(input("width = "))
height = int(input("height = "))
contour = input("контур = ")
inner = input("всередині = ")

if width < 3 or height < 3:
    print("Помилка: мінімальний розмір рамки — 3x3")
else:
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print(contour, end="")
            else:
                print(inner, end="")
        print()

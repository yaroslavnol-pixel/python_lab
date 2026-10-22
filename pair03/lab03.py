# ==========================================
# Завдання 1. Статистика тексту (2 б.)
# ==========================================
print("--- Завдання 1 ---")
text1 = input("Введіть довільний текст: ")

vowels_set = "аеєиіїоуюяaeiou"
total_chars = len(text1)
letter_count = 0
digit_count = 0
space_count = 0
vowel_count = 0

for char in text1:
    if char.isalpha():
        letter_count += 1
    if char.isdigit():
        digit_count += 1
    if char == " ":
        space_count += 1
    if char.lower() in vowels_set:
        vowel_count += 1

words = text1.split()
word_count = len(words)

print(f"Символів: {total_chars}")
print(f"Літер: {letter_count}")
print(f"Цифр: {digit_count}")
print(f"Пробілів: {space_count}")
print(f"Голосних: {vowel_count}")
print(f"Слів: {word_count}\n")

# ==========================================
# Завдання 2. Нормалізація ПІБ (3 б.)
# ==========================================
print("--- Завдання 2 ---")
pib_input = input("Введіть ПІБ (Прізвище Ім'я По батькові): ")

pib_parts = pib_input.split()

if len(pib_parts) == 3:
    surname = pib_parts[0].capitalize()
    first_name_initial = pib_parts[1][0].upper()
    patronymic_initial = pib_parts[2][0].upper()

    result_pib = f"{surname} {first_name_initial}.{patronymic_initial}."
    print("Результат:", result_pib)
else:
    print("Помилка: Введено некоректну кількість слів. Потрібно ввести 3 слова (Прізвище, Ім'я, По батькові).")
print()

# ==========================================
# Завдання 3. Анаграми (3 б.)
# ==========================================
print("--- Завдання 3 ---")
str1 = input("Введіть перший рядок: ")
str2 = input("Введіть второй рядок: ")

norm1 = str1.lower().replace(" ", "")
norm2 = str2.lower().replace(" ", "")

if sorted(norm1) == sorted(norm2):
    print(f"Рядки '{str1}' та '{str2}' є анаграмами.")
else:
    print(f"Рядки '{str1}' та '{str2}' НЕ є анаграмами.")
print()

# ==========================================
# Завдання 4. Аналіз речення (4 б.)
# ==========================================
print("--- Завдання 4 ---")
sentence = input("Введіть речення: ")
words_raw = sentence.split()
clean_words = []
for w in words_raw:
    cleaned = w.strip(".,!?:;\"'()[]{}")
    if cleaned:
        clean_words.append(cleaned)

if clean_words:
    min_len = min(len(w) for w in clean_words)
    max_len = max(len(w) for w in clean_words)

    shortest_words = list(dict.fromkeys([w for w in clean_words if len(w) == min_len]))
    longest_words = list(dict.fromkeys([w for w in clean_words if len(w) == max_len]))

    unique_words = set(w.lower() for w in clean_words)

    print("Найдовші:", ", ".join(longest_words))
    print("Найкоротші:", ", ".join(shortest_words))
    print("Унікальних слів:", len(unique_words))

    target_word = input("Введіть слово для заміни: ")
    new_word = input("Введіть нове слово: ")

    modified_sentence = sentence.replace(target_word, new_word)
    print("Після заміни:", modified_sentence)
else:
    print("Речення не містить слів.")
print()

# ==========================================
# 7. Додаткове завдання (Шифр)
# ==========================================
print("--- Додаткове завдання (Шифр Цезаря) ---")
secret_text = input("Введіть текст для шифрування: ")
try:
    shift = int(input("Введіть величину зсуву (ціле число): "))

    encrypted_text = "".join(chr(ord(c) + shift) for c in secret_text)
    print("Зашифрований текст:", encrypted_text)

    decrypted_text = "".join(chr(ord(c) - shift) for c in encrypted_text)
    print("Розшифрований текст:", decrypted_text)
except ValueError:
    print("Введено некоректний зсув.")
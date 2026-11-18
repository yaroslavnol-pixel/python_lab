import tkinter as tk
import student_utils


STUDENTS = ["Anna", "Ivan", "Olha"]


def create_report():
    raw_value = count_entry.get().strip()


    if not raw_value.isdecimal():
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Помилка: введіть ціле число від 1 до 20.")
        return

    count = int(raw_value)
    if count < 1 or count > 20:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Помилка: кількість оцінок має бути від 1 до 20.")
        return

    report_lines = []
    for student in STUDENTS:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        report_lines.append(f"{student}: {grades} -> {avg} -> {level}")

    report = "\n".join(report_lines)


    print("\n--- Звіт за учнями ---")
    print(report)


    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, report)


window = tk.Tk()
window.title("Статистика учнів")
window.geometry("520x320")

tk.Label(window, text="Введіть кількість оцінок для кожного учня (1–20):").pack(pady=8)

count_entry = tk.Entry(window, width=20)
count_entry.pack(pady=5)

tk.Button(window, text="Сформувати звіт", command=create_report).pack(pady=10)

output_text = tk.Text(window, width=60, height=10)
output_text.pack(pady=8)

window.mainloop()
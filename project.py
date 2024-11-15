import tkinter as tk
from tkinter import messagebox
import math
# создание функции для квадратного уравнения
def solve_quadratic_equation():
    # ввод даннных(квадратные уравнения)
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    discriminant = b**2 - 4*a*c # формула дискриминанта
    # если дискриминант больше нуля
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = f"Корни уравнения: x1 = {x1}, x2 = {x2}"
    # если дискриминант равен нулю    
    elif discriminant == 0:
        x = -b / (2*a)
        result = f"Уравнение имеет единственный корень: x = {x}"
    # если дискриминант меньше нуля    
    else:
        result = "Уравнение не имеет действительных корней"
    
    # вывод результата
    messagebox.showinfo("Результат", result)
# создание функции для не полного квадратного уравнения
def solve_incomplete_quadratic_equation():
    # ввод данных
    a = float(entry_a.get())
    b = float(entry_b.get())

    x = -(b / a)
    result = f"Корень уравнения: x = {x}"
    # выводрезультата
    messagebox.showinfo("Результат", result)
# создание функции для конвертера систем счисления
def convert_number():
    number = entry_number.get()
    base_from = int(entry_base_from.get())
    base_to = int(entry_base_to.get())

    try:
        number_in_base_10 = int(number, base_from)
        converted_number = str(format(number_in_base_10, 'X')) if base_to == 16 else str(format(number_in_base_10, base_to))
        result = f"Конвертированное число: {converted_number}"
    except ValueError:
        result = "Ошибка: введено недопустимое число или система счисления"

    messagebox.showinfo("Результат", result)

# Создание главного окна
window = tk.Tk()
window.title("Калькулятор квадратных уравнений/конвертер систем счисления")
window.geometry("500x500")

# Создание виджетов
label_title = tk.Label(window, text="Квадратные уравнения")
label_a = tk.Label(window, text="Введите a:")
entry_a = tk.Entry(window)
label_b = tk.Label(window, text="Введите b:")
entry_b = tk.Entry(window)
label_c = tk.Label(window, text="Введите c:")
entry_c = tk.Entry(window)
button_solve_quadratic = tk.Button(window, text="Решить", command=solve_quadratic_equation)

label_title.pack()
label_a.pack()
entry_a.pack()
label_b.pack()
entry_b.pack()
label_c.pack()
entry_c.pack()
button_solve_quadratic.pack()

# Создание виджетов для квадратных неполных уравнений
label_incomplete_title = tk.Label(window, text="Квадратные неполные уравнения")
label_incomplete_a = tk.Label(window, text="Введите a:")
entry_incomplete_a = tk.Entry(window)
label_incomplete_b = tk.Label(window, text="Введите b:")
entry_incomplete_b = tk.Entry(window)
button_solve_incomplete = tk.Button(window, text="Решить", command=solve_incomplete_quadratic_equation)

label_incomplete_title.pack()
label_incomplete_a.pack()
entry_incomplete_a.pack()
label_incomplete_b.pack()
entry_incomplete_b.pack()
button_solve_incomplete.pack()

# Создание виджетов для конвертера систем счисления
label_conversion_title = tk.Label(window, text="Конвертер систем счисления")
label_number = tk.Label(window, text="Введите число:")
entry_number = tk.Entry(window)
label_base_from = tk.Label(window, text="Из системы счисления:")
entry_base_from = tk.Entry(window)
label_base_to = tk.Label(window, text="В систему счисления:")
entry_base_to = tk.Entry(window)
button_convert = tk.Button(window, text="Конвертировать", command=convert_number)

label_conversion_title.pack()
label_number.pack()
entry_number.pack()
label_base_from.pack()
entry_base_from.pack()
label_base_to.pack()
entry_base_to.pack()
button_convert.pack()

# Запуск главного цикла окна
window.mainloop()
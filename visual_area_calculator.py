import sys
import os
import customtkinter as tk
from tkinter import messagebox
import git
import requests
import webbrowser

__version__ = "0.0.5"

REPO_URL = "https://github.com/Eternal1of/Callc"
RELEASES_URL = "https://api.github.com/repos/Eternal1of/Callc/releases"

# Глобальная переменная для отслеживания количества открытых окон
open_windows_count = 0

def update_from_github():
    try:
        repo = git.Repo(".")
        repo.remotes.origin.pull()
        messagebox.showinfo("Обновление", "Приложение было успешно обновлено.")
    except git.exc.GitCommandError as e:
        messagebox.showerror("Ошибка обновления", str(e))

def check_updates():
    try:
        response = requests.get(RELEASES_URL)
        response.raise_for_status()
        releases = response.json()
        latest_version = releases[0]["tag_name"]
        current_version = __version__

        if current_version < latest_version:
            if messagebox.askyesno("Доступно обновление", "Доступно новое обновление. Хотите установить его?"):
                update_from_github()
    except requests.exceptions.RequestException as e:
        messagebox.showwarning("Ошибка проверки обновлений", str(e))

def calculate_area(round_values):
    total_area = 0
    room_areas = []

    def calculate_click():
        nonlocal total_area, room_areas

        try:
            length = float(length_entry.get())
            length_minus = float(length_minus_entry.get())
            height = float(height_entry.get())
            num_doors = int(doors_entry.get())

            area = (length - length_minus) * height
            door_area = num_doors
            area -= door_area

            if round_values:
                area = round(area, 2)

            total_area = area
            room_areas.append(area)

            total_area_label.configure(text="Общая площадь: {:.2f}".format(total_area))

        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат ввода. Пожалуйста, введите числовое значение.")

    def reset_click():
        nonlocal total_area, room_areas
        total_area = 0
        room_areas = []
        total_area_label.configure(text="Общая площадь:")

    def copy_click():
        result = total_area_label.cget("text")
        result = result.replace("Общая площадь: ", "")
        root.clipboard_clear()
        root.clipboard_append(result)

    def validate_float_input(entry_text):
        try:
            float(entry_text)
            return True
        except ValueError:
            return False

    def validate_int_input(entry_text):
        try:
            int(entry_text)
            return True
        except ValueError:
            return False

    def open_github_link():
        webbrowser.open(REPO_URL)

    def open_window_calculator(event):
        global open_windows_count
        if open_windows_count < 2:
            open_windows_count += 1
            messagebox.showinfo("В разработке...", "Калькулятор окон находится в разработке.")
        else:
            messagebox.showinfo("Ошибка", "Доступно только два окна программы.")

    def open_window_engineering_calculator(event):
        global open_windows_count
        if open_windows_count < 2:
            open_windows_count += 1
            messagebox.showinfo("В разработке...", "Инженерный калькулятор находится в разработке.")
        else:
            messagebox.showinfo("Ошибка", "Доступно только два окна программы.")

    root = tk.CTk()
    root.title("Калькулятор площади помещений")

    tk.set_appearance_mode("Dark")
    tk.set_default_color_theme("blue")

    top_frame = tk.CTkFrame(root)
    top_frame.pack(pady=20)

    length_label = tk.CTkLabel(top_frame, text="Длина помещения:", font=("Arial", 14))
    length_label.pack(anchor="w")

    length_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
    length_entry.pack(fill="x", padx=10)

    length_minus_label = tk.CTkLabel(top_frame, text="Значение длины для вычета:", font=("Arial", 14))
    length_minus_label.pack(anchor="w")

    length_minus_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
    length_minus_entry.insert(tk.END, "0")
    length_minus_entry.pack(fill="x", padx=10)

    height_label = tk.CTkLabel(top_frame, text="Высота помещения:", font=("Arial", 14))
    height_label.pack(anchor="w")

    height_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
    height_entry.pack(fill="x", padx=10)

    doors_label = tk.CTkLabel(top_frame, text="Количество дверей:", font=("Arial", 14))
    doors_label.pack(anchor="w")

    doors_entry = tk.CTkEntry(top_frame, font=("Arial", 14), validate="key")
    doors_entry.configure(validatecommand=(root.register(validate_int_input), "%P"))
    doors_entry.pack(fill="x", padx=10)

    buttons_frame = tk.CTkFrame(root)
    buttons_frame.pack(pady=20)

    calculate_button = tk.CTkButton(buttons_frame, text="Рассчитать", font=("Arial", 14), command=calculate_click)
    calculate_button.pack(side=tk.LEFT, padx=(0, 10))

    reset_button = tk.CTkButton(buttons_frame, text="Сбросить", font=("Arial", 14), command=reset_click)
    reset_button.pack(side=tk.LEFT)

    total_area_label = tk.CTkLabel(root, text="Общая площадь:", font=("Arial", 16, "bold"))
    total_area_label.pack(pady=20)

    copy_button = tk.CTkButton(root, text="Копировать", font=("Arial", 14), command=copy_click)
    copy_button.pack()

    github_link_button = tk.CTkButton(root, text="Сделано QweRez(Eternal V)", font=("Arial", 12), command=open_github_link)
    github_link_button.pack(side=tk.BOTTOM)

    window_calculator_button = tk.CTkButton(root, text="Калькулятор окон", font=("Arial", 14))
    window_calculator_button.pack(anchor="w", pady=20)
    window_calculator_button.bind("<Button-1>", open_window_calculator)

    engineering_calculator_button = tk.CTkButton(root, text="Инженерный калькулятор", font=("Arial", 14))
    engineering_calculator_button.pack(anchor="w")
    engineering_calculator_button.bind("<Button-1>", open_window_engineering_calculator)

    # Проверка обновлений при каждом запуске
    check_updates()

    def on_close():
        global open_windows_count
        open_windows_count -= 1
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    # Получение названия текущего исполняемого файла
    current_file = os.path.basename(sys.argv[0])
    # Замена названия файла на "visual_area_calculator.exe"
    updated_file = current_file.replace(current_file, "visual_area_calculator.exe")
    # Обновление текущего исполняемого файла
    os.rename(current_file, updated_file)
    # Запуск программы с обновленным файлом
    calculate_area(round_values=True)







# pyinstaller -F --noconfirm --onedir --noconsole --add-data "C:\Users\kiril\AppData\Local\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter/" "C:\мусорка\bot\siti\visual_area_calculator.py"
# pyinstaller --noconfirm --onefile --noconsole --add-binary "C:\Users\kiril\AppData\Local\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter/" "C:\мусорка\bot\siti\visual_area_calculator.py"
# pyinstaller --noconfirm --onefile --noconsole --add-binary "C:\Users\kiril\AppData\Local\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter/" "C:\мусорка\bot\siti\visual_area_calculator.py"


import customtkinter as tk
from tkinter import messagebox

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

    def open_github_link():
        import webbrowser
        webbrowser.open("https://github.com/Eternal1of/")

    github_link_button = tk.CTkButton(root, text="Сделано QweRez(Eternal V", font=("Arial", 12), command=open_github_link)
    github_link_button.pack(side=tk.BOTTOM)

    window_calculator_button = tk.CTkButton(root, text="Калькулятор окон", font=("Arial", 14))
    window_calculator_button.pack(anchor="e", pady=20)

    def open_window_calculator(event):
        messagebox.showinfo("В разработке...", "Калькулятор окон находится в разработке.")

    window_calculator_button.bind("<Button-1>", open_window_calculator)

    root.mainloop()

if __name__ == "__main__":
    calculate_area(round_values=True)
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

    def open_calculate_area_window():
        nonlocal length_entry, length_minus_entry, height_entry, doors_entry, total_area_label, calculate_area_window

        if not calculate_area_window:
            calculate_area_window = tk.CTk()
            calculate_area_window.title("Калькулятор площади помещений")
            calculate_area_window.geometry("400x300")
            calculate_area_window.minsize(400, 300)

            top_frame = tk.CTkFrame(calculate_area_window)
            top_frame.pack(pady=20)

            length_label = tk.CTkLabel(top_frame, text="Длина помещения:", font=("Arial", 14))
            length_label.grid(row=0, column=0, sticky="e")

            length_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
            length_entry.grid(row=0, column=1)

            length_minus_label = tk.CTkLabel(top_frame, text="Значение длины для вычета:", font=("Arial", 14))
            length_minus_label.grid(row=1, column=0, sticky="e")

            length_minus_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
            length_minus_entry.insert(tk.END, "0")
            length_minus_entry.grid(row=1, column=1)

            height_label = tk.CTkLabel(top_frame, text="Высота помещения:", font=("Arial", 14))
            height_label.grid(row=2, column=0, sticky="e")

            height_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
            height_entry.grid(row=2, column=1)

            doors_label = tk.CTkLabel(top_frame, text="Количество дверей:", font=("Arial", 14))
            doors_label.grid(row=3, column=0, sticky="e")

            doors_entry = tk.CTkEntry(top_frame, font=("Arial", 14), validate="key")
            doors_entry.configure(validatecommand=(calculate_area_window.register(validate_int_input), "%P"))
            doors_entry.grid(row=3, column=1)

            buttons_frame = tk.CTkFrame(calculate_area_window)
            buttons_frame.pack(pady=20)

            calculate_button = tk.CTkButton(buttons_frame, text="Рассчитать", font=("Arial", 14), command=calculate_click)
            calculate_button.pack(side=tk.LEFT, padx=10)

            reset_button = tk.CTkButton(buttons_frame, text="Сбросить", font=("Arial", 14), command=reset_click)
            reset_button.pack(side=tk.LEFT, padx=10)

            total_area_label = tk.CTkLabel(calculate_area_window, text="Общая площадь:", font=("Arial", 16, "bold"))
            total_area_label.pack()

            copy_button = tk.CTkButton(calculate_area_window, text="Копировать", font=("Arial", 14), command=copy_click)
            copy_button.pack()

            calculate_area_window.protocol("WM_DELETE_WINDOW", close_calculate_area_window)

    def close_calculate_area_window():
        nonlocal calculate_area_window
        calculate_area_window.destroy()
        calculate_area_window = None

    def open_window_calculator():
        messagebox.showinfo("В разработке...", "Калькулятор окон находится в разработке.")

    def open_engineering_calculator():
        messagebox.showinfo("В разработке...", "Инженерный калькулятор находится в разработке.")

    def open_github_link():
        import webbrowser
        webbrowser.open("https://github.com/Eternal1of/")

    root = tk.CTk()
    root.title("Главное меню")
    root.geometry("400x300")
    root.minsize(400, 300)
    tk.set_appearance_mode("Dark")
    tk.set_default_color_theme("blue")


    main_menu_frame = tk.CTkFrame(root)
    main_menu_frame.pack(pady=20)

    calculate_area_button = tk.CTkButton(main_menu_frame, text="Калькулятор площади", font=("Arial", 14), command=open_calculate_area_window)
    calculate_area_button.pack(pady=10)

    window_calculator_button = tk.CTkButton(main_menu_frame, text="Калькулятор окон", font=("Arial", 14), command=open_window_calculator)
    window_calculator_button.pack(pady=10)

    engineering_calculator_button = tk.CTkButton(main_menu_frame, text="Инженерный калькулятор", font=("Arial", 14), command=open_engineering_calculator)
    engineering_calculator_button.pack(pady=10)


    github_link_button = tk.CTkButton(root, text="Сделано QweRez(Eternal V", font=("Arial", 12), command=open_github_link)
    github_link_button.pack(side=tk.BOTTOM)

    length_entry = None
    length_minus_entry = None
    height_entry = None
    doors_entry = None
    total_area_label = None
    calculate_area_window = None

    root.mainloop()

if __name__ == "__main__":
    calculate_area(round_values=True)

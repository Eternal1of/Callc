# TODO: Я затрахался если честно @flaymerr (интересно, пинги работают?)
import customtkinter as tk
import webbrowser

def calculate_area(round_values):
    total_area = 0
    room_areas = []

    def calculate_button_click():
        nonlocal total_area, room_areas

        try:
            room_length = float(room_length_entry.get())
            room_length_minus = float(room_length_minus_entry.get())
            room_height = float(room_height_entry.get())
            num_doors = int(num_doors_entry.get())

            room_area = (room_length - room_length_minus) * room_height
            door_area = num_doors
            room_area -= door_area

            if round_values:
                room_area = round(room_area, 2)

            total_area = room_area
            room_areas.append(room_area)

            total_area_label.configure(text="Общая площадь: {:.2f}".format(total_area))

        except ValueError:
            tk.showerror("Ошибка", "Неверный формат ввода. Пожалуйста, введите числовое значение.")

    def reset_button_click():
        nonlocal total_area, room_areas
        total_area = 0
        room_areas = []
        total_area_label.configure(text="Общая площадь:")

    def copy_button_click():
        result = total_area_label.cget("text")
        result = result.replace("Общая площадь: ", "")
        root.clipboard_clear()
        root.clipboard_append(result)

    def open_link(event):
        webbrowser.open("https://github.com/QweRezOn")

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

    # Применение темной темы
    tk.set_appearance_mode("Dark")
    tk.set_default_color_theme("blue")

    # Создание и размещение виджетов
    top_frame = tk.CTkFrame(root)
    top_frame.pack(side=tk.TOP, pady=20)

    room_length_label = tk.CTkLabel(top_frame, text="Длина помещения:", font=("Arial", 14))
    room_length_label.grid(row=0, column=0, sticky="e")

    room_length_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
    room_length_entry.grid(row=0, column=1)

    room_length_minus_label = tk.CTkLabel(top_frame, text="Значение длины для вычета:", font=("Arial", 14))
    room_length_minus_label.grid(row=1, column=0, sticky="e")

    room_length_minus_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
    room_length_minus_entry.insert(tk.END, "0")  # Установка значения по умолчанию
    room_length_minus_entry.grid(row=1, column=1)

    room_height_label = tk.CTkLabel(top_frame, text="Высота помещения:", font=("Arial", 14))
    room_height_label.grid(row=2, column=0, sticky="e")

    room_height_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
    room_height_entry.grid(row=2, column=1)

    num_doors_label = tk.CTkLabel(top_frame, text="Количество дверей:", font=("Arial", 14))
    num_doors_label.grid(row=3, column=0, sticky="e")

    num_doors_entry = tk.CTkEntry(top_frame, font=("Arial", 14), validate="key")
    num_doors_entry.configure(validatecommand=(root.register(validate_int_input), "%P"))
    num_doors_entry.grid(row=3, column=1)

    buttons_frame = tk.CTkFrame(root)
    buttons_frame.pack(pady=20)

    calculate_button = tk.CTkButton(buttons_frame, text="Рассчитать", font=("Arial", 14), command=calculate_button_click)
    calculate_button.pack(side=tk.LEFT, padx=10)

    reset_button = tk.CTkButton(buttons_frame, text="Сбросить", font=("Arial", 14), command=reset_button_click)
    reset_button.pack(side=tk.LEFT, padx=10)

    total_area_label = tk.CTkLabel(root, text="Общая площадь:", font=("Arial", 16, "bold"))
    total_area_label.pack()

    copy_button = tk.CTkButton(root, text="Копировать", font=("Arial", 14), command=copy_button_click)
    copy_button.pack()

    footer_label = tk.CTkLabel(root, text="Сделано ", font=("Arial", 12))
    footer_label.pack()

    qwerez_link = tk.CTkLabel(root, text="QweRez", font=("Arial", 12, "underline"), cursor="hand2")
    qwerez_link.pack()
    qwerez_link.bind("<Button-1>", open_link)

    root.update()  # Обновление окна для получения актуальных размеров

    # Позиционирование футера в центре нижней части окна
    footer_frame = tk.CTkFrame(root)
    footer_frame.pack(side=tk.BOTTOM, pady=(root.winfo_height() - 100, 20))  # Регулируйте отступы вторым значением

    footer_label.pack(in_=footer_frame, side=tk.LEFT)
    qwerez_link.pack(in_=footer_frame, side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    calculate_area(round_values=True)

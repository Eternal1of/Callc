import customtkinter as tk

# TODO: @flaymerr пидорасина?

def calculate_area(round_values):
    total_area = 0
    room_areas = []

    def calculate_button_click():
        nonlocal total_area, room_areas

        try:
            room_number = int(room_number_entry.get())
            room_length = float(room_length_entry.get())
            room_length_minus = float(room_length_minus_entry.get())
            room_height = float(room_height_entry.get())
            num_doors = int(num_doors_entry.get())

            room_area = (room_length - room_length_minus) * room_height
            door_area = num_doors
            room_area -= door_area

            if round_values:
                room_area = round(room_area, 2)

            total_area += room_area
            room_areas.append(room_area)

            total_area_label.configure(text="Общая площадь: {:.2f}".format(total_area))

        except ValueError:
            tk.messagebox.showerror("Ошибка", "Неверный формат ввода. Пожалуйста, введите числовое значение.")

    def reset_button_click():
        nonlocal total_area, room_areas
        total_area = 0
        room_areas = []
        total_area_label.configure(text="Общая площадь:")

    root = tk.CTk()
    root.title("Калькулятор площади помещений")
    root.geometry("1100x580")

    # Применение темной темы
    root.set_theme("dark")

    # Создание и размещение виджетов
    room_number_label = tk.CTkLabel(root, text="Номер помещения:", font=("Arial", 14))
    room_number_label.pack()

    room_number_entry = tk.CTkEntry(root, font=("Arial", 14))
    room_number_entry.pack()

    room_length_label = tk.CTkLabel(root, text="Длина помещения:", font=("Arial", 14))
    room_length_label.pack()

    room_length_entry = tk.CTkEntry(root, font=("Arial", 14))
    room_length_entry.pack()

    room_length_minus_label = tk.CTkLabel(root, text="Значение длины для вычета:", font=("Arial", 14))
    room_length_minus_label.pack()

    room_length_minus_entry = tk.CTkEntry(root, font=("Arial", 14))
    room_length_minus_entry.pack()

    room_height_label = tk.CTkLabel(root, text="Высота помещения:", font=("Arial", 14))
    room_height_label.pack()

    room_height_entry = tk.CTkEntry(root, font=("Arial", 14))
    room_height_entry.pack()

    num_doors_label = tk.CTkLabel(root, text="Количество дверей:", font=("Arial", 14))
    num_doors_label.pack()

    num_doors_entry = tk.CTkEntry(root, font=("Arial", 14))
    num_doors_entry.pack()

    calculate_button = tk.CTkButton(root, text="Рассчитать", font=("Arial", 14), command=calculate_button_click)
    calculate_button.pack()

    reset_button = tk.CTkButton(root, text="Сбросить", font=("Arial", 14), command=reset_button_click)
    reset_button.pack()

    total_area_label = tk.CTkLabel(root, text="Общая площадь:", font=("Arial", 16, "bold"))
    total_area_label.pack()

    root.mainloop()


if __name__ == "__main__":
    calculate_area(round_values=True)

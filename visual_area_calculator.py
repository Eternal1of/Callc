import customtkinter as tk

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
    root.geometry("400x300")

    # Создание и размещение виджетов
    room_number_label = tk.CTkLabel(root, text="Номер помещения:")
    room_number_label.pack()

    room_number_entry = tk.CTkEntry(root)
    room_number_entry.pack()

    room_length_label = tk.CTkLabel(root, text="Длина помещения:")
    room_length_label.pack()

    room_length_entry = tk.CTkEntry(root)
    room_length_entry.pack()

    room_length_minus_label = tk.CTkLabel(root, text="Значение длины для вычета:")
    room_length_minus_label.pack()

    room_length_minus_entry = tk.CTkEntry(root)
    room_length_minus_entry.pack()

    room_height_label = tk.CTkLabel(root, text="Высота помещения:")
    room_height_label.pack()

    room_height_entry = tk.CTkEntry(root)
    room_height_entry.pack()

    num_doors_label = tk.CTkLabel(root, text="Количество дверей:")
    num_doors_label.pack()

    num_doors_entry = tk.CTkEntry(root)
    num_doors_entry.pack()

    calculate_button = tk.CTkButton(root, text="Рассчитать", command=calculate_button_click)
    calculate_button.pack()

    reset_button = tk.CTkButton(root, text="Сбросить", command=reset_button_click)
    reset_button.pack()

    total_area_label = tk.CTkLabel(root, text="Общая площадь:")
    total_area_label.pack()

    root.mainloop()


if __name__ == "__main__":
    calculate_area(round_values=True)

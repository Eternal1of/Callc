import datetime

# Запрос варианта запуска у пользователя
option = int(input("Выберите вариант запуска (0 - ввод данных в консоль, 1 - чтение данных из файла, 2 - автоматический): "))

if option == 0 or option == 1:
    # Не создавать экземпляр AutoCAD
    pass

elif option == 2:
    try:
        import win32com.client

        # Попытка получить существующий экземпляр AutoCAD
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
        # Получение активного документа
        doc = acad.ActiveDocument
        # Получение модели пространства модели
        msp = doc.ModelSpace

    except:
        # Создание экземпляра AutoCAD, если не удалось получить существующий
        acad = win32com.client.Dispatch("AutoCAD.Application")
        # Ожидание, чтобы AutoCAD успел запуститься полностью
        acad.Visible = True
        acad.WindowState = 1  # Развернуть окно AutoCAD на весь экран
        doc = acad.ActiveDocument
        # Получение модели пространства модели
        msp = doc.ModelSpace

else:
    print("Неверный вариант запуска.")
    exit()
# TODO@flaymerr
def calculate_area():
    total_area = 0
    room_areas = []  # Список для хранения площадей помещений

    # Запрос у пользователя ввода данных
    room_number = input("Введите номер помещения (номер комнаты): ")
    room_length = float(input("Введите длину помещения: "))
    room_length_minus = float(input("Введите значение длины, которое нужно отнять от длины стены: "))
    room_height = float(input("Введите высоту помещения: "))
    num_doors = int(input("Введите количество дверей в помещении: "))

    # Вычисление площади помещения
    room_area = (room_length - room_length_minus) * room_height

    # Вычитание площади дверей
    door_area = num_doors  # Площадь одной двери равна 1 метру
    room_area -= door_area

    total_area += room_area
    room_areas.append(room_area)

    return total_area, room_areas

# Подсчет площади
total_area, room_areas = calculate_area()

# Вывод общей площади
print("Общая площадь:", total_area)

# Запрос создания файла upd(время на компьютере windows 10).txt
create_file = input("Создать файл upd(время на компьютере windows 10).txt? (y/n): ")

if create_file.lower() == "y":
    # Получение текущего времени на компьютере Windows 10
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"upd({current_time}).txt"

    # Создание и запись в файл
    with open(file_name, "a") as file:
        file.write(f"Общая площадь: {total_area}\n")
        for i, room_area in enumerate(room_areas, 1):
            file.write(f"Помещение {i}  {room_area} ")

    print(f"Файл {file_name} создан.")

# Запрос на повторный расчёт
calculate_again = input("Желаете выполнить повторный расчёт? (y/n): ")

while calculate_again.lower() == "y":
    # Повторный расчёт площади
    new_total_area, new_room_areas = calculate_area()

    # Добавление результатов к общей площади и списку площадей помещений
    total_area += new_total_area
    room_areas.extend(new_room_areas)

    # Вывод общей площади
    print("Общая площадь:", total_area)

    # Запрос на повторный расчёт
    calculate_again = input("Желаете выполнить повторный расчёт? (y/n): ")

# Завершение программы
print("Программа завершена.")

import datetime
import configparser
import os

def calculate_area(round_values):
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

    if round_values:
        room_area = round(room_area, 2)

    total_area += room_area
    room_areas.append(room_area)

    return total_area, room_areas

def create_file(total_area, room_areas):
    # Получение текущего времени на компьютере Windows 10
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"upd({current_time}).txt"

    # Запись в файл в нужном порядке
    with open(file_name, "a") as file:
        file.write(f"№(номер помещения) S(площадь помещения)\n")
        for i, room_area in enumerate(room_areas, 1):
            file.write(f"{i} {room_area}\n")

    print(f"Файл {file_name} создан.")

def run_calculation(round_values):
    total_area = 0
    room_areas = []

    while True:
        # Подсчет площади
        new_total_area, new_room_areas = calculate_area(round_values)

        # Добавление результатов к общей площади и списку площадей помещений
        total_area += new_total_area
        room_areas.extend(new_room_areas)

        # Вывод общей площади
        print("Общая площадь:", total_area)

        # Запрос на повторный расчёт
        calculate_again = input("Желаете выполнить повторный расчёт? (y/n): ")

        if calculate_again.lower() != "y":
            break

    # Запрос создания файла upd(время на компьютере windows 10).txt
    create_file_input = input("Создать файл upd(время на компьютере windows 10).txt? (y/n): ")

    if create_file_input.lower() == "y":
        create_file(total_area, room_areas)

    print("Программа завершена.")

def read_configuration():
    config = configparser.ConfigParser()
    if os.path.exists("conf.ini"):
        config.read("conf.ini")
        round_values = config.getboolean("Settings", "RoundValues")
    else:
        round_values = ask_rounding_preference()
        config["Settings"] = {"RoundValues": str(round_values)}
        with open("conf.ini", "w") as config_file:
            config.write(config_file)
    return round_values

def ask_rounding_preference():
    rounding_preference = input("Хотите округлять значения до сотых? (y/n): ")
    if rounding_preference.lower() == "y":
        return True
    else:
        return False

# Не создавать экземпляр AutoCAD
round_values = read_configuration()
run_calculation(round_values)

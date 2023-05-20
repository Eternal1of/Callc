import configparser
import os

def calculate_area(round_values):
    total_area = 0
    room_areas = []

    while True:
        try:
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

            # Вывод общей площади
            print("Общая площадь:", total_area)

            # Запрос на повторный расчет
            calculate_again = input("Желаете выполнить повторный расчет? (y/n): ")

            if calculate_again.lower() != "y":
                break
        except ValueError:
            print("Ошибка: неверный формат ввода. Пожалуйста, введите числовое значение.")

        except KeyboardInterrupt:
            print("Программа прервана пользователем.")

    return total_area, room_areas

def create_file(total_area, room_areas):
    file_name = "upd.txt"

    # Запись в файл в нужном порядке
    with open(file_name, "a") as file:
        for i, room_area in enumerate(room_areas, 1):
            file.write(f"{i} {room_area}\n")

    print(f"Файл {file_name} обновлен.")

def run_calculation(round_values):
    total_area = 0
    room_areas = []

    while True:
        try:
            # Подсчет площади
            new_total_area, new_room_areas = calculate_area(round_values)

            # Добавление результатов к общей площади и списку площадей помещений
            total_area += new_total_area
            room_areas.extend(new_room_areas)

            # Запрос на повторный расчет
            calculate_again = input("Желаете выполнить повторный расчет? (y/n): ")

            if calculate_again.lower() != "y":
                break
        except KeyboardInterrupt:
            print("Программа прервана пользователем.")

    # Запрос создания файла upd.txt
    while True:
        try:
            create_file_input = input("Создать/обновить файл upd.txt? (y/n): ")

            if create_file_input.lower() == "y":
                create_file(total_area, room_areas)
            break
        except IOError:
            print("Ошибка: не удалось создать/обновить файл upd.txt.")

    print("Программа завершена.")

def read_configuration():
    config = configparser.ConfigParser()
    if os.path.exists("settings/conf.ini"):
        config.read("settings/conf.ini")
        round_values = config.getboolean("Settings", "RoundValues")
    else:
        round_values = ask_rounding_preference()
        config["Settings"] = {"RoundValues": str(round_values)}
        os.makedirs("settings", exist_ok=True)
        with open("settings/conf.ini", "w") as config_file:
            config.write(config_file)
    return round_values

def ask_rounding_preference():
    while True:
        try:
            rounding_preference = input("Хотите округлять значения до сотых? (y/n): ")
            if rounding_preference.lower() == "y":
                return True
            elif rounding_preference.lower() == "n":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Ошибка: неверный формат ввода. Пожалуйста, введите 'y' или 'n'.")

round_values = read_configuration()
run_calculation(round_values)

def save_settings(round_values):
    config = configparser.ConfigParser()
    config["Settings"] = {"RoundValues": str(round_values)}
    with open("settings/conf.ini", "w") as config_file:
        config.write(config_file)
    print("Настройки сохранены.")


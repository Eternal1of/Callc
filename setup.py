import os
import subprocess

# Увеличение версии
def increment_version(version):
    major, minor, patch = version.split(".")
    patch = str(int(patch) + 1)
    new_version = ".".join([major, minor, patch])
    return new_version

# Получение текущей версии
def get_current_version():
    with open("visual_area_calculator.py", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "__version__" in line:
                version = line.split("=")[1].strip().strip('"')
                return version

    return None

# Обновление файла с новой версией
def update_version_file(new_version):
    with open("visual_area_calculator.py", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if "__version__" in line:
                line = f'__version__ = "{new_version}"\n'
            file.write(line)
        file.truncate()

# Запуск процесса с помощью PyInstaller
def run_pyinstaller():
    command = 'pyinstaller --noconfirm --onefile --noconsole --add-binary "C:\Users\kiril\AppData\Local\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter/" "C:\мусорка\bot\siti\visual_area_calculator.py"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

if __name__ == "__main__":
    # Получение текущей версии
    current_version = get_current_version()
    if current_version is None:
        print("Ошибка: Не удалось найти текущую версию.")
        exit(1)

    # Увеличение версии
    new_version = increment_version(current_version)

    # Обновление файла с новой версией
    update_version_file(new_version)

    # Запуск процесса PyInstaller
    stdout, stderr = run_pyinstaller()

    # Вывод результатов
    if stdout:
        print(stdout)
    if stderr:
        print(stderr)
        print("Ошибка: Возникла ошибка при создании исполняемого файла.")
        exit(1)

    print("Успешно: Исполняемый файл успешно создан.")

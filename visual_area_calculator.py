from tkinter import messagebox
import requests, webbrowser, git, os, sys
from distutils.version import LooseVersion
import customtkinter as tk

__version__ = "0.0.7"

REPO_URL = "https://github.com/Eternal1of/Callc"
RELEASES_URL = "https://api.github.com/repos/Eternal1of/Callc/releases/latest"

class AreaCalculator:
    def __init__(self):
        self.root = tk.CTk()
        self.total_area = 0
        self.room_areas = []
        self.open_windows_count = 0

        self.root.title("Калькулятор площади помещений")
        tk.set_appearance_mode("Dark")
        tk.set_default_color_theme("blue")

        self.create_widgets()
        self.check_updates()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def create_widgets(self):
        top_frame = tk.CTkFrame(self.root)
        top_frame.pack(pady=20)

        length_label = tk.CTkLabel(top_frame, text="Длина помещения:", font=("Arial", 14))
        length_label.pack(anchor="w")

        self.length_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
        self.length_entry.pack(fill="x", padx=10)

        length_minus_label = tk.CTkLabel(top_frame, text="Значение длины для вычета:", font=("Arial", 14))
        length_minus_label.pack(anchor="w")

        self.length_minus_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
        self.length_minus_entry.insert(tk.END, "0")
        self.length_minus_entry.pack(fill="x", padx=10)

        height_label = tk.CTkLabel(top_frame, text="Высота помещения:", font=("Arial", 14))
        height_label.pack(anchor="w")

        self.height_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
        self.height_entry.pack(fill="x", padx=10)

        doors_label = tk.CTkLabel(top_frame, text="Количество дверей:", font=("Arial", 14))
        doors_label.pack(anchor="w")

        self.doors_entry = tk.CTkEntry(top_frame, font=("Arial", 14))
        self.doors_entry.pack(fill="x", padx=10)

        buttons_frame = tk.CTkFrame(self.root)
        buttons_frame.pack(pady=20)

        calculate_button = tk.CTkButton(buttons_frame, text="Рассчитать", font=("Arial", 14), command=self.calculate_click)
        calculate_button.pack(side=tk.LEFT, padx=(0, 10))

        reset_button = tk.CTkButton(buttons_frame, text="Сбросить", font=("Arial", 14), command=self.reset_click)
        reset_button.pack(side=tk.LEFT)

        self.total_area_label = tk.CTkLabel(self.root, text="Общая площадь:", font=("Arial", 16, "bold"))
        self.total_area_label.pack(pady=20)

        copy_button = tk.CTkButton(self.root, text="Копировать", font=("Arial", 14), command=self.copy_click)
        copy_button.pack()

        github_link_button = tk.CTkButton(self.root, text="Сделано QweRez(Eternal V)", font=("Arial", 12), command=self.open_github_link)
        github_link_button.pack(side=tk.BOTTOM, pady=20)

        window_calculator_button = tk.CTkButton(self.root, text="Калькулятор окон", font=("Arial", 14))
        window_calculator_button.pack(anchor="center", pady=20)
        window_calculator_button.bind("<Button-1>", self.open_window_calculator)

        engineering_calculator_button = tk.CTkButton(self.root, text="Инженерный калькулятор", font=("Arial", 14))
        engineering_calculator_button.pack(anchor="center")
        engineering_calculator_button.bind("<Button-1>", self.open_window_engineering_calculator)

    def check_updates(self):
        try:
            response = requests.get(RELEASES_URL)
            response.raise_for_status()
            release_info = response.json()

            if release_info and "tag_name" in release_info:
                latest_version = release_info["tag_name"]
                current_version = __version__

                if LooseVersion(current_version) < LooseVersion(latest_version):
                    if messagebox.askyesno("Доступно обновление", "Доступно новое обновление. Хотите установить его?"):
                        self.update_from_github()
            else:
                messagebox.showwarning("Ошибка проверки обновлений", "Не удалось получить информацию о релизах.")
        except requests.exceptions.RequestException as e:
            messagebox.showwarning("Ошибка проверки обновлений", str(e))

    def update_from_github(self):
        try:
            repo = git.Repo(".")
            repo.remotes.origin.pull()
            messagebox.showinfo("Обновление", "Приложение было успешно обновлено.")
            python = sys.executable
            os.execl(python, python, *sys.argv)
        except git.exc.GitCommandError as e:
            messagebox.showerror("Ошибка обновления", str(e))

    def calculate_click(self):
        try:
            length = float(self.length_entry.get())
            length_minus = float(self.length_minus_entry.get())
            height = float(self.height_entry.get())
            num_doors = int(self.doors_entry.get())

            area = (length - length_minus) * height
            door_area = num_doors * 1  # Измените 1 на фактическую площадь двери
            area -= door_area

            area = round(area, 2)
            self.total_area = area
            self.room_areas.append(area)

            self.total_area_label.configure(text="Общая площадь: {:.2f}".format(self.total_area))
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат ввода. Пожалуйста, введите числовое значение.")

    def reset_click(self):
        self.length_entry.delete(0, tk.END)
        self.length_minus_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.doors_entry.delete(0, tk.END)
        self.total_area = 0
        self.room_areas = []
        self.total_area_label.configure(text="Общая площадь:")

    def copy_click(self):
        result = self.total_area_label.cget("text")
        result = result.replace("Общая площадь: ", "")
        self.root.clipboard_clear()
        self.root.clipboard_append(result)

    def validate_int_input(self, entry_text):
        try:
            int(entry_text)
            return True
        except ValueError:
            return False

    def open_github_link(self):
        webbrowser.open(REPO_URL)

    def open_window_calculator(self, event):
        if self.open_windows_count < 2:
            self.open_windows_count += 1
            messagebox.showinfo("В разработке...", "Калькулятор окон находится в разработке.")
        else:
            messagebox.showinfo("Ошибка", "Доступно только два окна программы.")

    def open_window_engineering_calculator(self, event):
        if self.open_windows_count < 2:
            self.open_windows_count += 1
            engineering_calculator = EngineeringCalculator()
            self.root.destroy()
        else:
            messagebox.showinfo("Ошибка", "Доступно только два окна программы.")

    def on_close(self):
        self.open_windows_count -= 1
        self.root.destroy()

    def run(self):
        self.root.mainloop()



class EngineeringCalculator:
    def __init__(self):
        self.root = tk.CTk()
        self.root.title("Инженерный калькулятор")
        
        # Добавьте код для создания виджетов и функциональности инженерного калькулятора
        
        self.root.mainloop()


if __name__ == "__main__":
    app = AreaCalculator()
    app.run()

from modules import app_obj
from modules.window import MainWindow


def main():
    try:
        main_window = MainWindow(window_width=1200, window_height=800)
        main_window.show()
        app_obj.exec()
    except Exception as error:
        print(f"Помилка під час запуску проєкту: {error}")


if __name__ == "__main__":
    main()

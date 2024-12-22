import os
import shutil


def move_photos():
    # Указываем директории
    source_dir = "/Users/admin/Code/parsers/telegram-images/"
    target_dir = "../web-tgchat-checker/img"  # Adjust target path if needed
    file_list_path = "uncommitted.txt"  # Path to the uncommitted file list

    # Проверяем, существуют ли исходная и целевая папки
    if not os.path.exists(source_dir):
        print(f"Источник {source_dir} не найден.")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Проверяем, существует ли файл со списком
    if not os.path.exists(file_list_path):
        print(f"Файл со списком {file_list_path} не найден.")
        return

    # Считываем список файлов из uncommitted.txt
    with open(file_list_path, "r") as f:
        files = [line.strip() for line in f.readlines()]

    # Проверяем, есть ли файлы для переноса
    if not files:
        print("Нет файлов для переноса.")
        return

    # Переносим файлы из списка
    print(f"Найдено {len(files)} файлов для переноса.")
    for file in files:
        # Создаем полный путь до исходного файла
        source_path = os.path.join(source_dir, file)
        target_path = os.path.join(target_dir, os.path.basename(file))  # Ensure only the filename is used

        # Печать пути для отладки
        print(f"Проверка пути: {source_path}")

        try:
            if os.path.exists(source_path):  # Проверяем, существует ли файл
                shutil.move(source_path, target_path)
                print(f"Перемещён файл: {file}")
            else:
                print(f"Файл не найден: {source_path}")
        except Exception as e:
            print(f"Ошибка при перемещении файла {file}: {e}")


if __name__ == "__main__":
    move_photos()

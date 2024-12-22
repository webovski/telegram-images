import os

def generate_html():
    # Путь к папке с картинками
    images_dir = "../telegram-images/all"

    # Шаблон URL для картинок
    base_url = "https://raw.githubusercontent.com/webovski/telegram-images/refs/heads/main/all/"

    # Проверяем, существует ли папка
    if not os.path.exists(images_dir):
        print(f"Папка {images_dir} не найдена.")
        return

    # Получаем список файлов с расширением .jpg
    images = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

    # Генерируем HTML-код
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Grid</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin: 0;
            padding: 0;
        }
        .image-tile {
            width: 50px;
            height: 50px;
            margin: 2px;
            background-size: cover;
            background-position: center;
        }
    </style>
</head>
<body>
"""

    for image in images:
        image_url = base_url + image
        html_content += f'<div class="image-tile" style="background-image: url({image_url});"></div>'

    html_content += """
</body>
</html>
"""

    # Сохраняем HTML в файл
    output_file = "image_grid.html"
    with open(output_file, "w") as file:
        file.write(html_content)

    print(f"HTML-файл создан: {output_file}")

if __name__ == "__main__":
    generate_html()

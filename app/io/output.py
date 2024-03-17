def output_to_console(text):
    """
        Функція для виводу тексту у консоль.

        Args:
            text (str): Текст, який потрібно вивести.
        """
    print(text)


def write_to_file(content, filename):
    """
        Функція для запису до файлу за допомогою вбудованих можливостей Python.

        Args:
            content (str): Вміст, який потрібно записати до файлу.
            filename (str): Шлях до файлу, в який потрібно записати.

        Returns:
            None
        """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Дані було записано до файлу '{filename}'.")
    except IOError:
        print(f"Не вдалося записати до файлу '{filename}'.")

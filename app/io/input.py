import pandas as pd


def input_text():
    """
        Функція для вводу тексту з консолі.

        Returns:
            str: Введений користувачем текст.
        """

    text = input("Введіть текст: ")
    return text


def read_from_file(filename):
    """
        Функція для зчитування з файлу за допомогою вбудованих можливостей Python.

        Args:
            filename (str): Шлях до файлу, з якого потрібно зчитати.

        Returns:
            str: Вміст файлу.
                None, якщо файл не знайдено.
        """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None


def read_with_pandas(filename):
    """
        Функція для зчитування з файлу за допомогою бібліотеки pandas.

        Args:
            filename (str): Шлях до файлу, з якого потрібно зчитати.

        Returns:
            pandas.DataFrame: Об'єкт DataFrame з вмістом файлу.
                None, якщо файл не знайдено або не може бути зчитаний.
        """
    try:
        data = pd.read_csv(filename)  # Припустимо, що це CSV файл
        return data
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None

from app.io.input import input_text, read_from_file, read_with_pandas
from app.io.output import output_to_console, write_to_file


def main():
    # 4.1.1 input_text function
    text = input_text()

    output_to_console("Введений текст з консолі:")
    output_to_console(text)

    write_to_file(text, "data/output1.txt")

    # 4.1.2 read_from_file function
    file_content = read_from_file("input.txt")

    output_to_console("\nЗміст файлу 'input.txt':")
    output_to_console(file_content)

    write_to_file(file_content, "data/output2.txt")

    # 4.1.3 read_with_pandas function
    df = read_with_pandas("input.csv")

    output_to_console("\nПерші рядки DataFrame:")
    output_to_console(df.to_string())

    write_to_file(df.to_string(), "data/output_3.txt")


if __name__ == "__main__":
    main()

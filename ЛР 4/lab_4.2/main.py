import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        reader = csv.reader(f, delimiter=",")
        output_value = []

        """Получаем список названий столбцов"""
        for row in reader:
            names = row
            break

        """Заполняем столбцы данными"""
        for row in reader:
            output_value.append({})
            for i in range(len(names)):
                output_value[-1][names[i]] = row[i]

    """Сериализуем данные в json файл"""
    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(output_value, f, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

""" Главный файл для запуска приложения """

import argparse
from tabulate import tabulate
from prettytable import PrettyTable

from csv_processor import aggregate_data, filter_data
from function.functions import read_csv


def main():
    """
    Главная функция приложения.
    Обрабатывает CSV-файл с помощью фильтрации и агрегации.
    """
    # Парсер для аргументов командной строки
    parser = argparse.ArgumentParser(
        description='Обработка CSV-файла с помощью фильтрации и агрегации.'
    )

    # Путь к CSV-файлу
    parser.add_argument('file', help='Путь к CSV-файлу')

    # Аргумент для фильтрации
    parser.add_argument(
        '--filter',
        nargs=3,
        metavar=('COLUMN', 'OP', 'VALUE'),
        help='Фильтрация: COLUMN OP VALUE (например: price > 100)'
    )

    # Аргумент для агрегации
    parser.add_argument(
        '--aggregate',
        metavar='COLUMN',
        help='Агрегация: COLUMN (например: price)'
    )

    args = parser.parse_args()
    data = read_csv(args.file)

    # Обработка фильтрации
    if args.filter:
        column, operator, value = args.filter
        filtered_data = filter_data(
            data,
            column,
            operator,
            value
        )
        print(
            tabulate(filtered_data,
                     headers='keys',
                     tablefmt='pretty')
        )

    # Обработка агрегации
    if args.aggregate:
        column = args.aggregate
        result = aggregate_data(data, column)

        table = PrettyTable()
        table.field_names = [
            f"Показатель {column}",
            f"Значение {column}"
        ]
        table.add_row(["Среднее", f"{result['average']:.2f}"])
        table.add_row(["Минимум", f"{result['min']:.2f}"])
        table.add_row(["Максимум", f"{result['max']:.2f}"])
        table.add_row(["Всего значений", f"{result['total']}"])

        print(f'Агрегация по колонке {column}:')
        print(table)


if __name__ == '__main__':
    main()

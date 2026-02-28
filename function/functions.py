""" Дополнительные функции для работы с CSV """

import csv
from typing import List, Dict, Any


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает данные в виде списка словарей.

    Аргументы:
        file_path: Путь к CSV-файлу.

    Возвращает:
        Список словарей с данными из файла.
    """

    try:
        with open(
            file_path,
            mode='r',
            encoding='utf-8'
        ) as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    except FileNotFoundError:
        print(
            f"Ошибка: Файл '{file_path}' не найден. "
            f"Проверьте, существует ли указанный путь"
        )
        return []

    except IsADirectoryError:
        print(
            f"Ошибка: '{file_path}' - это директория, "
            f"а не файл. Укажите путь к файлу"
        )
        return []

    except csv.Error as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


def determine_type(value: Any) -> str:
    """
    Определяет тип переданного значения.

    Аргументы:
        value: Значение для проверки.

    Возвращает:
        'number' если значение числовое, иначе 'string'.
    """
    try:
        float(value)
        return "number"
    except (ValueError, TypeError):
        return "string"

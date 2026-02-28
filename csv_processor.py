""" Логика фильтрации и агрегации данных """

from typing import List, Dict, Any

from function.functions import determine_type


def filter_data(
    data: List[Dict[str, Any]],
    column: str,
    operator: str,
    value: Any
) -> List[Dict[str, Any]]:
    """
    Фильтрует данные по заданным условиям.

    Аргументы:
        data: Список словарей с данными.
        column: Название колонки для фильтрации.
        operator: Оператор фильтрации ('==', '>', '<').
        value: Значение для фильтрации.

    Возвращает:
        Список отфильтрованных словарей.
    """

    filtered = []
    for row in data:
        try:
            row_value = row[column]

            # Определяем тип переданного значения
            comparison_type = determine_type(value)

            # Приводим value к нужному типу
            if comparison_type == "number":
                row_value = float(row_value)
                value = float(value)
            else:
                row_value = str(row_value)
                value = str(value)

            # Фильтрация по оператору
            if operator == '==':
                if row_value == value:
                    filtered.append(row)

            elif operator == '>':
                if row_value > value:
                    filtered.append(row)

            elif operator == '<':
                if row_value < value:
                    filtered.append(row)

        except (ValueError, KeyError) as k:
            print(f"Ошибка: {k} в строке {row}")

    return filtered


def aggregate_data(data: List[Dict[str, Any]], column: str) -> Dict[str, Any]:
    """
    Выполняет агрегацию данных по указанной колонке.

    Аргументы:
        data: Список словарей с данными.
        column: Название колонки для агрегации.

    Возвращает:
        Словарь со статистикой: среднее, минимум, максимум, количество.
    """
    values = []

    for row in data:
        try:
            if column in row:
                # Пробуем преобразовать в число
                if isinstance(row[column], (int, float)):
                    value = float(row[column])
                    values.append(value)

                elif isinstance(row[column], str) \
                        and row[column].replace('.', '', 1).isdigit():
                    value = float(row[column])
                    values.append(value)

                else:
                    continue

        except (ValueError, KeyError) as e:
            print(f"Ошибка при обработке строки {row}: {e}")

    # Проверяем есть ли данные для агрегации
    if not values:
        print("Нет данных для агрегации")
        return {
            'average': None,
            'min': None,
            'max': None,
            'total': None
        }

    # Вычисляем статистику
    average = sum(values) / len(values)
    minimum = min(values)
    maximum = max(values)
    total_values = len(values)

    return {
        'average': average,
        'min': minimum,
        'max': maximum,
        'total': total_values
    }

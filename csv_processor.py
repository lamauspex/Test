
""" Догика фильтрации и агрегации данных """

from typing import List, Dict, Any

from function.functions import determine_type


# Фу-ия для фильтрации данных
def filter_data(data: List[Dict[str, Any]], column: str, operator: str, value: Any) -> List[Dict[str, Any]]:
    """
    Фильтрует данные по заданным условиям:

    data: Список словарей с данными.
    column: Название колонки для фильтрации.
    operator: Оператор фильтрации ('==', '>', '<').
    value: Значение для фильтрации.
    """

    filtered = []  # список данных
    for row in data:
        try:
            row_value = row[column]
            
            # Определяем тип значения в колонке
            complarison_type = determine_type(value)
            
            # Приводим value к нужному типу
            if complarison_type == "number":
                row_value = float(row_value)
                value = float(value)
            else:
                row_value = str(row_value)
                value = str(value)
            
            # Фильтрация
            if operator == '==':
                if row_value == value: # Сравниваем для равенства
                    filtered.append(row)
                    
            elif operator == '>':
                if row_value > value:  # Сравниваем на больше
                    filtered.append(row)
            
            elif operator == '<':
                if row_value < value:  # Сравниваем на меньше
                    filtered.append(row)
        
        except (ValueError, KeyError) as k:
            print(f"Ошибка: {k} в строке {row}")  
      
    return filtered  # Возвращаем отфильтрованные данные



# Фу-ия для агрегации данных
def aggregate_data(data: List[Dict[str, Any]], column: str) -> Any:
    """
    Выполняет агрегацию данных по указанному типу:

    data: Список словарей с данными.
    column: Название колонки для агрегации.
    """
    values = []
    
    for row in data:
        
        try:
            if column in row:
                # Определяем тип значения в колонке
                if isinstance(row[column], (int, float)):
                    value = float(row[column])  
                    values.append(value)
                
                elif isinstance(row[column], str) and row[column].replace('.', '', 1).isdigit():
                    value = float(row[column])
                    values.append(value)
                
                else:
                    continue
                
        except (ValueError, KeyError) as e:
            print(f"Ошибка при обработке строки {row}: {e}")

    
    # Проверяем есть ли данные
    if not values:
        print("Нет данных для агрегации")
        return {
            'average': None,
            'min': None,
            'max': None,
            'total': None
        }
    
    # Выполняем агрегацию в зависимости от типа
    average = sum(values) / len(values)  # Среднее 
    minimum = min(values)                # Минимум
    maximum = max(values)                # Максимум
    total_values = len(values)           # Всего значений
    
    return {
            'average': average,
            'min': minimum,
            'max': maximum,
            'total': total_values
    }

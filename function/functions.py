
""" Назначение: доп. фу-ии """

import csv
from typing import List, Dict, Any

 
# Фу-ия для чтения CSV-файла
def read_csv(file_path: str) -> List[Dict[str,Any]]:
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file) 
            return [row for row in reader]
    
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден. Проверьте, существует ли указанный путь")
        return []
    
    except IsADirectoryError:
        print("Ошибка: '{file_path}' - это директория, а не файл. Укажите путь к файлу")
        return []
    
    except csv.Error as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


# Определяет тип значения: 'str' или 'number'
def determine_type(value:Any) -> str:
    try:
        float(value)
        return "number"
    except (ValueError, TypeError):
        return "string"

""" Главный файл для запуска: обработка CSV """

import argparse 
from tabulate import tabulate
from prettytable import PrettyTable

from csv_processor import aggregate_data, filter_data
from function.functions import read_csv


# Главная фу-ия
def main():
    # Парсер для аргументов командной строки
    parser = argparse.ArgumentParser(description='Обработайтка CSV-файла с помощью фильтрации и агрегации.')
    
    # Путь к CSV-файлу
    parser.add_argument('file', help='Path to the CSV file') 
    
    # Аргумент для фильтрации
    parser.add_argument(
        '--filter', 
        nargs=3, 
        metavar=('COLUMN', 'OP', 'VALUE'), 
        help='Фильтрация (COLUMN OP VALUE)') 
    
    # Аргумент для агрегации
    parser.add_argument(
        '--aggregate',
        #type=str, 
        metavar='COLUMN', 
        help='Аагрегация (COLUMN )'
        )  
    
    args = parser.parse_args()  
    data = read_csv(args.file) 


    # Если указаны аргументы для фильтрации
    if args.filter:
        column, operator, value = args.filter                              # Извлекаем аргументы 
        filtered_data = filter_data(data, column, operator, value)         # Фильтруем 
        print(tabulate(filtered_data, headers='keys', tablefmt='pretty'))  # Выводим результат
    
    
    # Если указаны аргументы для агрегации
    if args.aggregate:
        column = args.aggregate                       # Извлекаем аргументы 
        result = aggregate_data(data, column)         # Выполняем агрегацию
        
        table = PrettyTable()
        table.field_names = [(f"Показатель {column}"), (f"Значение {column}")]
        table.add_row(["Среднее", f"{result['average']:.2f}"])
        table.add_row(["Минимум", f"{result['min']:.2f}"])
        table.add_row(["Максимум", f"{result['max']:.2f}"])
        table.add_row(["Всего Значений", f"{result['total']:.2f}"])
        
        # Выводим результат 
        print(f'Агрегация по колонке {column}*:') 
        print(table)



# Запускаем главную функцию 
if __name__ == '__main__':
    main()

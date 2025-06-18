
from csv_processor import aggregate_data



# Проверка агрегации данных в колонке с числовыми значениями
def test_aggregate_data_valid():
    data = [{'price': 10}, {'price': 20}, {'price': 30}]
    result = aggregate_data(data, 'price')
    assert result['average'] == 20
    assert result['min'] == 10
    assert result['max'] == 30
    assert result['total'] == 3


# Проверка, что при отсутствии данных возвращаются None для всех показателей
def test_aggregate_data_no_values():
    data = []
    result = aggregate_data(data, 'price')
    assert result['average'] is None
    assert result['min'] is None
    assert result['max'] is None
    assert result['total'] is None


# Проверка ошибки
def test_aggregate_data_key_error():
    data = [{'price': '10'}, {'price': '20'}, {'price': '30'}]
    assert ('Ошибка при обработке строки {row}: {e}')

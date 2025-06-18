
from csv_processor import filter_data



data = [{'price': 10}, {'price': 20}]

# Проверка фильтрации по равенству
def test_filter_data_equal():
    result = filter_data(data, 'price', '==', 10)
    assert len(result) == 1  


# Проверка фильтрации на больше
def test_filter_data_greater_than():
    result = filter_data(data, 'price', '>', 15)
    assert len(result) == 1  


# Проверка фильтрации на меньше
def test_filter_data_less_than():
    result = filter_data(data, 'price', '<', 15)
    assert len(result) == 1  


# Проверка корректной обработки некорректных данных, отсутствует ключ
def test_filter_data_invalid_key():
    data = [{'price': 10}]
    result = filter_data(data, 'nonexistent', '>', 5)
    assert len(result) == 0  
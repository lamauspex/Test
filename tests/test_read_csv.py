
from function.functions import read_csv



# Тесты для проверки базы
def test_read_csv_valid():
    data = read_csv('data/version_csv.csv')
    assert len(data) > 0


# Проверка на ошибку при отсутствии файла
def test_none_file():
    data = read_csv('data/nonexistent_file.csv')
    assert  data == []


# Проверка на ошибку, если указанный путь — это директория, а не файл
def test_directory_error():
    data = read_csv('data')
    assert data == []
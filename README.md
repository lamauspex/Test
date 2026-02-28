

# CSV Processor



## 🟢 Описание проекта

Этот проект позволяет обрабатывать CSV-файлы с поддержкой фильтрации и агрегации данных.



## 🟢 Установка

1. Клонируйте репозиторий:

```shell
git clone https://github.com/lamauspex/Test.git
```


2. Создайте и активируйте виртуальное окружение:

Для Windows:
```shell
python -m venv venv
```
```shell
venv\Scripts\activate
```

Для macOS и Linux:
```shell
python3 -m venv venv
```
```shell
source venv/bin/activate
```



3. Установите зависимости:
```shell
pip install -r requirements.txt
```


## 🟢 Использование

 Запустите скрипт с указанием пути к CSV-файлу:


### Пример Для Фильтрации 

```shell
python main.py data/version_csv.csv --filter brand == xiaomi
```

```shell
python main.py data/version_csv.csv --filter name == "iphone 15 pro"
```

```shell
python main.py data/version_csv.csv --filter raiting == "4.9"
```

```shell
python main.py data/version_csv.csv --filter price '>' 300
```

```shell
python main.py data/version_csv.csv --filter price '<' 500
```


### Пример Для Агрегации

```shell
python main.py data/version_csv.csv --aggregate price 
```

Или

```shell
python main.py data/version_csv.csv --aggregate raiting
```


Ваш вклад в проект приветствуется! Если вы хотите внести изменения или улучшения, создайте pull request или откройте issue на GitHub.

#### Контакты
Если у вас есть вопросы или предложения, не стесняйтесь связаться со мной:

- Имя: Резник Кирилл
- Email: lamauspex@yandex.ru
- GitHub: https://github.com/lamauspex
- Telegram: @lamauspex

Спасибо за интерес к проекту! Надеюсь, он будет полезен в вашей работе.
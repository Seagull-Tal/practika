Установка
pip install tinydb


Инициализация базы

Создаёт файл db.json:

python init_db.py

Примеры запуска

python app.py get_tpl --login=test@mail.ru --tel="+7 999 999 99 99"

Если шаблон найден:
User Form

Если не найден:
{"login": "email", "tel": "text"}



Типы данных

email
phone (+7 XXX XXX XX XX)
date (DD.MM.YYYY или YYYY-MM-DD)
text (текст)

Логика

Подходит шаблон, если все его поля есть в запросе и совпадают по типу. Шаблоны без поля name игнорируются


Тесты

python -m unittest -v tests/test_form_matcher.py
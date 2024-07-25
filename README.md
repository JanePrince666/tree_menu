Django приложение, реализующее древовидное меню с использованием стандартных возможностей Django и Python.\nМеню хранится в базе данных и может быть редактировано через стандартную админку Django. Приложение позволяет отображать несколько меню на одной странице, определять активный пункт меню по текущему URL и поддерживает переходы по заданным URL.
# Основные функции
* Древовидное меню: Меню реализовано через кастомный template tag, который позволяет отображать меню на любой странице.\n
* Разворачивание пунктов: Все пункты меню над выделенным элементом развернуты, а также первый уровень вложенности под выделенным пунктом.\n
* Хранение в БД: Структура меню хранится в базе данных, что позволяет легко управлять меню через админку.\n
* Редактирование через админку: Меню можно редактировать через стандартную админку Django.\n
* Определение активного пункта: Активный пункт меню определяется на основе текущего URL страницы.\n
* Несколько меню на странице: Поддерживается отображение нескольких меню на одной странице, определяемых по названию.\n
* Переход по URL: При клике на пункт меню происходит переход по заданному URL, который может быть указан как явно, так и через именованный URL.\n
* Оптимизация запросов: Для отрисовки каждого меню требуется ровно один запрос к базе данных.\n
# Установка и запуск
Предварительные требования
Python 3.x
Django 3.x или выше
# Шаги по установке
1) Клонируйте репозиторий
2) Создайте виртуальное окружение (рекомендуется):
```
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```

3) Установите зависимости:
```
pip install -r requirements.txt
```

4) Создайте и примените миграции:
```
python manage.py makemigrations
python manage.py migrate
```

5) Создайте суперпользователя для доступа к админке:
```
python manage.py createsuperuser
```

6) Запустите сервер:
```
python manage.py runserver
```

7) Перейдите в админку:
Откройте браузер и перейдите по адресу http://127.0.0.1:8000/admin.\n
Войдите, используя созданные учетные данные суперпользователя.\n
Создайте и редактируйте пункты меню через интерфейс админки.\n

# Использование меню в шаблонах
Чтобы отобразить меню на странице, используйте следующий тег в вашем шаблоне:
```text
{% load your_custom_tags %}
{% draw_menu 'main_menu' %}
```
Замените 'main_menu' на имя вашего меню.

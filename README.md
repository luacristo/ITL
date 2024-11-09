# Лабораторная работа №5: Создание базы данных с использованием SQLite и Flask

## Цель работы
Научиться создавать базу данных SQLite, настраивать веб-приложение на Flask для работы с этой базой, а также добавлять поддержку кросс-доменных запросов с помощью CORS.

---

## Требования

- Все файлы проекта должны быть организованы в одной директории:
  - `app.py` - основной файл приложения Flask
  - `database.py` - файл для работы с базой данных
  - `models.py` - файл с описанием моделей данных
  - `requirements.txt` - файл с зависимостями

### Задание

1. **Создайте базу данных SQLite:**
   (экономя время сразу делайте через Python - без DB Browser for SQLite)
   - Создайте таблицы для хранения информации о сотрудниках IT-компании, включая:
     - id (первичный ключ)
     - имя
     - должность
     - email
     - зарплата
  ну там можно еще что то придумать)) это лишь общее задание..

2. **Настройка Flask-приложения:**
   - Создайте маршруты для выполнения следующих операций:
     - Получение всех сотрудников
     - Получение конкретного сотрудника по ID
     - Добавление нового сотрудника
     - Обновление информации о сотруднике
     - Удаление сотрудника
     - хочу видеть еще оценку зарплаты `SMB` (типо если от 30000 до 100000 - средняя, больше 100000 высокая и менее 30000 низкая)
  опять же можно расширить и добавить что то свое))

SMB:
- s (small) - низкая зарплата
- m (medium) - средняя зарплата
- h (high) - высокая зарплата

3. **Добавление CORS:**
   - Настройте CORS, чтобы разрешить запросы из других доменов.

---

После реализации используйте swagger UI для формирования API. В специально отведенном файле `api.py`.

сначала установите пакеты: `pip install flask-restx flask_migrate flask_restplus`

```python
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restx import Api, Resource, fields 
from models import db, Employee
from database import create_app # или что у тебя там используется

app = create_app()
CORS(app) 

api = Api(app, version='1.0', title='Employee API',
          description='An API to manage employees in an IT company')

# если у тебя не только Employee то соответственно для каждого тут и будет общий API

# потом ns
ns = api.namespace('employees', description='Operations related to employees')

# модели далее
employee_model = api.model('Employee', {...})

@ns.route('/')
class EmployeeList(Resource):
    pass


@ns.route('/<int:id>')
@ns.response(404, 'Employee not found')
@ns.param('id', 'The employee identifier')
class EmployeeResource(Resource):
    pass

if __name__ == '__main__':
    app.run(port="5001", debug=True)
```



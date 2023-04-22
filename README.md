## Gallery


### Логины и пароли:
 **Админ** ```Логин root - Пароль root``` 
 **Пользователи:** ```Логин user - Пароль 1234. Логин new_user - Пароль 1234```

## Локальный запуск проекта
После клонирования проекта выполните команды:

### Создайте виртуальное окружение командой
```virtualenv -p python3 venv```

### Активируйте виртуальное окружение командой
```source venv/bin/activate или venv\Scripts\activate```

### Установите зависимости командой
```
pip install -r requirements.txt
```

### Перейдите в папку gallery командой
```
cd gallery
```

### Примените миграции командой
```
python manage.py migrate
```
### Загрузите фикстуры командой
```python3 manage.py loaddata fixtures/dump.json```

### Запустите проект командой
```
python manage.py runserver
```

### Создайте администратора командой
```
python manage.py createsuperuser
```

Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin

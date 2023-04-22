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

### Инстукция к API для добавления и удаления Избранного текущего пользователя
#### Аутентификация  
1. Отправить POST запрос по адресу http://127.0.0.1:8000/api/login/  
В body передать (изменяем тип передаваемых данных на JSON):  
```
{  
    "username": "root",  
    "password": "root"  
} 
``` 
Далее, копируем токен, заходим в Headers, в поле Key прописываем Authorization и в value вставляем Token <полученный токен> (без стрелок)  
  
### Функционал
1. Добавление в избранное
POST http://127.0.0.1:8000/api/favorites/  
В body передаём (изменяем тип передаваемых данных на JSON):  
```
{    
    "photo": <int:pk>  
}
<int:pk> - уникальный идентификатор фотографии. Что бы добавить желаемое фото в избранное, запустите проект, как описано выше, пройдите в панель администратора -> Фотографии -> выберите нужный номер 
```  
2. Удаление  
DELETE http://127.0.0.1:8000/api/posts/<int:pk>/  
<int:pk> - в данном контексте передаётся универсальный идентификатор записи в модели "Избранное". Дабы получить желаемый номер, отправьте запрос GET http://127.0.0.1:8000/api/favorites  и выберите нужный id

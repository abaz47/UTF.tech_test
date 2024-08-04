# Тестовое задание backend разработчик UTF.tech
Описание задания - https://handsome-lobster-d78.notion.site/backend-UTF-tech-6dd5f993f1c54f5a8d202e8c13e67716

## Запуск:
Для запуска необходим установленный python3. Клонируем репозиторий, переходим в директорию с ним.
Создаем и активируем виртуальную среду, устанавливаем зависимости:
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

При отсутствии БД выполняем миграции, создаем пользователя:
```
python ./utftechtest/manage.py migrate
python ./utftechtest/manage.py createsuperuser
```

Запуск сервера:
```
python ./utftechtest/manage.py runserver
```

Для наполнения БД можно воспользоваться панелью администратора.
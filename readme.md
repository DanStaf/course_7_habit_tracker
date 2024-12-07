# course 7 / SPA habit tracker

## Developing Steps

1. add .gitignore, .env, readme
2. setup Poetry, DB and Django
```
/settings/Python interpreter/Add interpreter/Poetry environment 
poetry add django==4.2 python-dotenv psycopg2
django-admin startproject config .
python manage.py startapp spa
python manage.py startapp users
create DB "spa"
setup settings.py
```
3. setup User
```
poetry add djangorestframework djangorestframework-simplejwt django-filter
```
- config.settings.py
- config.urls
- models
- admin
- permissions
- serializers
- urls
- views
- csu `python manage.py csu`

3. setup Habit model
- models
- admin

4. setup Habit endpoints
- paginators
- serializers
- urls
- views (CRUD)

5. setup public habits
- urls
- views

6. Валидаторы
- validators
- serializers

7. Телеграм
- poetry add celery django-celery-beat redis eventlet
- config: settings, celery.py, tasks, services / migrate
- https://t.me/BotFather
- https://core.telegram.org/bots/api
- poetry add telebot
- add tg_id to user model
- config: env, settings, tasks, services


CORS

Документация

Тесты

Flake8







---

---

---

## Task

Реализовать бэкенд-часть SPA веб-приложения (трекер полезных привычек).

Идея: книга «Атомные привычки» (Джеймс Клир 2018).
- приобретение новых полезных привычек
- искоренению старых плохих привычек.

`Критерии приемки курсовой работы`



### Описание задач

---

### 1. Добавьте необходимые модели привычек.
я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

#### Привычка:
Пользователь — создатель привычки.

Действие — действие, которое представляет собой привычка.
(Полезная привычка - действие, за которое пользователь будет получать вознаграждение (приятная привычка или любое другое вознаграждение)

Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
- способ вознаградить себя за выполнение полезной привычки
- Приятная привычка указывается в качестве связанной для полезной привычки
- bool

Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
Примеры:
- Полезная -> вознаграждение Приятная (полезная имеет связанную)
- Полезная -> вознаграждение (само по себе)

Вознаграждение — чем пользователь должен себя вознаградить после выполнения.

Место — место, в котором необходимо выполнять привычку.

Время — время, когда необходимо выполнять привычку.

Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.

Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.

Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

+ `Все необходимые модели описаны или переопределены.`

### Валидаторы
Исключить одновременный выбор связанной привычки и указания вознаграждения.
В модели не должно быть заполнено одновременно и поле вознаграждения,
и поле связанной привычки. Можно заполнить только одно из двух полей.

Время выполнения должно быть не больше 120 секунд.

В связанные привычки могут попадать только привычки с признаком приятной привычки.

У приятной привычки не может быть вознаграждения или связанной привычки.

Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
Нельзя не выполнять привычку более 7 дней.
Например, привычка может повторяться раз в неделю, но не раз в 2 недели.
За одну неделю необходимо выполнить привычку хотя бы один раз.

+ `Настроили все необходимые валидаторы.`

---

### 2. Реализуйте эндпоинты для работы с фронтендом.

### Эндпоинты
+ Регистрация.

+ Авторизация.

+ Список привычек текущего пользователя с пагинацией.

+ Список публичных привычек.

+ Создание привычки.

+ Редактирование привычки.

+ Удаление привычки.

+ `Все необходимые эндпоинты реализовали.`

---

### 3. Создайте приложение для работы с Telegram и рассылками напоминаний.

### Интеграция
Для полноценной работы сервиса необходимо реализовать работу с отложенными задачами
для напоминания о том, в какое время какие привычки необходимо выполнять.

Для этого потребуется интегрировать сервис с мессенджером Телеграм,
который будет заниматься рассылкой уведомлений.

Вспомнить, как работать с API Телеграма, можно в разделе «Альтернативная задача»
в домашке урока Celery.

+ `Настроили интеграцию с Телеграмом.`

+ `Настроили отложенную задачу через Celery.`

---

### 4. Разное

### Пагинация
+ Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.

+ `Реализовали пагинацию.`

### Права доступа
+ Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.

+ Пользователь может видеть список публичных привычек без возможности их
как-то редактировать или удалять.

`Описанные права доступа заложены.`

### Безопасность
Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту
на развернутом сервере.

`Настроили CORS.`

### Документация
Для реализации экранов силами фронтенд-разработчиков необходимо настроить
вывод документации. При необходимости эндпоинты,
на которые документация не будет сгенерирована автоматически, описать вручную.

### Тесты
`Проект покрыли тестами как минимум на 80%.`

### Доп. критерии

`Использовали переменные окружения.`

`Код оформили в соответствии с лучшими практиками.`

`Имеется список зависимостей.`

`Результат проверки Flake8 равен 100%, при исключении миграций.`

`Решение выложили на GitHub.`


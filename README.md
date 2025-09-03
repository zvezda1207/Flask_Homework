# Flask REST API для объявлений

Простое REST API приложение на Flask для создания и управления объявлениями.

## Технологии

- Python 3.9
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PostgreSQL
- Docker
- Docker Compose

## Функциональность

- Создание объявлений (POST /adv)
- Получение списка всех объявлений (GET /adv)
- Получение конкретного объявления (GET /adv/<id>)
- Изменение объявления (PATCH /adv/<id>)
- Удаление объявления (DELETE /adv/<id>)

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/zvezda1207/Flask_Homework.git
cd Flask_Homework
```

2. Скопируйте файл `.env.example` в `.env` и заполните значениями для вашего окружения:

```bash
cp .env.example .env
```

Затем отредактируйте файл .env и установите свои значения переменных.

3. Запустите приложение с помощью Docker Compose:

```bash
docker-compose up --build
```

4. Приложение будет доступно по адресу: http://localhost:5000

## Использование API

### Создание объявления

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "title": "Продам машину",
  "description": "Отличное состояние, 2018 год",
  "owner": "Иван Иванов"
}' http://localhost:5000/adv
```

### Получение всех объявлений

```bash
curl http://localhost:5000/adv
```

### Получение конкретного объявления

```bash
curl http://localhost:5000/adv/1
```

### Изменение объявления

```bash
curl -X PATCH -H "Content-Type: application/json" -d '{
  "title": "Новое название"
}' http://localhost:5000/adv/1
```

### Удаление объявления

```bash
curl -X DELETE http://localhost:5000/adv/1
```
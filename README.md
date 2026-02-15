# Telegram RSS News Bot

Телеграм-бот, который парсит RSS-ленты и автоматически публикует новости в канал.

> **Важно:** пока работает только с одним RSS-источником.

## Стек

- Python 3.12
- Aiogram 3.21
- SQLAlchemy 2.0 + Alembic
- APScheduler
- Pydantic Settings
- Docker + Docker Compose
- Poetry

## Что умеет

- Парсит RSS и публикует новости по расписанию
- Хранит историю опубликованного, чтобы не дублировать
- Позволяет настраивать интервал рассылки прямо из бота
- Есть троттлинг, чтобы не словить бан от Telegram

## Структура
```
bot/
├── handlers/       
├── keyboards/      
├── middleware/     
├── states/         
├── utils/          
└── db/
    ├── crud.py
    ├── database.py
    └── models.py
migrations/
docker-compose.yaml
Dockerfile
startup.sh
.env.example
```

## Запуск
```bash
git clone https://github.com/yourusername/telegram-rss-bot.git
cd telegram-rss-bot
cp .env.example .env
```

Заполните `.env`:
```
BOT_TOKEN=...
CHANNEL_ID=...
```
```bash
docker-compose up --build
```

## Команды

| Команда | Описание |
|---------|----------|
| `/start` | Запуск |
| `/settings` | Панель управления |
| `/add <url>` | Добавить источник |
| `/remove <url>` | Удалить источник |
| `/show` | Список источников |
| `/start_sender` | Запустить рассылку |

## Планы

- Поддержка нескольких источников
- Фильтрация по тегам
- Уведомления об ошибках
- Тесты

## Скриншоты

![](https://raw.githubusercontent.com/Mksdnk/rss_news_bot/main/screenshots/screenshot1.png)
![](https://raw.githubusercontent.com/Mksdnk/rss_news_bot/main/screenshots/screenshot2.png)
![](https://raw.githubusercontent.com/Mksdnk/rss_news_bot/main/screenshots/screenshot3.png)
![](https://raw.githubusercontent.com/Mksdnk/rss_news_bot/main/screenshots/screenshot4.png)

#!/bin/sh

# Ожидание готовности БД
echo "Waiting for database at ${POSTGRES_HOST}:${POSTGRES_PORT}..."
while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
  sleep 0.5
done
echo "Database ready!"

# Применение миграций
echo "Applying database migrations..."
alembic upgrade head

# Запуск бота 
echo "Starting bot..."
while true; do
    python -m bot.main
    status=$?
    if [ $status -ne 0 ]; then
        echo "Bot crashed with exit code $status. Restarting in 5 seconds..."
        sleep 5
    else
        echo "Bot exited normally. Stopping container."
        break
    fi
done
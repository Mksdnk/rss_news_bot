FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==1.8.2"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

COPY . .

RUN chmod 777 /app/startup.sh

CMD ["sh", "/app/startup.sh"]
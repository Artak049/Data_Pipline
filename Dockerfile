FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install asyncpg faker

CMD ["sh", "-c", "sleep 10 && python main.py"]
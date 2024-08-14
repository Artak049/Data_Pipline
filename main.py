import asyncio
import random
import asyncpg
from faker import Faker

fake = Faker()


# Creating database if not exists
async def create_db_if_not_exists(db, user, pwd, host, port):
    conn = await asyncpg.connect(user=user, password=pwd, host='db', port=port, database='data_pipline')
    try:
        db_exists = await conn.fetchval(f"""SELECT EXISTS
        (SELECT 1 FROM pg_database WHERE datname = '{db}')
         """)

        if not db_exists:
            await conn.execute(f"CREATE DATABASE {db}")
            print(f"Created database {db}")
        else:
            print(f"Database {db} already exists")
    finally:
        await conn.close()


# Create table if not exists
async def create_table_if_not_exists(conn):
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS user_metrics (
    user_id INT,
    session_id INT,
    talked_time INT,
    microphone_used BOOLEAN,
    speaker_used BOOLEAN,
    timestamp TIMESTAMP)
    """)


# connecting function
async def db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="NewMe2024",
        database="data_pipline",
        host="db"
    )


# generating fake user metrics with library faker
def generate_user_metrics():
    return {
        "user_id": fake.random_int(min=1, max=10000),
        "session_id": fake.random_int(min=1, max=1000),
        "talked_time": fake.random_int(1, 10000),
        "microphone_used": random.choice([True, False]),
        "speaker_used": random.choice([True, False]),
        "timestamp": fake.date_time_this_year().timestamp()
    }


# Inserting user metrics from generate_user_metrics
async def insert_metrics(conn, data):
    await conn.execute("""
    INSERT INTO user_metrics (user_id, session_id, talked_time, microphone_used, speaker_used, timestamp )
    VALUES ($1, $2, $3, $4, $5, to_timestamp($6))""", data["user_id"], data["session_id"], data["talked_time"],
                       data["microphone_used"], data["speaker_used"], data["timestamp"])


async def stream_user_metrics(interval=1):
        await create_db_if_not_exists("data_pipline", "postgres", "NewMe2024", "db", 5432)
        conn = await db_connection()
        await create_table_if_not_exists(conn)
        try:
            while True:
                metrics = generate_user_metrics()
                await insert_metrics(conn, metrics)
                print("inserted:", metrics)
                await asyncio.sleep(interval)
        finally:
                await conn.close()


async def main():
    await stream_user_metrics()

if __name__ == "__main__":
    asyncio.run(main())

import psycopg2

# Подключение к Railway
conn = psycopg2.connect(
    host="hopper.proxy.rlwy.net",
    port=32436,
    database="railway",
    user="postgres",
    password="mJzZmcvnamZbzoIfVSIkHCOUPlEIrAHn",
    sslmode="require"
)

cur = conn.cursor()

# Создаем таблицу, если её нет
cur.execute("""
CREATE TABLE IF NOT EXISTS costumer (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone_number TEXT,
    insta_acc TEXT
);
""")

conn.commit()
print("✅ Таблица 'costumer' создана или уже существует.")

cur.close()
conn.close()

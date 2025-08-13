from flask import Flask, render_template, request
import psycopg2
import os
import threading
from bot import run_bot

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "hopper.proxy.rlwy.net")
DB_PORT = os.environ.get("DB_PORT", "32436")
DB_NAME = os.environ.get("DB_NAME", "railway")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "mJzZmcvnamZbzoIfVSIkHCOUPlEIrAHn")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode="require"
    )

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        phone_number = request.form["phone_number"]
        insta_acc = request.form["insta_acc"]

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO costumer (name, phone_number, insta_acc)
            VALUES (%s, %s, %s)
        """, (name, phone_number, insta_acc))

        conn.commit()
        cur.close()
        conn.close()

        return f"""
        <div style='text-align:center; font-family:Arial; margin-top:50px;'>
            <h2 style='color:green;'>✅ Клиент {name} добавлен!</h2>
            <a href='/' style='display:inline-block; padding:10px 20px; background:#0d6efd; color:white; text-decoration:none; border-radius:5px;'>Добавить ещё</a>
        </div>
        """

    return render_template("form.html")

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

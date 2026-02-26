import sqlite3
import json

class UserStore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL)")
        conn.commit()
        conn.close()

    def load(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM users").fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def save(self, user):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user["name"], user["email"])
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    def find_by_id(self, user_id):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        return dict(row) if row else None

    def update_user(self, user_id, updated_data):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (updated_data["name"], updated_data["email"], user_id)
        )
        conn.commit()
        conn.close()
        return self.find_by_id(user_id)

    def delete_user(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
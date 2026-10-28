import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    def autentikasi(self, username, password):
        if not self.conn:
            return None

        cursor = self.conn.cursor(dictionary=True)

        try:
            password_hash = self.hash_password(password)

            query = """
                SELECT id_user, username, role
                FROM users
                WHERE username = %s AND password = %s
            """
            cursor.execute(query, (username, password_hash))
            return cursor.fetchone()

        finally:
            cursor.close()

    def register_user(self, username, password, role):
        if not self.conn or not username or not password:
            return False

        if role not in ("admin", "anggota"):
            return False

        cursor = self.conn.cursor()

        try:
            password_hash = self.hash_password(password)

            query = """
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """
            cursor.execute(
                query, (username, password_hash, role)
            )
            self.conn.commit()
            return True

        except Exception as e:
            self.conn.rollback()
            print("Gagal mendaftarkan pengguna:", e)
            return False

        finally:
            cursor.close()

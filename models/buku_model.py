
from config.database import Database


class BukuModel:
    def __init__(self):
        self.db = Database()

    def create_buku(self, judul, penulis, tahun_terbit):
        conn = self.db.get_connection()

        if not conn:
            print("Gagal: koneksi database tidak tersedia.")
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (judul, penulis, tahun_terbit))
            conn.commit()

            print("Berhasil menambahkan buku.")
            return True

        except Exception as e:
            conn.rollback()
            print(f"Gagal menambahkan buku: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_all_buku(self):
        conn = self.db.get_connection()

        if not conn:
            print("Gagal: koneksi database tidak tersedia.")
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM buku")
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data buku: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        conn = self.db.get_connection()

        if not conn:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE buku
                SET judul = %s, penulis = %s, tahun_terbit = %s
                WHERE id_buku = %s
            """
            cursor.execute(
                query, (judul, penulis, tahun_terbit, id_buku)
            )
            conn.commit()

            print(f"Berhasil mengupdate buku ID {id_buku}.")
            return cursor.rowcount > 0

        except Exception as e:
            conn.rollback()
            print(f"Gagal update buku: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete_buku(self, id_buku):
        conn = self.db.get_connection()

        if not conn:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM buku WHERE id_buku = %s",
                (id_buku,)
            )
            conn.commit()

            print(f"Berhasil menghapus buku ID {id_buku}.")
            return cursor.rowcount > 0

        except Exception as e:
            conn.rollback()
            print(f"Gagal menghapus buku: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

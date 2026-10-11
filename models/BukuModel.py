from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()

    def create_buku(self, judul, penulis, tahun_terbit):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
                cursor.execute(query, (judul, penulis, tahun_terbit))
                conn.commit()
                print("Berhasil menambahkan buku")
            except Exception as e:
                print(f"Gagal menambahkan buku: {e}")
            finally:
                cursor.close()
                conn.close()

    def get_all_buku(self):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                query = "SELECT * FROM buku"
                cursor.execute(query)
                data = cursor.fetchall()
                return data
            except Exception as e:
                print(f"Gagal mengambil data buku: {e}")
                return []
            finally:
                cursor.close()
                conn.close()

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE buku SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
                cursor.execute(query, (judul, penulis, tahun_terbit, id_buku))
                conn.commit()
                print(f"Berhasil mengupdate buku dengan ID {id_buku}")
            except Exception as e:
                print(f"Gagal update buku: {e}")
            finally:
                cursor.close()
                conn.close()

    def delete_buku(self, id_buku):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM buku WHERE id_buku = %s"
                cursor.execute(query, (id_buku,))
                conn.commit()
                print(f"Berhasil menghapus buku dengan ID {id_buku}")
            except Exception as e:
                print(f"Gagal menghapus buku: {e}")
            finally:
                cursor.close()
                conn.close()
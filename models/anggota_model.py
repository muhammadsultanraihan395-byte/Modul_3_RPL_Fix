from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()

    # Operasi Create (Tambah Anggota)
    def tambah_anggota(self, nama, alamat):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
                cursor.execute(query, (nama, alamat))
                conn.commit()
                print(f"Berhasil menambahkan anggota: {nama}")
            except Exception as e:
                print(f"Gagal menambahkan anggota: {e}")
            finally:
                cursor.close()
                conn.close()

    # Operasi Read (Tampilkan Semua Anggota)
    def get_all_anggota(self):
        conn = self.db.get_connection()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                query = "SELECT * FROM anggota"
                cursor.execute(query)
                data = cursor.fetchall()
                return data
            except Exception as e:
                print(f"Gagal mengambil data anggota: {e}")
                return []
            finally:
                cursor.close()
                conn.close()
from models.BukuModel import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 3. Menguji fungsi Update
print("\n=== UJI UPDATE BUKU ===")
model.update_buku(1, "Pemrograman Python Lanjutan", "Guido van Rossum", 2024)

# Ubah angka 2 menjadi 9 (atau ID lain yang baru di-create)
print("\n=== UJI DELETE BUKU ===")
model.delete_buku(9)

from models.anggota_model import AnggotaModel

model_anggota = AnggotaModel()

print("=== UJI CREATE ANGGOTA ===")
model_anggota.tambah_anggota("Budi Santoso", "Jl. Mawar No. 12")

print("\n=== UJI READ ANGGOTA ===")
anggota_list = model_anggota.get_all_anggota()
for anggota in anggota_list:
    print(f"ID: {anggota['id_anggota']} | Nama: {anggota['nama']} | Alamat: {anggota['alamat']}")
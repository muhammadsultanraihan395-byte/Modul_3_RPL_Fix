# Sistem Manajemen Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan merupakan aplikasi desktop berbasis Python yang dikembangkan untuk membantu proses pengelolaan data buku dan pengguna perpustakaan. Aplikasi ini menggunakan arsitektur Model-View-Controller (MVC) agar setiap bagian program memiliki tugas dan fungsi yang terstruktur.

Aplikasi menyediakan fitur autentikasi pengguna, pengelolaan data buku, serta pembagian hak akses berdasarkan peran pengguna. Antarmuka aplikasi dibuat menggunakan CustomTkinter, sedangkan penyimpanan data menggunakan database MySQL.

## 2. Struktur Direktori MVC

Proyek ini menggunakan pola arsitektur Model-View-Controller (MVC) dengan struktur direktori sebagai berikut:

```text
Modul V/
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── config/
│   └── database.py
│
├── controllers/
│   ├── auth_controller.py
│   └── buku_controller.py
│
├── models/
│   ├── user_model.py
│   └── buku_model.py
│
├── views/
│   ├── login_view.py
│   └── buku_view.py
│
├── tests/
│   ├── test_auth.py
│   └── test_buku.py
│
├── dist/
├── build/
├── env/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

**Penjelasan komponen MVC:**

- **Models:** Bertanggung jawab mengelola data dan berkomunikasi dengan database MySQL, termasuk proses autentikasi pengguna dan pengelolaan data buku.
- **Views:** Bertanggung jawab menampilkan antarmuka aplikasi kepada pengguna, seperti halaman login dan halaman pengelolaan buku.
- **Controllers:** Bertanggung jawab mengatur alur aplikasi, menghubungkan Models dengan Views, serta menangani proses autentikasi dan pengelolaan buku.
- **Config:** Menyimpan konfigurasi koneksi database MySQL.
- **Tests:** Menyimpan program pengujian untuk memeriksa fungsi autentikasi dan pengelolaan buku.
- **.github/workflows:** Menyimpan konfigurasi GitHub Actions untuk menjalankan proses Continuous Integration (CI) secara otomatis.

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### A. Persiapan

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki beberapa perangkat lunak berikut:

1. Python.
2. Visual Studio Code.
3. Laragon.
4. Git.
5. MySQL.

### B. Mengunduh Proyek

Clone repository GitHub menggunakan perintah:

```bash
git clone https://github.com/USERNAME/Modul_3_RPL_Fix.git
```

Masuk ke direktori proyek:

```bash
cd Modul_3_RPL_Fix
```

### C. Membuat Virtual Environment

Buat lingkungan virtual Python:

```bash
python -m venv env
```

Aktifkan virtual environment pada Windows:

```powershell
.\env\Scripts\Activate.ps1
```

### D. Menginstal Dependensi

Instal seluruh pustaka yang dibutuhkan aplikasi melalui requirements.txt:

```bash
pip install -r requirements.txt
```

### E. Konfigurasi Database MySQL

1. Buka aplikasi Laragon.
2. Jalankan layanan MySQL.
3. Buat database dengan nama `perpustakaan`.
4. Sesuaikan konfigurasi database pada file `config/database.py`.

Konfigurasi database yang digunakan:

- Host: localhost
- Database: perpustakaan
- Username: root
- Password: kosong (sesuai konfigurasi lokal).

Pastikan nama database dan informasi koneksi sesuai dengan konfigurasi MySQL pada perangkat yang digunakan.

## 4. Cara Menjalankan Aplikasi

Setelah seluruh dependensi terpasang dan database berhasil dikonfigurasi, aplikasi dapat dijalankan melalui beberapa langkah berikut.

### A. Menjalankan melalui Python

Pastikan virtual environment telah aktif, kemudian jalankan:

```bash
python main.py
```

Aplikasi akan menampilkan halaman login. Pengguna dapat memasukkan username dan password yang telah terdaftar pada database.

### B. Menjalankan Pengujian Otomatis

Untuk menjalankan seluruh unit test menggunakan Pytest, gunakan perintah:

```bash
pytest -v
```

### C. Menjalankan Pemeriksaan Kualitas Kode

Pemeriksaan kode menggunakan Flake8 dapat dilakukan dengan perintah:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

### D. Menjalankan Aplikasi dalam Format EXE

Aplikasi dapat dikemas menjadi file executable menggunakan PyInstaller:

```bash
pyinstaller --clean --noconfirm --onefile --windowed --name AplikasiPerpustakaan --collect-all=mysql.connector --hidden-import=mysql.connector.plugins.mysql_native_password --hidden-import=mysql.connector.locales.eng.client_error main.py
```

Setelah proses pemaketan selesai, file aplikasi dapat ditemukan di:

```text
dist/AplikasiPerpustakaan.exe
```

Pastikan layanan MySQL pada Laragon sudah berjalan sebelum membuka aplikasi.

## 5. Continuous Integration (CI)

Proyek ini menerapkan Continuous Integration menggunakan GitHub Actions. Pipeline dijalankan secara otomatis ketika terdapat perubahan kode yang dikirimkan ke branch `main` atau ketika Pull Request dibuat menuju branch tersebut.

Tahapan pipeline meliputi:

1. Mengambil kode dari repository GitHub.
2. Menyiapkan lingkungan Python 3.11.
3. Menginstal dependensi proyek melalui requirements.txt.
4. Memeriksa kualitas kode menggunakan Flake8.
5. Menjalankan pengujian otomatis menggunakan Pytest.

Penerapan CI bertujuan membantu mendeteksi kesalahan kode lebih awal serta menjaga kualitas dan konsistensi aplikasi selama proses pengembangan.
import tkinter.messagebox as messagebox

from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = None
        self.authenticated_user = None
        self.logged_out = False

    def run(self):
        # Perulangan utama untuk mengatur Login dan Logout
        while True:
            self.authenticated_user = None

            # Tampilkan halaman login
            self.view = LoginView()
            self.view.btn_login.configure(
                command=self.proses_login
            )

            # Tunggu sampai jendela login ditutup
            self.view.mainloop()

            # Jika login tidak berhasil atau jendela ditutup
            if not self.authenticated_user:
                break

            # Ambil informasi pengguna yang berhasil login
            user = self.authenticated_user
            self.logged_out = False

            # Tampilkan menu perpustakaan
            app_utama = BukuController(
                user_role=user["role"],
                on_logout=self.proses_logout
            )

            app_utama.run()

            # Jika jendela ditutup tanpa Logout, keluar aplikasi
            if not self.logged_out:
                break

    def proses_login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan password wajib diisi!"
            )
            return

        user = self.model.autentikasi(username, password)

        if not user:
            messagebox.showerror(
                "Login Gagal",
                "Username atau password salah!"
            )
            return

        messagebox.showinfo(
            "Login Berhasil",
            f"Selamat datang, {user['username']}!"
        )

        # Simpan informasi pengguna
        self.authenticated_user = user

        # Tutup jendela login
        self.view.destroy()
        self.view = None

    def proses_logout(self):
        # Tandai bahwa pengguna melakukan Logout
        self.logged_out = True

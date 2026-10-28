import tkinter.messagebox as messagebox

from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = None

    def run(self):
        self.tampilkan_login()

    def tampilkan_login(self):
        self.view = LoginView()
        self.view.btn_login.configure(
            command=self.proses_login
        )
        self.view.mainloop()

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

        self.view.destroy()
        self.view = None

        BukuController(
            user_role=user["role"],
            on_logout=self.tampilkan_login
        ).run()

import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota", on_logout=None):
        self.user_role = user_role
        self.on_logout = on_logout

        self.model = BukuModel()
        self.view = BukuView(
            user_role=self.user_role,
            on_logout=self.logout
        )

        # Menampilkan role pada judul jendela
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # Binding tombol simpan
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        # Otorisasi tombol update dan delete
        if self.user_role != "admin":
            self.view.btn_update.configure(state="disabled")
            self.view.btn_delete.configure(state="disabled")

            # Anggota hanya boleh melihat data buku
            self.view.btn_simpan.configure(
                state="disabled",
                text="Khusus Admin"
            )

            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        # Proteksi tambahan di level controller
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menambah data!"
            )
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data."
            )

    def logout(self):
        # Tutup jendela buku
        self.view.destroy()

        # Kembali ke halaman login jika callback tersedia
        if self.on_logout:
            self.on_logout()

    def run(self):
        self.view.mainloop()

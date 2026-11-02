
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

        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.view.btn_update.configure(
            command=self.update_data
        )

        self.view.btn_delete.configure(
            command=self.hapus_data
        )

        self.view.btn_logout.configure(
            command=self.logout
        )

        # Menghubungkan pemilihan baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_buku
        )

        # Hak akses anggota
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled")
            self.view.btn_update.configure(state="disabled")
            self.view.btn_delete.configure(state="disabled")

            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    # Menampilkan seluruh data buku
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

    # Mengambil data ketika baris tabel dipilih
    def pilih_buku(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        # Mengisi form dengan data yang dipilih
        for entry, value in zip(
            (
                self.view.entry_judul,
                self.view.entry_penulis,
                self.view.entry_tahun
            ),
            data[1:]
        ):
            entry.configure(state="normal")
            entry.delete(0, "end")
            entry.insert(0, value)

            if self.user_role != "admin":
                entry.configure(state="disabled")

    # Membersihkan form
    def kosongkan_form(self):
        for entry in (
            self.view.entry_judul,
            self.view.entry_penulis,
            self.view.entry_tahun
        ):
            entry.configure(state="normal")
            entry.delete(0, "end")

            if self.user_role != "admin":
                entry.configure(state="disabled")

        self.view.tabel.selection_remove(
            self.view.tabel.selection()
        )

    # Menambah data buku
    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya petugas yang dapat menambah data!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom wajib diisi!"
            )
            return

        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil ditambahkan!"
            )

            self.kosongkan_form()
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Gagal",
                "Data buku gagal ditambahkan!"
            )

    # Memperbarui data buku
    def update_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya petugas yang dapat memperbarui data!"
            )
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        id_buku = data[0]

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom wajib diisi!"
            )
            return

        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah kamu yakin ingin memperbarui data buku ini?"
        )

        if not konfirmasi:
            return

        berhasil = self.model.update_buku(
            id_buku,
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )

            self.kosongkan_form()
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Gagal",
                "Data buku gagal diperbarui!"
            )

    # Menghapus data buku
    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya petugas yang dapat menghapus data!"
            )
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        id_buku = data[0]
        judul = data[1]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi Hapus",
            f"Apakah kamu yakin ingin menghapus buku '{judul}'?"
        )

        if not konfirmasi:
            return

        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )

            self.kosongkan_form()
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Gagal",
                "Data buku gagal dihapus!"
            )

    # Logout
    def logout(self):
        self.view.destroy()

        if self.on_logout:
            self.on_logout()

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()

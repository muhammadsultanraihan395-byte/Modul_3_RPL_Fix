import tkinter.messagebox as messagebox

from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()
        self.id_buku_dipilih = None

        # Hubungkan tombol ke fungsi controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        # Isi form saat pengguna memilih baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_buku
        )

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

    def pilih_buku(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        nilai = self.view.tabel.item(pilihan[0], "values")

        self.id_buku_dipilih = int(nilai[0])

        self.view.entry_judul.delete(0, "end")
        self.view.entry_judul.insert(0, nilai[1])

        self.view.entry_penulis.delete(0, "end")
        self.view.entry_penulis.insert(0, nilai[2])

        self.view.entry_tahun.delete(0, "end")
        self.view.entry_tahun.insert(0, nilai[3])

    def simpan_data(self):
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan", "Semua kolom harus diisi!"
            )
            return

        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan", "Tahun terbit harus berupa angka!"
            )
            return

        berhasil = self.model.create_buku(
            judul, penulis, int(tahun)
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data buku berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data gagal disimpan. Periksa terminal."
            )

    def perbarui_data(self):
        if self.id_buku_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku dari tabel yang ingin diperbarui!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan", "Semua kolom harus diisi!"
            )
            return

        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan", "Tahun terbit harus berupa angka!"
            )
            return

        berhasil = self.model.update_buku(
            self.id_buku_dipilih,
            judul,
            penulis,
            int(tahun)
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data buku berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data tidak berhasil diperbarui. "
                "Pastikan ID buku masih tersedia."
            )

    def hapus_data(self):
        if self.id_buku_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku dari tabel yang ingin dihapus!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Yakin ingin menghapus buku ID "
            f"{self.id_buku_dipilih}?"
        )

        if not konfirmasi:
            return

        berhasil = self.model.delete_buku(
            self.id_buku_dipilih
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data buku berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data gagal dihapus. Periksa terminal."
            )

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")
        self.id_buku_dipilih = None

        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    def run(self):
        self.view.mainloop()

import tkinter.messagebox as messagebox

from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()
        self.id_anggota_dipilih = None

        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_update.configure(
            command=self.perbarui_data
        )
        self.view.btn_delete.configure(
            command=self.hapus_data
        )

        self.view.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_anggota
        )

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def pilih_anggota(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        nilai = self.view.tabel.item(
            pilihan[0], "values"
        )

        self.id_anggota_dipilih = int(nilai[0])

        self.view.entry_nama.delete(0, "end")
        self.view.entry_nama.insert(0, nilai[1])

        self.view.entry_alamat.delete(0, "end")
        self.view.entry_alamat.insert(0, nilai[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        berhasil = self.model.tambah_anggota(
            nama, alamat
        )

        # Model lama belum mengembalikan nilai True/False.
        if berhasil is False:
            messagebox.showerror(
                "Error", "Gagal menyimpan data anggota."
            )
            return

        messagebox.showinfo(
            "Sukses",
            "Perintah simpan telah dijalankan. "
            "Periksa tabel untuk memastikan data tersimpan."
        )

        self.bersihkan_form()
        self.muat_data_tabel()

    def perbarui_data(self):
        messagebox.showwarning(
            "Belum tersedia",
            "Fungsi update memerlukan method update_anggota() "
            "di AnggotaModel."
        )

    def hapus_data(self):
        messagebox.showwarning(
            "Belum tersedia",
            "Fungsi hapus memerlukan method "
            "delete_anggota() di AnggotaModel."
        )

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")
        self.id_anggota_dipilih = None

        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    def run(self):
        self.view.mainloop()

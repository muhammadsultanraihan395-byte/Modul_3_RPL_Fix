
from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Inisialisasi model
    model = BukuModel()

    # Mock koneksi database melalui Database
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    model.db.get_connection = MagicMock(return_value=mock_conn)
    mock_conn.cursor.return_value = mock_cursor

    # Jalankan fungsi tambah buku
    hasil = model.create_buku(
        "Buku Testing",
        "Penulis QA",
        2026
    )

    # Pastikan operasi berhasil
    assert hasil is True

    # Pastikan query dijalankan tepat satu kali
    mock_cursor.execute.assert_called_once_with(
        """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """,
        ("Buku Testing", "Penulis QA", 2026)
    )

    # Pastikan transaksi disimpan
    mock_conn.commit.assert_called_once()

    # Pastikan koneksi ditutup
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()
    
from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_get_all_buku_berhasil():
    model = BukuModel()

    # Membuat mock koneksi dan cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    model.db.get_connection = MagicMock(
        return_value=mock_conn
    )
    mock_conn.cursor.return_value = mock_cursor

    # Data tiruan yang dikembalikan database
    data_dummy = [
        {
            "id_buku": 1,
            "judul": "Buku Testing",
            "penulis": "Penulis QA",
            "tahun_terbit": 2026
        }
    ]

    mock_cursor.fetchall.return_value = data_dummy

    # Menjalankan fungsi yang diuji
    hasil = model.get_all_buku()

    # Memastikan hasil sesuai data tiruan
    assert hasil == data_dummy
    assert len(hasil) == 1

    # Memastikan query SELECT dijalankan
    mock_conn.cursor.assert_called_once_with(
        dictionary=True
    )
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM buku"
    )
    mock_cursor.fetchall.assert_called_once()

    # Memastikan koneksi ditutup
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()


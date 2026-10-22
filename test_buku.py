
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

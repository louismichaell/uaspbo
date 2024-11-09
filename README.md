# 🚀 Sistem Informasi Reservasi Tiket Maskapai

Program ini adalah contoh implementasi sistem informasi reservasi tiket maskapai menggunakan OOP di Python. Program mendefinisikan beberapa kelas yang mewakili entitas dalam sistem reservasi, seperti `Penumpang` dan `Tiket`. Tiket dapat dibedakan ke dalam dua kelas utama: **Bisnis** dan **Ekonomi**. Setiap kelas memiliki atribut dan metode unik yang memungkinkannya untuk menyimpan informasi terkait dan menampilkan data tiket dan penumpang.

## Fitur

- **Kelas Abstrak untuk Penumpang**: `IPenumpang` adalah kelas abstrak dengan metode `viewPenumpang` yang digunakan untuk menampilkan data penumpang.
- **Kelas `Penumpang`**: Implementasi dari `IPenumpang` yang berisi data pribadi penumpang (ID, nama, dan nomor telepon).
- **Kelas `Tiket`**: Mewakili tiket secara umum dan menyimpan informasi tiket seperti nomor tiket, asal, tujuan, dan kelas.
- **Kelas `Bisnis` dan `Ekonomi`**: Mewarisi kelas `Tiket` dan menambahkan atau mengubah fitur tertentu, seperti `fasilitasTambahan` untuk kelas `Bisnis`.
  
## Struktur Kelas

1. **IPenumpang (Abstrak)**: Sebagai antarmuka untuk penumpang.
2. **Penumpang**: Implementasi `IPenumpang` yang menyimpan data penumpang.
3. **Tiket**: Menyimpan data tiket dasar, memiliki metode untuk memilih kelas.
4. **Bisnis**: Sub-kelas dari `Tiket` dengan tambahan fitur `fasilitasTambahan`.
5. **Ekonomi**: Sub-kelas dari `Tiket` tanpa tambahan fitur.

## Cara Kerja

1. Program meminta pengguna memasukkan data penumpang dan tiket (seperti nomor tiket, asal, tujuan, dan kelas).
2. Jika kelas tiket adalah "Bisnis," pengguna dapat memasukkan fasilitas tambahan.
3. Program menampilkan data penumpang dan tiket sesuai kelas yang dipilih.

## Prasyarat

Pastikan Python sudah terpasang di sistem Anda.

## Cara Menjalankan Program

1. Clone repositori ini.
2. Jalankan program dengan menjalankan perintah berikut di terminal:

   ```bash
   python <nama_file>.py

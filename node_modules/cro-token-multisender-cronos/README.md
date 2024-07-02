# CRO Token MultiSender - Cronos

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

Script ini adalah alat sederhana yang memungkinkan Anda untuk mengirim CRO (Chrono) ke beberapa alamat tujuan sekaligus di jaringan Cronos menggunakan beberapa private key yang telah Anda siapkan. Ini berguna jika Anda perlu mendistribusikan CRO ke beberapa akun secara efisien.

## Daftar Isi
- [Persyaratan](#persyaratan)
- [Pemasangan](#pemasangan)
- [Cara Menggunakan](#cara-menggunakan)
- [Lisensi](#lisensi)

## Persyaratan

- Python 3.x
- web3.py library (`pip install web3`)
- tqdm library (`pip install tqdm`)

## Pemasangan

1. Pastikan Anda telah menginstal Python 3.x. Jika belum, Anda dapat mengunduhnya dari [situs resmi Python](https://www.python.org/downloads/).

2. Instal library yang diperlukan dengan menjalankan perintah berikut:
`pip install web3 tqdm`

## Cara Menggunakan

1. Buat file `privatekeys.txt` dan `destinations.txt`. Isi `privatekeys.txt` dengan satu atau lebih private key yang ingin Anda gunakan untuk mengirim CRO. Isi `destinations.txt` dengan alamat-alamat tujuan yang ingin Anda kirimkan CRO-nya.

2. Jalankan skrip dengan perintah berikut:
`python script.py`


3. Script akan memulai pengiriman CRO ke alamat-alamat tujuan yang Anda tentukan. Setiap transaksi akan mencetak detailnya, dan Anda dapat mengikuti kemajuannya.

4. Setelah selesai, script akan mencetak jumlah wallet yang berhasil dikirim, jumlah yang gagal, dan total CRO yang dihabiskan untuk pengiriman.

## Konfigurasi Tambahan

Anda dapat mengedit beberapa pengaturan dalam skrip ini untuk mengkustomisasi pengiriman Anda:

- **Jeda Waktu Minimum dan Maksimum**: Anda dapat mengubah `JEDA_MIN` dan `JEDA_MAX` dalam skrip untuk menyesuaikan jeda waktu antara transaksi. Contoh:

  ```python
  JEDA_MIN = 5  # jeda waktu minimum antara transaksi (detik)
  JEDA_MAX = 10  # jeda waktu maksimum antara transaksi (detik)
   ```
  
- **Total CRO yang Akan Dikirim**: Anda dapat mengubah jumlah CRO yang akan dikirim ke setiap alamat tujuan dalam skrip. Contoh:
  ```python
  send_cro_to_many_wallets(privatekeys, destinations, 0.1)  # Mengirim 0.1 CRO ke setiap alamat tujuan
  ```

- **Gas Fee**: Anda dapat mengedit gas dalam dictionary tx dalam skrip untuk menyesuaikan jumlah gas yang akan digunakan. Contoh:

  ```python
    tx = {
      'from': address,
      'to': Web3.to_checksum_address(destination),
      'value': aw_round,
      'nonce': nonce,
      'gas': 21000,  # Ubah ke jumlah gas yang diinginkan
      'gasPrice': int(gas_price),  # Ubah ke integer
      'chainId': w3.eth.chain_id,
  }
   ```

## Lisensi

Projek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE.md) untuk detail lebih lanjut.

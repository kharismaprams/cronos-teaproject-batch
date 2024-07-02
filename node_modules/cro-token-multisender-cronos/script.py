from web3 import Web3, exceptions
import time
from tqdm import tqdm
import random

# Baca daftar private key dari file privatekeys.txt
with open("privatekeys.txt", "r") as file:
    privatekeys = [line.strip() for line in file.readlines()]

# Baca daftar alamat penerima dari file destinations.txt
with open("destinations.txt", "r") as file:
    destinations = [line.strip() for line in file.readlines()]

# Pengaturan persentase dan jeda waktu
TST_FROM = 1  # persentase dari saldo untuk penarikan (min)
TST_TO = 1    # persentase dari saldo untuk penarikan (maks)
JEDA_MIN = 10  # jeda waktu minimum antara transaksi (detik) - Ubah sesuai keinginan Anda
JEDA_MAX = 20  # jeda waktu maksimum antara transaksi (detik) - Ubah sesuai keinginan Anda

# Fungsi sleep_progress() sama seperti sebelumnya
def sleep_progress(secs):
    for i in tqdm(range(secs), desc='Menunggu', bar_format="{desc}: {n_fmt}s / {total_fmt}s {bar}", colour='green'):
        time.sleep(1)

def send_cro_to_many_wallets(privatekeys, destinations, amount_in_cro):
    w3 = Web3(Web3.HTTPProvider("https://evm.cronos.org/"))
    total_berhasil = 0
    total_gagal = 0
    total_cro_terkirim = 0

    for privatekey in privatekeys:
        account = w3.eth.account.from_key(privatekey)
        address = account.address
        token_balance = w3.eth.get_balance(w3.to_checksum_address(address))
        proc_of_min = int(token_balance * TST_FROM / 100)
        proc_of_max = int(token_balance * TST_TO / 100)
        amount_in_wei = int(amount_in_cro * 10**18)
        aw_round = amount_in_wei

        for destination in destinations:
            try:
                nonce = w3.eth.get_transaction_count(address)
                gas_price = w3.eth.gas_price
                
                tx = {
                    'from': address,
                    'to': Web3.to_checksum_address(destination),
                    'value': aw_round,
                    'nonce': nonce,
                    'gas': 21000,
                    'gasPrice': int(gas_price),  # Ubah ke integer
                    'chainId': w3.eth.chain_id,
                }

                sign = account.sign_transaction(tx)
                hash_ = w3.eth.send_raw_transaction(sign.rawTransaction)
                print("Alamat:", address)
                print("Tujuan:", destination)
                print("Hash Transaksi:", hash_.hex())
                print("Menunggu konfirmasi...")

                # Menunggu konfirmasi
                tx_receipt = w3.eth.wait_for_transaction_receipt(hash_, timeout=140)
                print("Berhasil mengirim CRO:", aw_round / 10**18)
                total_berhasil += 1
                total_cro_terkirim += amount_in_cro
                
                # Tambahkan jeda waktu antara transaksi
                jeda = random.randint(JEDA_MIN, JEDA_MAX)
                print(f"Menunggu {jeda} detik sebelum transaksi berikutnya...")
                sleep_progress(jeda)

            except exceptions.InsufficientFunds:
                print("Alamat:", address)
                print("Saldo tidak mencukupi untuk mengirim transaksi.")
                total_gagal += 1
            except exceptions.ValueError:
                print("Alamat:", address)
                print("Gas price terlalu tinggi.")
                total_gagal += 1
            except Exception as e:
                print("Alamat:", address)
                print("Kesalahan:", e)
                total_gagal += 1

    return total_berhasil, total_gagal, total_cro_terkirim

def main():
    total_berhasil, total_gagal, total_cro_terkirim = send_cro_to_many_wallets(privatekeys, destinations, 0.1) # Mengirim 0.1 CRO ke setiap alamat tujuan
    print(f"Pengujian selesai.")
    print(f"Total wallet berhasil dikirim: {total_berhasil}")
    print(f"Total wallet gagal dikirim: {total_gagal}")
    print(f"Total CRO terkirim: {total_cro_terkirim} CRO")

if __name__ == "__main__":
    main()

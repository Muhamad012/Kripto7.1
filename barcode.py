from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA
import base64
import hashlib

# Fungsi untuk melakukan enkripsi AES 256 OCB
def encrypt_aes_ocb(data, key):
    cipher = AES.new(key, AES.MODE_OCB)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

# Fungsi untuk menghitung hash SHA-1
def calculate_sha1(data):
    sha1_hash = hashlib.sha1(data.encode('utf-8')).digest()
    return base64.b64encode(sha1_hash).decode('utf-8')

# Fungsi untuk mencetak barcode
def generate_barcode():
    # Memasukkan data dari pengguna
    nomor_pengiriman = input("Masukkan Nomor Pengiriman: ")
    tanggal_kirim = input("Masukkan Tanggal Kirim: ")
    kode_cabang = input("Masukkan Kode Cabang: ")

    # Menggabungkan data yang akan dienkripsi
    data_to_encrypt = f"{nomor_pengiriman}-{tanggal_kirim}-{kode_cabang}"

    # Menghasilkan kunci AES
    aes_key = get_random_bytes(32)

    # Melakukan enkripsi AES OCB
    encrypted_data = encrypt_aes_ocb(data_to_encrypt, aes_key)

    # Menghitung hash SHA-1
    sha1_hash = calculate_sha1(data_to_encrypt)

    # Menggabungkan hasil enkripsi dan hash
    barcode_data = f"{encrypted_data}-{sha1_hash}"

    print("Barcode yang dihasilkan:", barcode_data)

# Contoh penggunaan
if __name__ == "__main__":
    generate_barcode()

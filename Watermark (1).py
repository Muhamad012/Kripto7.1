from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

# Fungsi untuk mengenkripsi data JSON dengan AES 256 CTR dan encoding Base64
def encrypt_json(data, key):
    json_string = json.dumps(data)
    nonce = get_random_bytes(8)
    key = key.ljust(32)[:32]
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CTR, nonce=nonce)
    encrypted_data = cipher.encrypt(json_string.encode('utf-8'))
    encrypted_message = base64.b64encode(nonce + encrypted_data).decode('utf-8')

    return encrypted_message

# Fungsi untuk mendekripsi data JSON dengan AES 256 CTR dan decoding Base64
def decrypt_and_display(watermark, key):
    decoded_watermark = base64.b64decode(watermark.encode('utf-8'))
    nonce = decoded_watermark[:8]
    key = key.ljust(32)[:32]
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CTR, nonce=nonce)
    decrypted_data = cipher.decrypt(decoded_watermark[8:])
    json_data = decrypted_data.decode('utf-8')
    data_object = json.loads(json_data)
    print("Hasil Dekripsi:")
    print(json.dumps(data_object, indent=2))

username = input("Masukkan username: ")
password = input("Masukkan password: ")
status = input("Masukkan status: ")

data_to_encrypt = {
    "username": username,
    "password": password,
    "status": status
}
encryption_key = input("Masukkan kunci enkripsi: ")
encrypted_data = encrypt_json(data_to_encrypt, encryption_key)
with open("encrypted_data_watermark.txt", "w") as file:
    file.write(encrypted_data)

print("Data JSON telah dienkripsi dan disimpan sebagai watermark.")
with open("encrypted_data_watermark.txt", "r") as file:
    encrypted_watermark = file.read()
decrypt_and_display(encrypted_watermark, encryption_key)

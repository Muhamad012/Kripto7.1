from PIL import Image, ImageDraw, ImageFont
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

# Fungsi untuk mengenkripsi data JSON dengan AES 256 CTR dan encoding Base64
def encrypt_json(data, key):
    # Mengonversi data JSON menjadi string
    json_string = json.dumps(data)

    # Menghasilkan nonce (IV) dengan panjang 8 byte
    nonce = get_random_bytes(8)

    # Mengonversi kunci menjadi panjang 32 byte
    key = key.ljust(32)[:32]

    # Membuat objek cipher AES 256 CTR
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CTR, nonce=nonce)
    
    # Melakukan enkripsi
    encrypted_data = cipher.encrypt(json_string.encode('utf-8'))

    # Mengembalikan nonce dan data terenkripsi
    return encrypted_data, nonce

# Contoh data JSON
data_to_encrypt = {
    "username": "Dobleh",
    "password": "Aslinya_Dua_Orang",
    "status": "active"
}

# Kunci enkripsi (Anda dapat mengganti kunci ini sesuai kebutuhan)
encryption_key = "dobleh_yang_terbaik"

# Enkripsi data JSON dan simpan sebagai watermark
encrypted_data, nonce = encrypt_json(data_to_encrypt, encryption_key)

# Simpan sebagai watermark (contoh: file)
with open("encrypted_data_watermark.txt", "wb") as file:
    file.write(base64.b64encode(nonce + encrypted_data))

print("Data JSON telah dienkripsi dan disimpan sebagai watermark.")



# Fungsi untuk mendekripsi data JSON dengan AES 256 CTR dan decoding Base64
def decrypt_and_display(watermark, key):
    # Baca watermark dari file (atau sesuaikan sumbernya)
    with open("encrypted_data_watermark.txt", "r") as file:
    encrypted_watermark = file.read()
    
    # Mengambil nonce (IV) dari watermark
    nonce = decoded_watermark[:8]

    # Mengonversi kunci menjadi panjang 32 byte
    key = key.ljust(32)[:32]

    # Membuat objek cipher AES 256 CTR
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CTR, nonce=nonce)

    # Melakukan dekripsi
    decrypted_data = cipher.decrypt(decoded_watermark[8:])

    # Mengonversi data terdekripsi dari bytes ke string JSON
    json_data = decrypted_data.decode('utf-8')

    # Mengonversi string JSON ke objek Python
    data_object = json.loads(json_data)

    # Menampilkan hasil dekripsi
    print("Hasil Dekripsi:")
    print(json.dumps(data_object, indent=2))

# Fungsi untuk membuat gambar mobil dan menyisipkan watermark
def create_car_image_with_watermark(decrypted_data):
    # Membuat gambar kosong dengan latar belakang putih
    image = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(image)

    # Menggambar gambar mobil (hanya contoh)
    car_image_path = "car_image.png"  # Ganti dengan path gambar mobil yang sesuai
    car_image = Image.open(car_image_path)
    image.paste(car_image, (50, 50))

    # Menambahkan teks watermark pada gambar
    font = ImageFont.load_default()
    watermark_text = json.dumps(decrypted_data, indent=2)
    draw.text((10, 10), watermark_text, fill='black', font=font)

    # Simpan gambar yang telah diubah
    image.save("car_image_with_watermark.png")

# Dekripsi dan tampilkan hasilnya
decrypt_and_display("encrypted_data_watermark.txt", encryption_key)

# Gunakan data terdekripsi untuk membuat gambar dengan watermark
create_car_image_with_watermark(data_object)

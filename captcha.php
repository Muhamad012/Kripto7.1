<?php
session_start();

// Fungsi untuk membuat CAPTCHA
function generateCaptcha($length = 6)
{
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

// Membuat CAPTCHA baru jika belum ada dalam session atau jika sudah kadaluarsa
if (!isset($_SESSION['captcha']) || (isset($_SESSION['captcha_time']) && time() - $_SESSION['captcha_time'] > 300)) {
    $_SESSION['captcha'] = generateCaptcha();
    $_SESSION['captcha_time'] = time();
}

// Mengambil 10 karakter pertama dari CAPTCHA sebagai kode CAPTCHA yang akan ditampilkan
$captchaCode = substr($_SESSION['captcha'], 0, 10);

// Encode CAPTCHA dengan Base64 untuk ditampilkan sebagai gambar atau teks
$encodedCaptcha = base64_encode($_SESSION['captcha']);

// Tampilkan form login beserta kode CAPTCHA
echo '<form method="post" action="process_login.php">';
echo 'Username: <input type="text" name="username"><br>';
echo 'Password: <input type="password" name="password"><br>';
echo '<img src="data:image/png;base64,' . $encodedCaptcha . '" alt="Captcha"><br>';
echo 'Captcha: <input type="text" name="captcha"><br>';
echo '<input type="submit" value="Login">';
echo '</form>';
?>

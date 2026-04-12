# jelaskan tentang perintah ini
# images_pt = torch.zeros([32, 28, 28, 3])

import torch
import tensorflow as tf

images_pt = torch.zeros([32, 28, 28, 3])

images_pt

# Penjelasann
# 1. torch.zeros
# - Fungsi ini adalah untuk membuat tensor berisi angka 0
# Jadi semua elemen di dalamnya otomatis menjadi 0

# 2. [32, 28, 28, 3]
# - 32 : Jumlah data (biasanya jumlah gambar / batch size)
# - 28 : Tinggi gambar (height)
# - 28 : Lebar gambar (width)
# - 3 : Jumlah channel warna (RGB)

# Jadi perintah di atas adalah untuk membuat 32 buah gambar kosong berukuran:
# - 28 x 28 pixel
# - dengan 3 warna channel (RGB)
# - semua pixel = 0 (hitam)

# Itulah kenapa setiap angka yang muncul di outputnya adalah 0, karena dari perintahnya adalah membuat tensor berisi angka 0

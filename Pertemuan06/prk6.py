from PIL import Image
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import math

from skimage.metrics import (
    peak_signal_noise_ratio as psnr,
    structural_similarity as ssim
)

# Menyiapkan folder untuk menyimpan hasil
folder_hasil = Path("hasil")
folder_hasil.mkdir(exist_ok=True)

# Membuka gambar asli
img_asli = Image.open("gambar.png").convert("L")  # Mengubah ke grayscale

# Mengubah gambar menjadi array numpy
arr_asli = np.array(img_asli)

print("Gambar berhasil dibuka")
print("Dimensi gambar asli:", img_asli.size)
print("Mode Warna gambar asli:", img_asli.mode)
print("Bentuk array gambar asli:", arr_asli.shape)

#fungsi menghitung MSE
def hitung_mse(gambar_asli, gambar_kompresi):

   selisih = (
      gambar_asli.astype(np.float64) -
      gambar_kompresi.astype(np.float64)
   )

   mse = np.mean(selisih ** 2)

   return mse
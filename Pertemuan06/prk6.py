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

#daftar gambar jpeg
gambar_jpeg = {
   "JPEG 10": "hasil/jpeg_10.jpeg",
   "JPEG 50": "hasil/jpeg_50.jpeg",
   "JPEG 90": "hasil/jpeg_90.jpeg"
}

print("\nMULAI PERHITUNGAN MSE, PSNR MANUAL")

for name, nama_file in daftar_jpeg.items():
   img_kompresi = Image.open(nama_file).convert("RGB")
   arr_kompresi = np.array(img_kompresi)

   #memastikan dimensi gambar sama
if arr_asli.shape != arr_kompresi.shape:
     raise ValueError(f"Dimensi gambar tidak sama: {nama_file}")

#menghitung MSE
mse = hitung_mse(arr_asli, arr_kompresi)

#menghitung PSNR
psnr = hitung_psnr_manual(mse)
print(f"\n{name}")
print(f"MSE: {mse:.4f}")
print(f"PSNR: {psnr:.2f} dB")

print("\nPerbandingan PNSR Manual dan Scikit-image")


for nama, nama_file in daftar_jpeg.items():

    img_kompresi = Image.open(nama_file).convert("RGB")
    arr_kompresi = np.array(img_kompresi)

    # Menghitung MSE
    mse = hitung_mse(arr_asli, arr_kompresi)

    # PSNR manual
    psnr_manual = hitung_psnr_manual(mse)

    # PSNR menggunakan scikit-image
    psnr_skimage = peak_signal_noise_ratio(
        arr_asli,
        arr_kompresi,
        data_range=255
    )

    print(f"\n{nama}")
    print(f"PSNR Manual  : {psnr_manual:.2f} dB")
    print(f"PSNR Skimage : {psnr_skimage:.2f} dB")
    print("\nPERHITUNGAN SSIM")

for nama, nama_file in daftar_jpeg.items():

    img_kompresi = Image.open(nama_file).convert("RGB")
    arr_kompresi = np.array(img_kompresi)

    # Menghitung SSIM
    ssim = structural_similarity(
        arr_asli,
        arr_kompresi,
        channel_axis=2,
        data_range=255
    )

    print(f"{nama}")
    print(f"SSIM : {ssim:.4f}\n")
# Sistem Multimedia

Kumpulan tugas praktikum mata kuliah Sistem Multimedia. Setiap pertemuan disimpan dalam folder terpisah (`Pertemuan01` … `Pertemuan06`) dan berisi skrip Python beserta media pendukung dan hasilnya.

## Daftar Isi

| Pertemuan | Topik | Skrip Utama |
|-----------|------|-------------|
| 01 | Pengenalan & penyiapan media | — (folder kosong) |
| 02 | Representasi data: audio & teks | `hitung.py`, `text2.py` |
| 03 | Portofolio | `port-3/` (folder kosong) |
| 04 | Encoding audio (FFmpeg) | `batch_encoding.py` |
| 05 | Pemrosesan citra: warna, kompresi, histogram, resizing | `prk5.py` |
| 06 | Pengukuran kualitas citra: MSE, PSNR, SSIM | `prk6.py` |

---

## Pertemuan01 — Pengenalan & Penyiapan Media

Dua folder kosong untuk menyimpan media mentah dan hasil pemrosesan.

- `MediaAseli/` — tempat media sumber (mentah)
- `MediaHasil/` — tempat media hasil olahan

## Pertemuan02 — Representasi Data: Audio & Teks

Menghitung ukuran file audio digital dan memeriksa penyandian karakter teks.

- `hitung.py` — menghitung estimasi ukuran file audio (byte) dari kombinasi *sample rate* (8000, 44100, 48000 Hz), *bit depth* (8, 16, 24 bit), jumlah kanal (mono/stereo), dan durasi 10 detik.
- `text2.py` — menampilkan representasi UTF-8 (dalam byte) dari tiap karakter pada sebuah string.

Menjalankan:

```bash
cd Pertemuan02
python3 hitung.py
python3 text2.py
```

## Pertemuan03 — Portofolio

Folder `port-3/` yang dialokasikan untuk portofolio tugas (saat ini kosong).

## Pertemuan04 — Encoding Audio dengan FFmpeg

Konversi batch file audio `.wav` menjadi berbagai format dan *bitrate* menggunakan FFmpeg.

- `batch_encoding.py` — mengonversi 5 file `music1.wav` … `music5.wav` ke MP3 128 kbps melalui `subprocess` + FFmpeg, lalu menyimpan hasilnya ke folder `audio_mp3/`.
- File sumber: `music1.wav` … `music5.wav`
- Folder hasil berisi keluaran encoding pada beberapa *bitrate*:
  - `audio_mp3/` — MP3 (64, 128, 320 kbps)
  - `audio_aac/` — AAC yang dikonversi ke `.mp3` (64, 128, 320 kbps)
  - `audio_flac/` — FLAC yang dikonversi ke `.mp3` (64, 128, 320 kbps)

Prasyarat: FFmpeg terpasang dan tersedia di `PATH`.

```bash
cd Pertemuan04
python3 batch_encoding.py
```

## Pertemuan05 — Pemrosesan Citra

Manipulasi citra menggunakan Pillow dan Matplotlib. Sumber: `image.JPG`. Semua keluaran disimpan di `hasil/`.

- `prk5.py` melakukan:
  1. **Konversi model warna** — RGB, Grayscale, HSV, disimpan sebagai PNG + visualisasi perbandingan.
  2. **Kompresi citra** — JPEG (kualitas 10, 50, 90), PNG (lossless), WebP (kualitas 10, 50, 90), lengkap dengan tabel perbandingan ukuran file.
  3. **Histogram** — histogram RGB, histogram Grayscale, serta perbandingan histogram sebelum & sesudah kompresi JPEG kualitas 10.
  4. **Resizing** — mengecilkan citra ke 50%, 25%, 10% (resampling Lanczos) dan visualisasi perbandingannya.

Prasyarat: `pillow`, `matplotlib`.

```bash
cd Pertemuan05
python3 prk5.py
```

## Pertemuan06 — Pengukuran Kualitas Citra

Mengukur seberapa besar kualitas citra menurun akibat kompresi, dengan membandingkan citra asli (`gambar.png`) terhadap hasil JPEG (kualitas 10, 50, 90) dan WebP. Keluaran disimpan di `hasil/`.

- `prk6.py` menghitung:
  - **MSE** (*Mean Squared Error*) — fungsi manual menggunakan NumPy.
  - **PSNR** (*Peak Signal-to-Noise Ratio*) — perhitungan manual dan menggunakan `skimage.metrics.peak_signal_noise_ratio`.
  - **SSIM** (*Structural Similarity Index*) — menggunakan `skimage.metrics.structural_similarity`.

Prasyarat: `pillow`, `numpy`, `matplotlib`, `scikit-image`.

```bash
cd Pertemuan06
python3 prk6.py
```

---

## Daftar Dependensi

Sebagian besar skrip membutuhkan paket Python berikut. Pasang sesuai kebutuhan:

```bash
pip install pillow matplotlib numpy scikit-image
```

Untuk Pertemuan04, FFmpeg harus terpasang di sistem:

```bash
# macOS (Homebrew)
brew install ffmpeg
```

## Struktur Folder

```
Sistem Multimedia/
├── Pertemuan01/        # MediaAseli/, MediaHasil/ (kosong)
├── Pertemuan02/        # hitung.py, text2.py
├── Pertemuan03/        # port-3/ (kosong)
├── Pertemuan04/        # batch_encoding.py + file WAV + hasil audio_mp3/aac/flac
├── Pertemuan05/        # prk5.py, image.JPG, hasil/
├── Pertemuan06/        # prk6.py, gambar.png, hasil/
└── README.md
```

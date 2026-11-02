
import subprocess
from pathlib import Path

# Folder tempat skrip berada
folder = Path(__file__).resolve().parent

# Buat folder khusus untuk mp3 jika belum ada
folder_mp3 = folder / "audio_mp3"
folder_mp3.mkdir(exist_ok=True)

# Daftar file audio sumber
daftar_file = [
    "music1.wav",
    "music2.wav",
    "music3.wav",
    "music4.wav",
    "music5.wav"
]

print("=" * 45)
print("BATCH ENCODING AUDIO KE MP3 128 KBPS")
print("=" * 45)

berhasil = 0
gagal = 0

# Proses encoding setiap file audio
for nama_file in daftar_file:
    sumber = folder / nama_file
    # Menyimpan hasil langsung ke folder audio_mp3
    hasil = folder_mp3 / f"{sumber.stem}_128k.mp3"

    print(f"\nMemproses: {nama_file}")

    # Periksa keberadaan file sumber
    if not sumber.exists():
        print(f"Gagal: File {nama_file} tidak ditemukan")
        gagal += 1
        continue

    # Perintah FFmpeg
    perintah = [
        "ffmpeg",
        "-y",
        "-i", str(sumber),
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        str(hasil)
    ]

    # Jalankan FFmpeg tanpa menampilkan log panjang
    proses = subprocess.run(
        perintah,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Periksa hasil proses encoding
    if proses.returncode == 0 and hasil.exists():
        print(f"Berhasil: {hasil.name} (disimpan di {folder_mp3.name}/)")
        berhasil += 1
    else:
        print(f"Gagal: {nama_file}")
        gagal += 1

# Ringkasan hasil encoding
print("\n" + "=" * 45)
print("RINGKASAN PROSES ENCODING")
print("=" * 45)
print(f"Jumlah file diproses : {berhasil + gagal}")
print(f"Berhasil             : {berhasil}")
print(f"Gagal                : {gagal}")
print("=" * 45)
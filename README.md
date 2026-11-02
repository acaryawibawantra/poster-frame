INI TOOLS WEB REQ BY ME DAN DI BUAT OTOMATIS SAMA HERMES AGENT DAWG KWKKWKWKW, TANPA NYENTUH IDE, JUST 2X PROMNT

# Poster → Feed 4:5

Utilitas satu file untuk mengubah poster ukuran apa pun jadi kanvas putih **1080 × 1350 px (4:5)** siap posting Instagram feed. Poster tetap utuh (tanpa crop) — sisa ruang otomatis putih.

## Pakai
Buka `index.html` di browser (atau versi online). Pilih/tarik poster → hasil muncul di preview → **Simpan ke Galeri**.

- Bisa banyak file sekaligus
- Mode **Utuh** (contain, default) atau **Penuh** (cover, crop tepi)
- Background bisa diganti, margin dalam 0–20%, output JPG/PNG + kualitas
- **Kompres otomatis** — output JPG diturunkan kualitasnya (binary search) sampai di bawah batas, default 2 MB
- EXIF orientasi HP otomatis diputar benar
- Semua proses lokal di browser — tidak ada file yang diunggah ke server

### Menyimpan
- **iPhone/Android:** tombol Simpan membuka menu berbagi → pilih **Simpan Gambar**
- **Mac/PC:** file langsung terunduh ke folder Download (tidak lewat share sheet)
- **iPhone tanpa share support / browser in-app:** terbuka layar penuh → tekan & tahan gambar → **Simpan ke Foto**
- Browser dalam Telegram/Instagram memblokir download — buka dulu di Safari/Chrome

## CLI (opsional)
```bash
python3 convert_poster.py poster1.jpg poster2.png
python3 convert_poster.py --mode cover --pad 3 --bg "#ffffff" poster.jpg -o hasil.jpg
```

## Struktur
- `index.html` — seluruh aplikasi (HTML + CSS + JS, tanpa dependency)
- `convert_poster.py` — versi CLI dengan logika geometri yang sama (Pillow)
- `.nojekyll` — agar GitHub Pages tidak memproses lewat Jekyll

## Logika geometri
`scale = min(1080/w, 1350/h)` untuk mode utuh, `max(...)` untuk mode penuh; gambar digambar terpusat di kanvas 1080×1350 dengan latar solid.

---

## Kredit
Dibuat oleh **Hermes Agent** (Nous Research) — 2 November 2026 — atas permintaan I Dewa Nyoman Acarya Wibawantra.
Agent documentation: https://hermes-agent.nousresearch.com


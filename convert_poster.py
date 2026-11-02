#!/usr/bin/env python3
"""Replika CLI dari logika index.html — poster apa pun -> kanvas putih 1080x1350 (4:5).

Dipakai untuk verifikasi geometri dan sebagai fallback batch/CLI.
Pemakaian:
    python3 convert_poster.py poster1.jpg poster2.png
    python3 convert_poster.py --mode cover --bg "#ffffff" --pad 0 in.jpg -o out.jpg
"""
import argparse
import sys
from pathlib import Path

from PIL import Image, ImageOps

OUT_W, OUT_H = 1080, 1350


def convert(src: Path, out: Path, mode="contain", bg="#ffffff", pad_pct=0.0,
            quality=92) -> tuple[int, int]:
    img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    sw, sh = img.size
    pad = max(0.0, min(20.0, pad_pct)) / 100.0
    avail_w = OUT_W * (1 - 2 * pad)
    avail_h = OUT_H * (1 - 2 * pad)

    scale = (min if mode == "contain" else max)(avail_w / sw, avail_h / sh)
    dw = max(1, round(sw * scale))
    dh = max(1, round(sh * scale))
    resized = img.resize((dw, dh), Image.LANCZOS)

    canvas = Image.new("RGB", (OUT_W, OUT_H), bg)
    if mode == "cover":
        box = (round(OUT_W * pad), round(OUT_H * pad),
               round(OUT_W * pad + avail_w), round(OUT_H * pad + avail_h))
        # crop bagian tengah poster yang jatuh di dalam kotak avail
        left = max(0, (dw - (box[2] - box[0])) // 2)
        top = max(0, (dh - (box[3] - box[1])) // 2)
        right = left + (box[2] - box[0])
        bottom = top + (box[3] - box[1])
        canvas.paste(resized.crop((left, top, right, bottom)), (box[0], box[1]))
    else:
        canvas.paste(resized, ((OUT_W - dw) // 2, (OUT_H - dh) // 2))

    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix.lower() in (".jpg", ".jpeg"):
        canvas.save(out, "JPEG", quality=quality, optimize=True)
    else:
        canvas.save(out, "PNG")
    return dw, dh


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("-o", "--out", help="output file (hanya untuk 1 gambar)")
    ap.add_argument("--mode", choices=["contain", "cover"], default="contain")
    ap.add_argument("--bg", default="#ffffff")
    ap.add_argument("--pad", type=float, default=0.0, help="margin dalam, persen (0-20)")
    ap.add_argument("--quality", type=int, default=92)
    a = ap.parse_args()

    if a.out and len(a.images) > 1:
        print("--out hanya untuk 1 gambar", file=sys.stderr)
        return 2

    for name in a.images:
        src = Path(name)
        out = Path(a.out) if a.out else src.with_name(f"{src.stem}_feed.jpg")
        dw, dh = convert(src, out, a.mode, a.bg, a.pad, a.quality)
        with Image.open(out) as o:
            print(f"{src.name} -> {out.name}  canvas={o.size[0]}x{o.size[1]}  poster={dw}x{dh}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

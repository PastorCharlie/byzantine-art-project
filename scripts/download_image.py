#!/usr/bin/env python3
"""
Download and optionally resize an image for the Byzantine Art Project corpus.

Usage:
    python3 scripts/download_image.py <url> <output_path> [max_width]

Arguments:
    url          Source URL (Wikimedia Commons file URL)
    output_path  Local path where the image should be saved
    max_width    Optional max width in pixels; if provided, downsample so
                 neither dimension exceeds this value (preserves aspect ratio).
                 Omit to download as-is.

Behavior:
    - Sets a project-identifying User-Agent for Wikimedia.
    - Downloads to a temp file first, then either copies or resizes to
      the final output path.
    - For resize: uses PIL Lanczos, JPEG quality 92.
    - Converts TIFF/PNG inputs to JPEG when output_path ends in .jpg/.jpeg.
    - Prints original and final dimensions to stdout.
    - Exits non-zero on any failure with a clear error message.
"""
import sys
import os
import shutil
import tempfile
import urllib.request
import urllib.error
from pathlib import Path

USER_AGENT = "ByzantineArtProject/1.0 (pastormango@pm.me)"
JPEG_QUALITY = 92


def fail(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def download(url: str, dest: str) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp, open(dest, "wb") as out:
            while True:
                chunk = resp.read(1 << 16)
                if not chunk:
                    break
                out.write(chunk)
    except urllib.error.URLError as e:
        fail(f"download failed: {e}")


def main() -> None:
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        fail("usage: download_image.py <url> <output_path> [max_width]")

    url = sys.argv[1]
    output_path = Path(sys.argv[2])
    max_width = int(sys.argv[3]) if len(sys.argv) == 4 else None

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(url).suffix or ".bin") as tmp:
        tmp_path = tmp.name

    try:
        download(url, tmp_path)

        # If no resize and same format, just move.
        suffix_in = Path(tmp_path).suffix.lower()
        suffix_out = output_path.suffix.lower()
        needs_pillow = (max_width is not None) or (suffix_in != suffix_out)

        if not needs_pillow:
            shutil.move(tmp_path, output_path)
            size_kb = output_path.stat().st_size // 1024
            print(f"saved: {output_path} ({size_kb} KB)")
            return

        try:
            from PIL import Image
        except ImportError:
            fail("Pillow not installed; cannot resize or convert. install with: pip install Pillow")

        with Image.open(tmp_path) as img:
            original = img.size
            if max_width is not None:
                img.thumbnail((max_width, max_width * 4), Image.LANCZOS)
            final = img.size

            if suffix_out in (".jpg", ".jpeg"):
                img = img.convert("RGB")
                img.save(output_path, quality=JPEG_QUALITY, optimize=True)
            else:
                img.save(output_path)

        size_kb = output_path.stat().st_size // 1024
        print(f"original: {original[0]}x{original[1]}")
        print(f"saved: {output_path} ({final[0]}x{final[1]}, {size_kb} KB)")
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


if __name__ == "__main__":
    main()

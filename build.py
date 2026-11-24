# /// script
# requires-python = ">=3.12"
# dependencies = ["fonttools", "brotli", "pillow"]
# ///
"""Build web fonts, fonts.css and preview.png from the source font files.

Run with ``uv run build.py`` after adding or changing a font in ``FONTS``.
"""

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent


@dataclass(frozen=True)
class Font:
    """One source font file and the CSS family and weight it is served as."""

    file: str
    family: str
    weight: int
    label: str


FONTS = [
    Font("futura-no2-demi-bold.ttf", "Futura No2 D", 600, "Futura No2 D · Demi Bold 600"),
    Font("radiance-regular.otf", "Radiance", 400, "Radiance · Regular 400"),
    Font("reaver-regular.otf", "Reaver", 400, "Reaver · Regular 400"),
    Font("reaver-semibold.otf", "Reaver", 600, "Reaver · SemiBold 600"),
]

SAMPLE = "The quick brown fox jumps over the lazy dog 0123456789"

# Preview colors work on both GitHub's light and dark themes.
BACKGROUND = "#1b1f24"
LABEL_COLOR = "#8b949e"
TEXT_COLOR = "#f0f3f6"


def write_if_changed(path: Path, data: bytes) -> None:
    """Write ``data`` to ``path`` unless the file already holds exactly that."""
    if path.exists() and path.read_bytes() == data:
        return
    path.write_bytes(data)
    print(f"wrote {path.name}")


def build_font(font: Font) -> None:
    """Set the source file's OS/2 weight to the CSS weight and write its woff2 copy."""
    source = ROOT / font.file
    tt = TTFont(source, recalcTimestamp=False)
    if tt["OS/2"].usWeightClass != font.weight:
        tt["OS/2"].usWeightClass = font.weight
        buffer = BytesIO()
        tt.save(buffer)
        write_if_changed(source, buffer.getvalue())

    tt.flavor = "woff2"
    buffer = BytesIO()
    tt.save(buffer)
    write_if_changed(source.with_suffix(".woff2"), buffer.getvalue())


def build_css() -> None:
    """Write fonts.css with one woff2 @font-face rule per font."""
    rules = [
        "@font-face {\n"
        f'  font-family: "{font.family}";\n'
        f'  src: url("{Path(font.file).with_suffix(".woff2").name}") format("woff2");\n'
        f"  font-weight: {font.weight};\n"
        "  font-style: normal;\n"
        "  font-display: swap;\n"
        "}\n"
        for font in FONTS
    ]
    write_if_changed(ROOT / "fonts.css", "\n".join(rules).encode())


def build_preview() -> None:
    """Render preview.png with a label and a sample line in each font."""
    scale = 2
    pad, label_size, text_size, row_gap = 32 * scale, 16 * scale, 34 * scale, 28 * scale

    rows = [
        (
            font,
            ImageFont.truetype(ROOT / font.file, label_size),
            ImageFont.truetype(ROOT / font.file, text_size),
        )
        for font in FONTS
    ]
    width = pad * 2 + max(int(text.getlength(SAMPLE)) for _, _, text in rows)
    row_height = label_size + 10 * scale + text_size
    height = pad * 2 + len(rows) * row_height + (len(rows) - 1) * row_gap

    image = Image.new("RGB", (width, height), BACKGROUND)
    draw = ImageDraw.Draw(image)
    y = pad
    for font, label, text in rows:
        draw.text((pad, y), font.label, font=label, fill=LABEL_COLOR)
        draw.text((pad, y + label_size + 10 * scale), SAMPLE, font=text, fill=TEXT_COLOR)
        y += row_height + row_gap

    buffer = BytesIO()
    image.save(buffer, "PNG", optimize=True)
    write_if_changed(ROOT / "preview.png", buffer.getvalue())


def main() -> None:
    """Build every output file from FONTS."""
    for font in FONTS:
        build_font(font)
    build_css()
    build_preview()


if __name__ == "__main__":
    main()

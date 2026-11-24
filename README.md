# 🔤 Fonts

Fonts I use across my projects, served through [jsDelivr](https://www.jsdelivr.com/).

## 📦 Files

| Family | Weight | Files |
|---|---|---|
| Futura No2 D | 600 | `futura-no2-demi-bold.ttf`, `.woff2` |
| Radiance | 400 | `radiance-regular.otf`, `.woff2` |
| Reaver | 400 | `reaver-regular.otf`, `.woff2` |
| Reaver | 600 | `reaver-semibold.otf`, `.woff2` |

## 🌐 Web

Link the stylesheet, then use the family names:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Aluerie/Fonts@v1/fonts.css">
```

```css
h1 { font-family: "Reaver", serif; font-weight: 600; }
```

## 🐍 Python (Pillow)

```python
from PIL import ImageFont

font = ImageFont.truetype("reaver-semibold.otf", 32)
```

Pillow needs a local file, so download it first from `https://cdn.jsdelivr.net/gh/Aluerie/Fonts@v1/<file>`.

## 🏷️ Releases

jsDelivr caches tagged files permanently, so after changing any file, push a new tag (`v2`, `v3`, …) and update the links to it.

## 🙏 Credits

- Futura No2 D: © (URW)++ Design & Development.
- Radiance and Reaver: © Valve Corporation, designed by YouWorkForThem (Reaver with Nicolas Massi). Licensed only for fan art under the Steam Subscriber Agreement.

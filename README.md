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

## 💻 Local install

Install the `.ttf` / `.otf` files (Windows can't install `.woff2`). Right-click → **Install for all users**, since some apps, OBS included, don't always pick up per-user fonts. Restart the app afterwards.

Installed fonts show up under these names:

| File | Font picker name | CSS `local()` name |
|---|---|---|
| `futura-no2-demi-bold.ttf` | Futura No2 D Demi Bold | `FuturaNo2D-DemiBold` |
| `radiance-regular.otf` | Radiance | `Radiance-Regular` |
| `reaver-regular.otf` | Reaver | `Reaver-Regular` |
| `reaver-semibold.otf` | Reaver SemiBold | `Reaver-SemiBold` |

### 🎬 OBS text source

Add a **Text (GDI+)** source, click **Select Font**, and pick the font by its font picker name from the table.

### 🎨 OBS browser source / custom CSS

Browser sources take CSS in the **Custom CSS** box. The simplest option doesn't need anything installed; it loads the fonts from the CDN (`@import` must be the first line):

```css
@import url("https://cdn.jsdelivr.net/gh/Aluerie/Fonts@v1/fonts.css");

body { font-family: "Reaver", serif; font-weight: 600; }
```

To use the installed copies instead (works offline), declare them with `local()` and the names from the table:

```css
@font-face {
  font-family: "Reaver";
  src: local("Reaver-SemiBold");
  font-weight: 600;
}

body { font-family: "Reaver", serif; font-weight: 600; }
```

## 🏷️ Releases

jsDelivr caches tagged files permanently, so after changing any file, push a new tag (`v2`, `v3`, …) and update the links to it.

## 🙏 Credits

- Futura No2 D: © (URW)++ Design & Development.
- Radiance and Reaver: © Valve Corporation, designed by YouWorkForThem (Reaver with Nicolas Massi). Licensed only for fan art under the Steam Subscriber Agreement.

# Captcha Dataset Generator with Mask Extraction

Generate datasets of captchas *and* their character-level masks for training computer vision (OCR, segmentation, etc) models.  
**Based on the  [`captcha`](https://github.com/lepture/captcha) library**, enhanced with mask extraction for each character, via my custom fork [`here`](https://github.com/malerbe/captcha).

---

## Features

- Easy generation of captcha images **with associated per-character mask images**
- Customizable captcha length, fonts, noise, backgrounds etc.

---

## 📸 Examples

| Captcha Example                   | Character Mask Example             |
| ---------------------------------- | -----------------------------------|
| ![captcha example](examples/captcha.png) | ![mask example](examples/mask.png)    |

*(Replace the image paths above with your own example images)*

---

## Usage Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/captcha-dataset-generator.git
cd captcha-dataset-generator
```

### 2. Install my improved captcha library (with mask support) /!\ IMPORTANT STEP /!\
```bash
pip install git+https://github.com/your-username/captcha-masks.git
```

### 3. Generate captchas and masks
```bash
python generate_dataset.py --count <nbr of captchas to generate> --output /path/to/output/directory --length <nbr of characters in each captcha>
```

## Requirements

Python 3.7+
captcha (modified fork)
numpy, Pillow, etc. (see requirements.txt)

## License
MIT


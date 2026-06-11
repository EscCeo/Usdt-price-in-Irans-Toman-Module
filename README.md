
[![GitHub](https://img.shields.io/badge/GitHub-EscCeo-black?logo=github)](https://github.com/EscCeo)
[![Telegram](https://img.shields.io/badge/Telegram-xzaliu-26A5E4?logo=telegram)](https://t.me/xzaliu)
[![X](https://img.shields.io/badge/X-xzaliu-black?logo=x)](https://x.com/xzaliu)
[![Requirements](https://img.shields.io/badge/Requirements-View-green)](./requirements.txt)
[![Python](https://img.shields.io/badge/Python-Source-blue?logo=python)](./main.py)
[![PyPI](https://img.shields.io/badge/PyPI-v1.0.0-blue)]([https://pypi.org/project/YOUR-PACKAGE-NAME/](https://pypi.org/project/usdt-price-in-iran-toman-module/))

# USD to IRR Price Scraper 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
[![English Docs](https://img.shields.io/badge/Docs-English-blue)](https://github.com/EscCeo/Usdt-price-in-Iran-s-Toman/blob/main/README.md#usd-to-irr-price-scraper)

[![Persian Docs](https://img.shields.io/badge/Docs-فارسی-success)](https://github.com/EscCeo/Usdt-price-in-Iran-s-Toman/blob/main/README.md#-persian--%D9%81%D8%A7%D8%B1%D8%B3%DB%8C)

A lightweight, robust Python module to fetch the live USD to Iranian Rial (IRR) exchange rate from TGJU.

## Quick Navigation

* [Python Source](#-usage)
* [Requirements](#-installation)
* [Persian / فارسی](#-persian--فارسی)
* [Contact](#-contact)

---

## 📋 Overview

This script scrapes the current dollar price from TGJU, one of Iran's most popular financial websites. Since financial websites often change their HTML structure, the scraper uses multiple fallback methods to remain reliable.

### Features

✅ Resilient to website layout changes

✅ Multiple parsing strategies

✅ Returns clean integer price

✅ Lightweight and fast

✅ Supports English and Persian projects

✅ Easy integration with Telegram bots, dashboards, APIs, and automation tools

---


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## 📦 Install from PyPI

```bash
pip install usdt-price-in-iran-toman-module



## 🛠️ How It Works

1. Sends a GET request to:

https://www.tgju.org/profile/price_dollar_rl

2. Parses the HTML using BeautifulSoup

3. Attempts multiple extraction methods:

* data-price attribute
* CSS class matching
* Regex fallback

4. Cleans the result

5. Returns an integer price or None

---

## 📦 Installation

### Requirements

```bash
pip install requests beautifulsoup4
```

Or install directly from:

```bash
pip install -r requirements.txt
```

### requirements.txt

```txt
requests
beautifulsoup4
```

---

## 🚀 Usage

### Python Source

```python
from dollar_price import get_dollar_price

price = get_dollar_price()

if price:
    print(f"Current Dollar Price: {price:,} Rials")
else:
    print("Failed to fetch price")
```

### Run Directly

```bash
python main.py
```

---

## 📁 Project Structure

```text
dollar-price-scraper/
│
├── main.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🌍 Persian / فارسی

این پروژه قیمت لحظه‌ای دلار را از وب‌سایت TGJU دریافت می‌کند.

ویژگی‌ها:

* سبک و سریع
* مناسب برای ربات‌های تلگرام
* دارای چندین روش جایگزین برای جلوگیری از خرابی اسکریپر
* مناسب برای پروژه‌های فارسی و انگلیسی

---

## 🌐 Use Cases

### Telegram Bots

نمایش قیمت لحظه‌ای دلار

### Discord / WhatsApp Bots

هشدار تغییر قیمت ارز

### Web Dashboards

Flask, FastAPI, Django

### Trading Tools

سیستم‌های آربیتراژ و تحلیل بازار

### Finance Apps

اپلیکیشن‌های مدیریت مالی

### Data Collection

ذخیره‌سازی قیمت‌های تاریخی

---

## 🔧 Customization

### Change Source

```python
url = "https://www.tgju.org/profile/price_dollar_rl"
```

### Add Cache

```python
from functools import lru_cache

@lru_cache(maxsize=1)
def get_dollar_price_cached():
    return get_dollar_price()
```

### Logging & Alerts

Add Telegram, Email, Discord or SMS notifications inside exception handlers.

---

## ⚠️ Important Notes

* Respect TGJU terms of service.
* Add rate limits for frequent requests.
* Website structure may change over time.
* Intended for educational and personal use.

---

## 🤝 Contributing

Contributions are welcome.

Possible improvements:

* Additional fallback selectors
* Gold price support
* Euro support
* Async version
* Unit tests
* API wrapper

---

## 📬 Contact

### GitHub

**@EscCeo**

### Telegram

**@xzaliu**

### X (Twitter)

**@xzaliu**

---

## 👨‍💻 Author

Created and maintained by **Ali (@EscCeo)**

Telegram: **@xzaliu**

X: **@xzaliu**

GitHub: **@EscCeo**

---

## 📄 License

MIT License

Free for personal and commercial use.

---

### ❤️ Made for the Iranian Developer Community

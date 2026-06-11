```markdown
# USD to IRR Price Scraper (TGJU)

A lightweight, robust Python module to fetch the **live USD to Iranian Rial (IRR)** exchange rate from [tgju.org](https://www.tgju.org).

---

## 📋 Overview

This script scrapes the current dollar price from one of Iran's most popular financial websites (**tgju.org**). Because financial sites frequently change their HTML structure, the scraper includes multiple fallback methods to maintain reliability.

**Key Features:**
- Resilient to website layout changes
- Multiple parsing strategies (data attributes, class patterns, regex fallback)
- Returns clean integer price (e.g., `685000`)
- Lightweight — only two dependencies
- Easy to integrate into bots, dashboards, alerts, etc.

---

## 🛠️ How It Works

1. Sends a GET request to `https://www.tgju.org/profile/price_dollar_rl` with a realistic browser User-Agent.
2. Parses the HTML using **BeautifulSoup**.
3. Attempts to extract the price using:
   - `data-price` attribute (most reliable when present)
   - CSS classes containing `price`, `value`, or `live`
   - Regex fallback searching for large comma-separated numbers in the page text
4. Cleans the extracted text (removes commas and non-digits)
5. Returns the price as an **integer** or `None` on failure.

---

## 📦 Installation

```bash
pip install requests beautifulsoup4
```

---

## 🚀 Usage

### Basic Usage

```python
from dollar_price import get_dollar_price

price = get_dollar_price()
if price:
    print(f"Current Dollar Price: {price:,} Rials")
else:
    print("Failed to fetch price")
```

### As a Standalone Script

```bash
python main.py
```

*(The function will print the price when run directly)*

---

## 📁 Project Structure

```
dollar-price-scraper/
├── main.py          # Main module
├── README.md                # This file
└── requirements.txt         # (optional)
```

**requirements.txt**
```txt
requests
beautifulsoup4
```

---

## 🌐 Use Cases

- **Telegram Bots** — Provide real-time dollar prices to users
- **Discord / WhatsApp Bots** — Currency alert bots
- **Web Dashboards** — Live price widgets (Flask, FastAPI, Django)
- **Price Tracking Scripts** — Monitor rate changes and send notifications
- **Trading / Arbitrage Tools** — Integrate with other financial data sources
- **Personal Finance Apps** — Track costs in IRR
- **Data Collection** — Historical price logging (add timestamp + CSV/JSON output)

---

## 🔧 Customization

### Change Source
```python
def get_dollar_price():
    url = "https://www.tgju.org/profile/price_dollar_rl"  # ← Change here
```

### Add Caching
```python
from functools import lru_cache
from datetime import timedelta

@lru_cache(maxsize=1)
def get_dollar_price_cached():
    # Add time-based cache expiration if needed
    return get_dollar_price()
```

### Error Logging / Alerts
Extend the `except` block to send notifications via Telegram, email, etc.

---

## ⚠️ Important Notes

- **Web Scraping**: Respect the site's `robots.txt` and terms of service. Use responsibly.
- **Rate Limiting**: Add delays if calling the function frequently.
- **Maintenance**: Financial websites change often — the scraper is designed to be resilient but may need occasional updates.
- **Legal**: This tool is for personal/educational use. Check local regulations regarding financial data usage.

---

## 🤝 Contributing

Feel free to open issues or pull requests to:
- Add more fallback selectors
- Support other currencies (Euro, Gold, etc.)
- Add async support (`httpx` + `asyncio`)
- Include tests

---

## 📄 License

MIT License — Free to use in personal and commercial projects.

---

**Made with ❤️ for the Iranian developer community**

# remmber to always use official apis for important projects ! 
# @EscCEO on GitHub & @XZALIU on Tg

import requests
from bs4 import BeautifulSoup
import re

def get_dollar_price():
    url = "https://www.tgju.org/profile/price_dollar_rl"  # the url can be changed
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Multiple possible selectors (tgju changes HTML often)
        price = None
        
        price_tag = soup.find('span', {'data-price': True}) or \
                    soup.find('span', class_=re.compile(r'price|value|live', re.I))
        
        if price_tag:
            price_text = price_tag.get('data-price') or price_tag.get_text()
        else:
           # search for numbers with comma in price context
            text = soup.get_text()
            matches = re.findall(r'([\d,]{7,})', text)
            if matches:
                price_text = max(matches, key=len)  # usually the biggest number is the price ( RIP iran citizens 👍 )
            else:
                price_text = None
        
        if price_text:
            # Cleans the price from any unwanted things
            
            price_clean = re.sub(r'[^\d]', '', price_text)
            price_int = int(price_clean)
            print(f"{price_int}")
            return price_int
        else:
            print("⚠️ Could not find price. Site structure may have changed.")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# how it works 
#if __name__ == "__main__":
#    get_dollar_price() 

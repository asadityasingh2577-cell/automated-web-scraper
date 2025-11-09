from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import TARGET_URL, HEADLESS
from db import insert_quote

def create_driver(headless=HEADLESS):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver

def parse_quotes_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    quote_blocks = soup.select(".quote")
    results = []
    for q in quote_blocks:
        text_el = q.select_one(".text")
        author_el = q.select_one(".author")
        tags_el = q.select(".tags .tag")
        text = text_el.get_text(strip=True) if text_el else ""
        author = author_el.get_text(strip=True) if author_el else ""
        tags = ",".join([t.get_text(strip=True) for t in tags_el]) if tags_el else ""
        results.append((text, author, tags))
    return results

def scrape_and_store(headless=HEADLESS, url=TARGET_URL, max_wait=10):
    print("Starting scrape for", url)
    driver = create_driver(headless=headless)
    try:
        driver.get(url)
        WebDriverWait(driver, max_wait).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".quote"))
        )
        html = driver.page_source
    except Exception as e:
        print("Error during page load:", e)
        html = driver.page_source
    finally:
        driver.quit()

    quotes = parse_quotes_from_html(html)
    inserted = 0
    for text, author, tags in quotes:
        insert_quote(text, author, tags)
        inserted += 1
    print(f"Inserted {inserted} quotes into DB.")
    return inserted

if __name__ == "__main__":
    scrape_and_store()

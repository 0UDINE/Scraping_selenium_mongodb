from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def get_scraped_books(pages=1):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://books.toscrape.com/")

    all_books = []
    for _ in range(pages):
        items = driver.find_elements(By.CLASS_NAME, "product_pod")
        for item in items:
            title = item.find_element(By.TAG_NAME, "h3").text
            price_raw = item.find_element(By.CLASS_NAME, "price_color").text
            # Nettoyage du prix : on enlève les symboles (£, Â)
            price = float(price_raw.replace("£", "").replace("Â", ""))
            all_books.append({"title": title, "price": price})

        try:
            driver.find_element(By.CLASS_NAME, "next").find_element(By.TAG_NAME, "a").click()
            time.sleep(1)
        except:
            break

    driver.quit()
    return all_books
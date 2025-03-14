import selenium.webdriver as webdriver 
from selenium.webdriver.chrome.service import Service

from time import sleep
def scrape_website(website):
    print("launching chrome browser...")
    
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        driver.get(website)
        print("successfully navigated to the website")
        html = driver.page_source
        sleep(10)
        
        return html
    finally:
        driver.quit()
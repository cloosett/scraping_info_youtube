from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def search(name_channel):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--incognito")
    options.add_argument('--disable-extensions')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)
    driver.get(f'https://www.youtube.com/results?search_query={name_channel}&sp=EgIQAg%253D%253D')

    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 5000);")
        time.sleep(1)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    youtube_channel_cards = soup.find_all('ytd-channel-renderer', class_='style-scope ytd-item-section-renderer')

    for card in youtube_channel_cards:
        name_channel_elem = card.find(class_='style-scope ytd-channel-name', id='text-container').text.strip()
        username_channel_elem = card.find('span', id='subscribers', class_='style-scope ytd-channel-renderer').text.strip()

        channel_url_about = f'https://www.youtube.com/{username_channel_elem}/about'
        driver.get(channel_url_about)
        time.sleep(4)
        page_source1 = driver.page_source
        soup1 = BeautifulSoup(page_source1, 'lxml')
        info_channel = soup1.find_all('tr', class_='description-item style-scope ytd-about-channel-renderer')
        for info in info_channel:
            print(info.text.strip())

    driver.quit()

if __name__ == "__main__":
    name_channel = input('Введіть назву каналу: ')
    search(name_channel)

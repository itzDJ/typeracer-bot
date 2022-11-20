"""Typeracer bot"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":
    url = input("Paste the join url for the typeracer game: ")
    driver = webdriver.Safari()
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)  # Wait for page to load

    # Push join button
    join = driver.find_element(By.CLASS_NAME, "raceAgainLink")
    join.click()

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    spans = soup.find_all("span", unselectable="on")
    input("Click enter to start in two seconds: ")
    time.sleep(2)
    textbox = driver.find_element(By.CLASS_NAME, "txtInput")
    for span in spans:
        textbox.send_keys(span.text)

    print("Done :)")

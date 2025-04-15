from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

def run():
    driver = webdriver.Chrome(service=Service())
    driver.get("https://comic.naver.com/webtoon?tab=mon")
    sleep(5)

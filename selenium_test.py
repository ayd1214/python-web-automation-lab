import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Selenium이 ChromeDriver를 자동으로 설치하고 경로를 관리하도록 설정
service = Service()

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')  # GUI 없이 브라우저 구동
specific_options.add_argument('--no-sandbox')  # 보안 문제 피할 수 있도록

# ChromeDriver를 자동으로 다운로드하여 사용
driver = webdriver.Chrome(service=service, options=specific_options)

driver.get('https://m.flyasiana.com/C/KR/KO/index')
time.sleep(1)
driver.save_screenshot('BEFORE.png')
driver.quit()
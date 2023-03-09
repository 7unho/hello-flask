from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
service.start()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)  # to keep browser open
driver = webdriver.Remote(service.service_url, options=options)
driver.get(url="https://techblogposts.com/")

# 페이지 스크롤을 내리기 위해 body 엘리먼트를 찾습니다.
body = driver.find_element(By.TAG_NAME, "body")
# li_tags = driver.find_elements(By.CLASS_NAME, "css-qr8q5p")
li_tags = driver.find_elements(By.CLASS_NAME, "css-zhzm1q")

# 스크롤을 내리는 횟수입니다. 원하는 만큼 설정할 수 있습니다.
scrolls = 200000

# 스크롤을 지정한 횟수만큼 내립니다.
while scrolls > 0:
    # li_tags = driver.find_elements(By.CLASS_NAME, "css-qr8q5p")
    li_tags = driver.find_elements(By.CLASS_NAME, "css-zhzm1q")
    
    for li in li_tags:
        print(li.text)
        print(li.find_element(By.TAG_NAME, "a").get_attribute("href"))
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1) # 페이지 로드를 위해 2초간 기다립니다.
    scrolls -= 1

# 스크롤을 내린 후에는 페이지에서 크롤링하고자 하는 정보를 수집합니다.
# 필요한 크롤링 코드를 작성합니다.

# 드라이버를 종료합니다.
driver.quit()

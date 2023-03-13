import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
service.start()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)  # to keep browser open
driver = webdriver.Remote(service.service_url, options=options)
driver.get(url="https://mornit.com/")

# # 스크롤 끝까지 내리기
# while True:
#     # 현재 화면 높이 가져오기
#     last_height = driver.execute_script("return document.body.scrollHeight")

#     # 스크롤 내리기
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # 로딩 대기
#     time.sleep(2)

#     # 새로운 화면 높이 가져오기
#     new_height = driver.execute_script("return document.body.scrollHeight")

#     # try:
#     #     LOAD_MORE_BUTTON = driver.find_element(By.CLASS_NAME, "css-oxkvct")
#     #     if LOAD_MORE_BUTTON:
#     #         LOAD_MORE_BUTTON.click()
#     # except:
#     #     pass
#     # # 더 이상 내릴 스크롤이 없으면 종료
#     if new_height == last_height:
#         break

li_tags = driver.find_elements(By.CLASS_NAME, "post-item")
output = open('techblogpost_crawling.txt', 'a', encoding='utf-8')

for li in li_tags:
    print(li.text)
    # output.write(li.text + "\n");
    print(li.find_element(By.TAG_NAME, "a").get_attribute("href"))
    # output.write(li.find_element(By.TAG_NAME, "a").get_attribute("href") + "\n");
# 웹드라이버 종료
output.close()
driver.quit()


# ts = '1일 전'
# ts = '오늘'
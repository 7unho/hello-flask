# -- Selenium 4.x 버전 이후
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://www.naver.com/')

service = Service(ChromeDriverManager().install())
service.start()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)  # to keep browser open
driver = webdriver.Remote(service.service_url, options=options)
driver.get(url="https://techblogposts.com/")

# # -- Selenium 3.x 버전 이전
# from selenium import webdriver
# import chromedriver_autoinstaller

# chromedriver_autoinstaller.install()
# driver = webdriver.Chrome()
# driver.get('https://www.naver.com/')
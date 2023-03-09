import feedparser
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://techblogposts.com/rss.xml"

# 첫 번째 페이지 로드
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")
entries = soup.find_all("entry")

while True:
    # 마지막 항목 식별
    last_entry = entries[-1]
    last_id = last_entry.find("id").text
    
    # 다음 페이지 로드
    next_url = url + "?after=" + last_id
    print('NEXT URL >>>>>>>>>> ' + next_url)
    response = requests.get(next_url)
    soup = BeautifulSoup(response.content, "xml")
    next_entries = soup.find_all("entry")
    
    # 마지막 항목이 같을 때까지 모든 항목 추출
    if next_entries and next_entries[0].find("id").text == last_id:
        break
    entries += next_entries

# 추출된 항목들에 대한 처리
for entry in entries:
    print(entry.find("title").text)
    print(entry.find("link")["href"])
    print(entry.find("published").text)
    print(entry.find("author").find("name").text)
    print()
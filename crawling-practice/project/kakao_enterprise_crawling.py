import requests
from bs4 import BeautifulSoup

# url = "https://aws.amazon.com/ko/blogs/tech/kurly-sagemaker-product-review-classification-model/"
url = "https://tech.kakaoenterprise.com"

for num in range(1, 200):
    # 페이지 가져오기
    response = requests.get(f"{url}/{num}")

    # BeautifulSoup 객체 만들기
    soup = BeautifulSoup(response.content, "html.parser")

    # article 태그 가져오기
    article_tag = soup.find("article")

    if article_tag is None:
        continue

    output = open(f"../output/content/kakao_enterprise/kakao_enterprise_{num}.txt", "a", encoding="utf-8")
    # article 태그의 내용 출력
    output.write(article_tag.get_text())


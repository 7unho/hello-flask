from medium_api import Medium

medium = Medium('APP_KEY')

user = medium.user(username="nishu-jain")

print(f'{user.fullname} has {user.followers_count} followers.')

user.fetch_articles()
for article in user.articles:
        print(article.title)
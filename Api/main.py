import requests

r=requests.get('https://newsapi.org/v2/everything?qInTitle=egypt%20&from=2024-8-27&to=2024-8-28&sortBy=popularity&language=en&apiKey=a6baf1f50b844ce9b8d789e0665233a5')
content = r.json()
#print (type(content))
articles = content['articles']

print (type(articles))
for article in articles:
   print (article['title'])
import bs4
import requests
author_list = []
for i in range(1, 10):
    base_url = 'http://quotes.toscrape.com/page/{}/'
    res = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    span_text = soup.select('.author')
    for name in span_text:
        author_list.append(name.text)
setauthors = set(author_list)
print(setauthors)
base_url = 'http://quotes.toscrape.com'
res = requests.get('http://quotes.toscrape.com')
soup = bs4.BeautifulSoup(res.text,"lxml")
soup.select('.tag-item')
for item in soup.select(".tag-item"):
    print(item.text)
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print(quotes)
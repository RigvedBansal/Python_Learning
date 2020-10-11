import requests,bs4
result = requests.get("http://www.example.com")
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)
print(soup.select('title')[0].getText())
print(soup.select('h1')[0].getText())
print(soup.select('p')[0].getText())
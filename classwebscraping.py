import bs4,requests
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)
first_item = soup.select('.toctext')[0]
print(first_item)
for item in soup.select('.toctext'):
    print(item.text)
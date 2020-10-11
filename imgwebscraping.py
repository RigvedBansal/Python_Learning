import bs4,requests
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text,'lxml')
computer = soup.select('.thumbimage')[0]
print(computer['src'])
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
f = open(r'C:\Users\HP\Desktop\computerdeepblue.jpeg','wb')
f.write(image_link.content)
f.close()
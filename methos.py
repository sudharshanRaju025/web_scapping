import requests 
from bs4 import BeautifulSoup
url = requests.get("http://localhost:52330/All.html")

# print(url.content)  # binary content

# print(url.text)  # unicode text

# print(url.status_code)  # 200

# print(url.headers)

soup = BeautifulSoup(url.text, 'html.parser')
# print(soup.title)  # <title>Web Page</title>

# print(soup.title.name)  # title

# print(soup.title.string)  # Web Page

# print(soup.select('p'))

# print(soup.select('.nav-item'))

# print(soup.select('p')[0])

# print(soup.a)

# print(soup.find_all(name='a'))

# print(soup.find(id="loginEmail"))

# print(soup.find(id="loginPassword"))

print(soup.find_all(class_="a-unordered-list a-vertical a-spacing-mini"))
# print(soup.find("h1", class_="card-title"))

# print(soup.select_one(selector='#navbarNav'))

# print(soup.select('img')[2])
# print(soup.select('img')[3])

# s = soup.select('img')[3]
# print(s['alt'])

# s = soup.select('img')[3]
# print(s['src'])

# print(soup.select_one('li a'))
# print(soup.select_one('li a').attrs['href'])
"C:\\Users\\sudarshan\\OneDrive\\Documents\\Personal Vault.lnk.xlsx"
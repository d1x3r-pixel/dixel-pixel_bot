from urllib import request, error
from bs4 import BeautifulSoup as b
import random
fact = []
with request.urlopen('https://lightwood.store/blog') as resp:
    data = resp.read()
    soup = b(data, 'html.parser')
    items = soup.find_all('div', attrs={'class': 't404__descr t-descr t-descr_xs'})
    for item in items:
        text = item.get_text()
        fact.append(text)

facts =  fact

kurs= []
with request.urlopen('https://www.cbk.kg/') as res:
    dat = res.read()
    sou = b(dat, 'html.parser')
    item = sou.find_all('div', attrs={'class': 'home-tab active'})
    for item in item:
        tex = item.get_text()
        kurs.append(tex)

facta = kurs 


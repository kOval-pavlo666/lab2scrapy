from bs4 import BeautifulSoup
import requests 

URL = "https://lnu.edu.ua/about/faculties/"

req = requests.get(URL)

s = BeautifulSoup(req.text, 'lxml')

faculties = s.find('ul', class_='structural-units')

print(faculties.text)

faculties_text = faculties.text.strip()

with open('lnu.txt', 'w', encoding='utf-8') as f:
    f.write(faculties_text)
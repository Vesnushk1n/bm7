import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('Solarize_Light2')

page = requests.get('https://mainfin.ru/currency/cb-rf/usd/date/2022')
soup = BeautifulSoup(page.text, 'html.parser')

dollar = soup.find_all('span', {'class': 'float-convert__btn'})

x = ([dol.text for dol in dollar])
x2 = list(map(float, x))
print(x2)
plt.plot(x2)
plt.show()

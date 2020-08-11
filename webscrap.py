import pandas as pd
import urllib.request as url
from bs4 import BeautifulSoup 
  
link = "https://www.flipkart.com/search?q=samsung&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page = url.urlopen(link)
#type(page)
soup = BeautifulSoup(page,'html')
price = soup.find_all('div',class_='_1vC4OE _2rQ-NK')
name = soup.find_all('div',class_='_3wU53n')
features = soup.find_all('ul',class_='vFw0gD')
mob_name = []
mob_price = []
mob_features = []
for i in name:
    mob_name.append(i.getText())
for i in price:
    mob_price.append(i.getText())
for i in features:
    mob_features.append(i.getText())
#     print({"Features":mob_features})
df = pd.DataFrame({"Mobile Name":mob_name,"Price":mob_price,"Feature":mob_features})
print(df)

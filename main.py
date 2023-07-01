import requests
from bs4 import BeautifulSoup
import json
numbers='0123456789'
a=[]
for i in range(1,11):
   url = f"https://www.parsemachine.com/sandbox/catalog/?page={i}"
   headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
   req = requests.get(url,headers=headers)
   src = req.text

   soup = BeautifulSoup(src,'lxml')
   all_products_hrefs = soup.find_all(class_='card product-card')
   for item in all_products_hrefs:
       item_href='https://www.parsemachine.com'+item.find('a').get('href')
       a.append(item_href)
res=[]
zxc=0
for ss in a:
    url=ss
    req=requests.get(url,headers=headers)
    src=req.text
    soup=BeautifulSoup(src,'lxml')
    x=soup.find(id='product_name').text.split()
    name=' '.join(x)
    y=soup.find(id='product_amount').text
    amount=''.join([ch for ch in y if ch in numbers])

    char=soup.find(class_='table-responsive').find('tbody').find_all('tr')
    res.append(
        {
            'Название': name,
            'Цена': amount
        }
    )
    for item in char:
        product=item.find_all('td')
        header=product[0].text
        value=product[1].text
        res.append(f'{header}:{value} ' )
    zxc+=1
    print(zxc)
with open('result.json','a',encoding = 'utf-8') as file:
    json.dump(res,file,indent=4,ensure_ascii=False)


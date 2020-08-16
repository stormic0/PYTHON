"""
 بعضی از آیتما اقساطی بود که چون توصورت سوال هم اشاره نشده بود بعید میدونم انتظار بره بریم ماه ها و قسط هاشو حساب کنیم و قیمت کل دراریم.
 لذا در این موارد برای قیمت همان پیش پرداخت در نظر گرفته شده.
 علاوه بر آن چون دریافت ورودی اسم ماشین در صورت سوال ذکر شده بود
 من هم آن را به شکل تابع input آورده ام اما اینکه این ورودی از چه ساختاری پیروی میکند از حیطه من خارج بوده و به عهده ی مصحح است.
 زیرا بسته به ساختار دسته بندی ماشین ها ممکن است این الگو متفاوت باشد.
 ینی در برخی موارد برای جست و جو یک ماشین خاص باید نام شرکت سازنده و نوع ماشین بیان شود مثلا hyundai/elantra
 اما در موردی مانند سمند همان عبارت samand کافی است.
"""


from bs4 import BeautifulSoup
import requests
import mysql.connector


path = 'https://bama.ir/car/' + input('please insert your car: ')     # edit input  (exp: input = 'hyundai/elantra')
r = requests.get(path)
soup = BeautifulSoup(r.text, 'html.parser')
raw_karkard = soup.find_all('p', attrs={'class':'price hidden-xs'})[:20]
list_raw_karkard = []
for karkard in raw_karkard:
    temp = (str(karkard).split('>')[1].split('<')[0]).strip()
    list_raw_karkard.append(temp)
raw_price = soup.find_all('p', attrs={'class':'cost'})[:20]
list_raw_price = []
for instance in raw_price:
    if instance.find('span', attrs={'itemprop':'price'}) is not None:
        temp = (str(instance.find('span', attrs={'itemprop':'price'})).split('>')[1].split('<')[0]).strip()
        list_raw_price.append(temp)
    else:
        temp = (str(instance).split('>')[3].split('<')[0]).strip()
        list_raw_price.append(temp)
OU = []
for gheimat in list_raw_price:
    for karkard in list_raw_karkard:
        OU.append((gheimat, karkard))
        list_raw_karkard.remove(karkard)
        break
cnx = mysql.connector.connect(user='root',
                              password='', host='127.0.0.1', database='proj')      # edit database
cursor = cnx.cursor()
for instance in OU:
    cursor.execute("INSERT INTO info VALUES (\'%s\', \'%s\')" % (instance[0], instance[1]))  # edit table
cnx.commit()
cnx.close()
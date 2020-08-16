"""
برنامه از سایت bama اطلاعات نام شهر سال کارکرد و قیمت را برای خودرو سوناتا 4 سیلندر استخراج کرده و در دیتا بیس ذخیره می کند.
درصورتی که هر کدام از 4 پارامتر ذکر شده وجود نداشت آن ردیف از اطلاعات ثبت نمی شود.
"""

from bs4 import BeautifulSoup
import requests
import mysql.connector


OU = []
for i in range(1,6):
    path = 'https://bama.ir/car/hyundai/sonata/4cyl-automatic?hasprice=true&page=' + str(i)
    r = requests.get(path)
    soup = BeautifulSoup(r.text, 'html.parser')
    raw_names = soup.find_all('h2', attrs={'itemprop':'name', 'class':'persianOrder'})
    list_names = []
    for name in raw_names:
        temp = str(name.find('span')).split('>')[1].split('<')[0]
        list_names.append(temp)
    raw_sal = soup.find_all('span', attrs={'class':'price year-label hidden-xs', 'itemprop':'releaseDate'})
    list_sal = []
    for sal in raw_sal:
        temp = str(sal).split('>')[1][:4]
        list_sal.append(temp)
    raw_karkard = soup.find_all('p', attrs={'class':'price hidden-xs'})
    list_karkard = []
    for karkard in raw_karkard:
        temp = str(karkard).split('>')[1].split('<')[0].strip()[7:]
        if temp != '':
            temp = int(temp.replace(',', ''))
        else:
            continue
        list_karkard.append(temp)
    raw_prices = soup.find_all('p', attrs={'class': 'cost'})
    list_prices = []
    for instance in raw_prices:
        temp = (str(instance.find('span', attrs={'itemprop': 'price'})).split('>')[1].split('<')[0]).strip().replace(',', '')
        list_prices.append(temp)
    raw_shahrs = soup.find_all('p', attrs={'class':'provice hidden-xs'})
    list_shahrs = []
    for shahr in raw_shahrs:
        temp = str(shahr.find('span')).split('>')[1].split('<')[0].split('،')[0]
        list_shahrs.append(temp)
    for instance in list_names:
        for a in list_sal:
            for b in list_karkard:
                for c in list_prices:
                    for d in list_shahrs:
                        OU.append((instance, d, int(a), b, int(c)))
                        list_shahrs.remove(d)
                        break
                    list_prices.remove(c)
                    break
                list_karkard.remove(b)
                break
            list_sal.remove(a)
            break
cnx = mysql.connector.connect(user='root',
                              password='', host='127.0.0.1', database='proj')   # edit database
cursor = cnx.cursor()
for instance in OU:
    cursor.execute("INSERT INTO info VALUES (\'%s\', \'%s\', %i, %i, %i)" % (instance[0], instance[1], instance[2], instance[3], instance[4]))  # edit table
cnx.commit()
cnx.close()
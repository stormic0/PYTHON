"""
         دراین برنامه کارکرد و سال ماشین برای ماشین سوناتا که در فاز یک دیتا های آن در دیتابیس ذخیره شد به عنوان ورودی داده میشود
         و توسط ماشینی که تحت تعلیم دیتا بیس قرار گرفته است قیمت آن تخمین زده شده و نمایش داده می شود.
"""

from sklearn import tree
import mysql.connector


x = []
y = []
cnx = mysql.connector.connect(user='root',
                              password='', host='127.0.0.1', database='proj')   # edit database
cursor = cnx.cursor()
query = "SELECT*FROM info"
cursor.execute(query)
for (name, shahr, sal, karkard, gheimat) in cursor:
    x.append((sal, karkard))
    y.append(gheimat)
cnx.close()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
while True:
    test = []
    test.append([int(input('SAL: ')), int(input('KARKARD: '))])
    answer = clf.predict(test)
    print('estimate price is: ', int(answer))
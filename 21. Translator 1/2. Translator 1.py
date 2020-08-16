#          مترجم آنلاين
from collections import OrderedDict
da = OrderedDict()
n = int(input())
la, lb = [], []
for i in range(n):
    la.append(input().split())
for i in range(len(la)):
    da[la[i][0]] = la[i][1]
jomle = input()
jomle = jomle.split()
for i in range(len(jomle)):
    for j in dict(da):
        if jomle[i] == j:
            lb.append((da[j]+' '))
            break
    else:
        lb.append((jomle[i]+' '))
khoruji = ''
for i in range(len(lb)):
    khoruji += lb[i]
khoruji = khoruji.strip()
print(khoruji)

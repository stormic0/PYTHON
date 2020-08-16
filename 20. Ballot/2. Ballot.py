#           سيستم شمارش آرا
from collections import OrderedDict
da = OrderedDict()
n = int(input())
la = []
for i in range(n):
    la.append(input())
la.sort()
for i in range(n):
    da[la[i]] = la.count(la[i])
keys = da.keys()
for i in list(keys):
    print(i, da[i])


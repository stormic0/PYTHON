#           ملاقات نوروزي
x1, x2, x3 = map(float, input().split(' '))
a = [x1, x2, x3]
a.sort()
vasat = a[1]
fasele_1 = abs(a[1]-a[0])
fasele_2 = abs(a[1]-a[2])
khoruji = fasele_1 + fasele_2
if int(khoruji) == khoruji:
    print(int(khoruji))
else:
    print(khoruji)

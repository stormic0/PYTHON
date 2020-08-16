#           مسابقات جهاني کبدي
n = int(input())
a = str(input()).split(' ')
b = []
for i in range(len(a)):
    if int(a[i]) < 3:
        b.append(a[i])
print(len(b)//3)

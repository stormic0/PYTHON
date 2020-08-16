#           قيمت لپتاپ ها
n = int(input())
a = []
for i in range(n):
    gheimat, keifiat = map(int, input().split(' '))
    a.append((gheimat, keifiat))
def GK(a):
    for i in (range(len(a))):
        for j in range(len(a)):
            if j != i:
                if a[i][0] < a[j][0]:
                    if a[i][1] > a[j][1]:
                        return True
                elif a[i][0] > a[j][0]:
                    if a[i][1] < a[j][1]:
                        return True
    else:
        return False
if GK(a):
    print('happy irsa')
else:
    print('poor irsa')

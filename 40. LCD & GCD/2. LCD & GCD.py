n, m = map(int, input().split(' '))
def Bmm(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    while (b != 0):
        rem = a % b
        a = b
        b = rem
    r = a
    return r
if 1 <= n and m <= 10**9:
    BMM = Bmm(n, m)
    KMM = int(n * m/ Bmm(n, m))
    print(BMM, KMM)

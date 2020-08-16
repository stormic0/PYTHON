def Bmm(a, b):
    if a < b:
        a,b = b,a
    while (b != 0):
        rem = a % b
        a = b
        b = rem
    r = a
    return r

def triples(IN):
    for n in range(1, IN):
        for m in range(n+1, 250):
            if n % 2 == 0 and m % 2 == 0: continue
            if n % 2 != 0 and m % 2 != 0: continue
            if Bmm(m,n) != 1: continue
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if a + b + c == IN:
                p = [a, b, c]
                p.sort()
                return p

n = int(input())
if 1 <= n <= 90000:
    if n >= 12:
        if triples(n) is None:
            det = 0
            for i in range(2, n):
                if n / i < 11: break
                if n / i == int(n / i):
                    if triples(int(n / i)) is not None:
                        det = 1
                        a, b, c = triples(int(n / i))
                        print(a * i, b * i, c * i)
                        break
            if det == 0: print('Impossible')
        else:
            a, b, c = triples(n)
            print(a, b, c)
    else: print('Impossible')

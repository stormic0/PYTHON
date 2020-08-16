def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
def prime_division(n):
    dl = []
    for i in range(2,n+1):
        if n % i == 0:
            if is_prime(i):
                dl.append(i)
    return len(dl)
a = []
for i in range(10):
    In = int(input())
    count = prime_division(In)
    a.append((In, count))
a.sort(key= lambda x: x[1], reverse=True)
b= []
for i in a:
    if i[1] == a[0][1]:
        b.append(i)
b.sort(key=lambda x: x[0], reverse=True)
print(b[0][0], b[0][1])
def maghsum(n):
    c = 0
    for i in range(1, n+1):
         if n % i == 0:
             c += 1
    return c

N = 2
NN = 0

for i in range(20):
    n = int(input())
    count = maghsum(n)
    if count > N:
        N = count
        NN = n
    elif count == N:
        if n > NN:
            NN = n
print(NN, N)

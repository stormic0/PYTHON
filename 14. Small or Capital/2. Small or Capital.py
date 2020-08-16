#           حروف کوچیک حروف بزرگ
a = input()
alpha,Alpha,n,N='abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ',0,0
for i in a:
    for j in alpha:
        if i == j:
            n += 1
for i in a:
    for j in Alpha:
        if i == j:
            N += 1
if N > n:
    print(a.upper())
else:
    print(a.lower())

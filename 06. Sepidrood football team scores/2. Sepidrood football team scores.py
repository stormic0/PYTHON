n, X = 0, 0
for i in range(30):
    x = int(input())
    if x == 0:
        X += 0
    elif x == 1:
        X += x
    elif x == 3:
        X += x
        n += 1
print(X, n)

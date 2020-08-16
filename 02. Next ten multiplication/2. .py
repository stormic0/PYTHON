x, n = int(input()), 1
while True:
    r = x % (10**n)
    if r < 10:
        x += 10 - r
        print(x)
        break
    else:
        n += 1

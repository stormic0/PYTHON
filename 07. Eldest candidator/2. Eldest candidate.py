a, x = 0, 10
while a != -1:
    a = int(input())
    if 10 <= a <= 90:
        if a > x:
            x = a
print(x)

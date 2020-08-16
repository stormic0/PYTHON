a = 0
b = []
while a != -1:
    a = int(input())
    if 10 <= a <= 90:
        b.append(a)
b.sort(reverse=True)
print(b[0], b[1])
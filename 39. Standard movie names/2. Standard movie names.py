n = int(input())
a = []
if 1 <= n <= 10:
    for i in range(n):
        a += [input().split(' ')]
    for i in range(len(a)):
        print()
        for j in range(len(a[i])):
            print((''.join(a[i][j])).capitalize() ,'' , end="")

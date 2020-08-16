geners = ['Horror', 'Romance', 'Comedy', 'History' , 'Adventure' , 'Action']
geners_value = {}
for i in geners:
    geners_value[i] = 0
n = int(input())
for i in range(n):
    name, g1, g2, g3 = map(str, input().split(' '))
    for j in geners:
        if g1 == j:
            geners_value[j] += 1
        if g2 == j:
            geners_value[j] += 1
        if g3 == j:
            geners_value[j] += 1
OU = []
for i in geners_value:
    OU.append((i,geners_value[i]))
OU.sort(key=lambda x:x[1], reverse=True)
x = 0
while x <= 6:
    for i in range(5):
        if OU[i][1] == OU[i+1][1]:
            if OU[i][0] > OU[i+1][0]:
                OU[i], OU[i+1] = OU[i+1], OU[i]
    x += 1
for i in OU:
    print(i[0],':',i[1])
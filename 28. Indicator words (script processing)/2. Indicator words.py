C_L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = input().split('.')
a = a[:len(a)-1]
b= []
for i in a:
    temp = i.strip().split(' ')
    b.append(temp)
for i in b:
    if i[0] == '':
        i.remove(i[0])
    i[0] = 'ss'
c = []
for i in b:
    for j in i:
        c.append(j)
OU = []
for i in range(len(c)):
    if c[i][0] in C_L:
        if c[i][-1] == ',':
            c[i] = c[i][:len(c[i])-1]
        OU.append((i+1, c[i]))

if OU == []:
    print('None')
else:
    for i in OU:
        print('%i:%s' % (i[0], i[1]))
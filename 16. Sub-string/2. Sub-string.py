#           زير رشته
a = input()
a, b = a.upper(), []
for i in a:
    b.append(i)
def ABD(b):
    ans1 = 0
    for i in range(len(b)-1):
        if b[i] == 'A' and b[i+1] == 'B':
            ans1 = 1
            b[i:i+2] = 'yechizi'
    return(ans1, b)
def BAD(b):
    ans2 = 0
    for i in range(len(b)-1):
        if b[i] == 'B' and b[i+1] == 'A':
            ans2 = 1
            break
    return ans2
ans1, b = ABD(b)
ans2 = BAD(b)
if ans1 + ans2 == 2:
    print('YES')
else:
    print('NO')

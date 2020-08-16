import datetime


try:
    d = input().split('/')
    a = datetime.datetime(int(d[0]), int(d[1]), int(d[2]))
    a = str(a).split(' ')[0].split('-')
    b = str(datetime.date.today()).split('-')
    for i in [a, b]:
        for j in range(len(i)):
            i[j] = int(i[j])
    sen = b[0] - a[0]
    if a[1] > b[1]:
        sen -= 1
    elif a[1] == b[1]:
        if a[2] > b[2]:
            sen -= 1
            
    print(sen)
except Exception:
    print('WRONG')

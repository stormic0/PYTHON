OU_raw = []
n = int(input())
for i in range(n):
    sex, name, lang = map(str, input().split('.'))
    OU_raw.append((sex, name.capitalize(), lang))
OU_raw.sort(key=lambda x: x[0], reverse=True)
m_s = []
f_s = []
for i in OU_raw:
    if i[0] == 'm':
        m_s.append(i)
    else:
        f_s.append(i)
m_s.sort(key=lambda x: str(x[1]))
f_s.sort(key=lambda x: str(x[1]))
OU = []
for i in f_s:
    OU.append(i)
for i in m_s:
    OU.append(i)
for i in OU:
    print(i[0], i[1], i[2])
n, en_fr_gr = int(input()), {}
for i in range(n):
    temp = input().split()
    en_fr_gr[temp[1]] = en_fr_gr[temp[2]] = en_fr_gr[temp[3]] = temp[0]
jomle, khoruji = input().split(' '), ''
for i in jomle:
    if i in en_fr_gr:
        khoruji += en_fr_gr[i] + ' '
    else:
        khoruji += i + ' '
khoruji = khoruji[:len(khoruji)-1]
print(khoruji)
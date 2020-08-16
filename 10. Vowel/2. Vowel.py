#           کار با رشته ها
In = input()
def DIV(n):
    In = []
    for i in n:
        In.append(i)
    return In
def RMV(In):
    Div = DIV(In)
    for i in list(Div):
        for j in 'aeiouAEIOU':
            if i == j:
                Div.remove(i)
    return Div
def FPR(Ou):
    a = str()
    for i in range(len(list(Ou))):
        a += '.' + Ou[i]
    return a
Ou = RMV(In)
Ou = FPR(Ou)
Ou = Ou.lower()
print(Ou)

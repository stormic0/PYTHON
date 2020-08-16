def SRT(In):
    Ou = ''
    for i in range(len(In)):
        Ou = Ou + ('+' + In[i])
    return Ou[1:]
In = input()
In = In.split('+')
In.sort()
print(SRT(In))
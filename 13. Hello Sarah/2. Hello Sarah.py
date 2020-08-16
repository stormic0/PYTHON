a = input()
b = a
def HF(a):
        for a1 in range(len(a)):
            a = b
            if a[a1] == 'h':
                a = a[a1+1:]
                for a2 in range(len(a)):
                    if a[a2] == 'e':
                        a = a[a2+1:]
                        for a3 in range(len(a)):
                            if a[a3] == 'l':
                                a = a[a3+1:]
                                for a4 in range(len(a)):
                                    if a[a4] == 'l':
                                        a = a[a4+1:]
                                        for a5 in range(a4, len(a)):
                                            if a[a5] == 'o':
                                                return('YES')
                                        else:
                                            return('NO')
                                else:
                                    return('NO')
                        else:
                            return('NO')
                else:
                    return('NO')
        
        else:
            return('NO')
                                
print(HF(a))

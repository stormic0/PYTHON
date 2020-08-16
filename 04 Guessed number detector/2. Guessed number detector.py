import random
a, b, ans = 1, 99, None
while ans != 'd':
    test = random.randint(a, b)
    print(test)
    ans = input()
    if ans == 'k':
        b = test
    elif ans == 'b':
        a = test

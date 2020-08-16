num, out = input(), ''
for i in range(len(num), 0, -1):
    out += num[i-1]
print(int(out)*2)
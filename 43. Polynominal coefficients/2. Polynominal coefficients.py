def Multi(A, B, len_A, len_B):
    prod = [0] * (len_A + len_B - 1)
    for i in range(len_A):
        for j in range(len_B):
            prod[i + j] += A[i] * B[j]
    return prod
def MultiPlus(A, B, len_A, len_B, n):
    for i in range(n-1):
        B = Multi(A, B, len_A, len_B)
        len_B = len(B)
    return B
m, n = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
B = A
len_A, len_B = len(A), len(B)
OUT = MultiPlus(A, B, len_A, len_B, n)
len_OUT = len(OUT)
for i in range(len_OUT):
    print(OUT[i], '',end='')



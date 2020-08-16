#           Palindrome
A = input()
A = A.lower()
a = []
def reverselist(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A
for i in A:
    a.append(i)
B = a.copy()
b = reverselist(B, 0, len(A)-1)
if a == B:
    print('palindrome')
else:
    print('not palindrome')





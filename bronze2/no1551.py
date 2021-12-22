from win32con import EXCEPTION_ARRAY_BOUNDS_EXCEEDED


def subtract(a, b):
    x = a - b
    return x


n, c = map(int, input().split())
A = list(map(int, input().split(",")))
for i in range(len(A)):
    if len(A) < A[i+1]:
        break
    A[i+1] - A[i]
# print(subtract(3, -5))
# print(subtract(A[0], A[1]))

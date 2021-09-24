# A = 5분 5*60
# B = 1분 1*60
# C = 10초 10
import sys

T = int(sys.stdin.readline())
A, B, C = 300, 60, 10
if T % C == 0:
    result = [0, 0, 0]
    while T > 0:
        if T >= A:
            T -= A
            result[0] += 1
        elif T >= B:
            T -= B
            result[1] += 1
        elif T >= C:
            T -= C
            result[2] += 1
else:
    result = [-1]
print(" ".join(map(str, result)))

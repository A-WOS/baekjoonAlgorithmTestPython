# print(ord('가'))
# print(ord('힣'))

N = int(input())
cnt = 1
for i in range(44032, 55204):
    if cnt == N:
        print(chr(i))
    cnt += 1

N, S = input().split()
N = int(N)
dict_a = {}
for i in range(N):
    name, chat = input().split()
    dict_a[name] = chat
cnt = 0
answer = dict_a[S]
for val in dict_a:
    if val == S:
        break
    elif dict_a[val] == answer:
        cnt += 1
print(cnt)

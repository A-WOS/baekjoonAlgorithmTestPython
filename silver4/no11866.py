N, K = map(int, input().split())

queue = []
result = []
for i in range(1, N + 1):
    queue.append(i)

i = 0
while queue:
    i = (i + (K - 1)) % len(queue)
    result.append(queue.pop(i))

# https://hyesun03.github.io/2017/04/08/python_int_join/
print("<" + ", ".join(map(str, result)) + ">")
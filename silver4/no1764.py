N, M = map(int, input().split())
not_listen, not_watch = set(), set()
for i in range(N):
    not_listen.add(input())
for i in range(M):
    not_watch.add(input())
rs = sorted(not_listen & not_watch)
print(len(rs))
for val in rs:
    print(val)
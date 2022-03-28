N = int(input())
interest = list(map(int, input().split()))
no_My_view = list(map(int, input().split()))
rs = 0
print(sum(interest))
for i, val in enumerate(no_My_view):
    if val == 0:
        rs += interest[i]
print(rs)
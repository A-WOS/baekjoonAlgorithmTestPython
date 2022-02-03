# # solved #1
# n = int(input())
# l1 = list(reversed(sorted(map(int, input().split()))))
# l2 = sorted(list(map(int, input().split())))
# tot = 0
# for i in range(n):
#     tot += l1[i] * l2[i]
# print(tot)

# solved #2
n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
tot = 0
for i in range(n):
    tot += l1.pop(l1.index(min(l1))) * l2.pop(l2.index(max(l2)))
print(tot)
l = list(map(int, input().split()))
l2 = [val for val in l]
l3 = l2.pop(l2.index(max(l2)))
if l[0] == l[1] == l[2]:
    print(2)
elif l3**2 == sum(x**2 for x in l2):
    print(1)
else:
    print(0)
# print(l, l2, l3)
# print(l, l2, l3)
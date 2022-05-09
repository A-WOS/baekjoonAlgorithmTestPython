import sys

T = int(input())
members = []
for _ in range(T):
    age, name = sys.stdin.readline().split()
    age = int(age)
    members.append([age, name])

members.sort(key = lambda x : x[0])

for member in members:
    print(member[0], member[1])

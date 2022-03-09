import sys

N, M = map(int, input().split())
address_dict = dict()
for _ in range(N):
    address, password = sys.stdin.readline().split()
    address_dict[address] = password

for _ in range(M):
    find_password = sys.stdin.readline().rstrip()
    print(address_dict[find_password])

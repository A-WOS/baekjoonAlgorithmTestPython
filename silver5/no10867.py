num_count = int(input())
rs = ''
for val in sorted(set(map(int, input().split()))):
    rs += f'{str(val)} '
print(rs.strip())
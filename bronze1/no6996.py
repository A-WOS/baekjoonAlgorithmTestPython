N = int(input())
for _ in range(N):
    A, B = input().split()
    rs1 = ''.join(sorted(A))
    rs2 = ''.join(sorted(B))
    if rs1 == rs2: print(f'{A} & {B} are anagrams.')
    else: print(f'{A} & {B} are NOT anagrams.')

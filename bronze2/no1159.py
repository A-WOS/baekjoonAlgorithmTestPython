
# N : 입력 받을 개수, l : 입력받은 문자열을 저장할 배열, distinct_l : l에서 중복되지 않은 첫글자 뽑아내어 저장
# r : distinct_l 에서 뽑은 문자의 개수를 l배열에서 세어서 5개 이상이면 문자를 이어붙여 결과를 반환
N = int(input())
l = []
distinct_l = []
r = ''
for i in range(N):
    s = input()
    l.append(s[0])

for x in l:
    if x not in distinct_l:
        distinct_l.append(x)
for val in distinct_l:
    if l.count(val) >= 5:
        r += val
if r:
    print(''.join(sorted(r)))
else:
    print("PREDAJA")


import sys
from itertools import permutations

while True:
    try:
        word, num = sys.stdin.readline().split()
        words, num = list(word), int(num)
        cnt = 1
        flag = False

        for per in permutations(words):

            if cnt == num:
                print(f'{word} {num} =', ''.join(list(per)))
                flag = True
                break
            cnt += 1

        if flag is False:
            print(f'{word} {num} = No permutation')
    except ValueError:
        break

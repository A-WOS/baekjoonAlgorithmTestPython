import sys
from itertools import permutations

# 테스트 케이스 개수
test_case = int(input())
for _ in range(test_case):
    # 단어의 수 k
    word_num = int(input())
    # k개의 단어를 담는 배열 words
    words = []
    # 만들어진 팰린드롬수 중 중복된 값이 있으면 제거를 위해 set() 사용
    word_set = set()
    rs_list = []
    for _ in range(word_num):
        words.append(sys.stdin.readline().rstrip())
    # 순열을 뽑기 위해 이용하는 permutations 자기 자신을 제외한 순열이 만들어짐
    # 5개중 2개, 5x4 = 20가지의 순열이 만들어짐
    for val in permutations(words, 2):
        rs = ''.join(val)
        # 혹시 모를 중복값에 대비해 set()으로 걸러줌
        if rs[:] == rs[::-1]: word_set.add(rs)
    # 틀렸던거 print(''.join(word_set)) if word_set else print(0)
    # 출력시 여러가지 팰린드롬수가 있다면 그 중 아무거나 출력하고 팰린드롬수가 없다면 0을 출력
    print(word_set.pop()) if word_set else print(0)


# 틀렸던거 풀이
# import sys
# from itertools import permutations
#
# test_case = int(input())
# for _ in range(test_case):
#     word_num = int(input())
#     words = []
#     word_set = set()
#     # test = []
#     # test_set = set()
#     for _ in range(word_num):
#         words.append(sys.stdin.readline().rstrip())
#     for val in permutations(words, 2):
#         rs = ''.join(val)
#         # test.append(rs)
#         # test_set.add(rs)
#         if rs[:] == rs[::-1]: word_set.add(rs)
#     # print(len(test))
#     # print(len(test_set))
#     # print(' '.join(test))
#     # print(''.join(word_set)) if word_set else print(0)

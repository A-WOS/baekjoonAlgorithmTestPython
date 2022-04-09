from collections import Counter

words = []
for _ in range(int(input())):
    word = input()
    words.append(word)

# counter 로 해당 단어가 몇번 들어갔는지 확인
counter = Counter(words)
# 입력 받은 단어중 제일 많이 입력받은 횟수 뽑아냄
max_count = max(counter.values())
# 빈도가 높은 단어들이 여러개일 경우를 생각해서 정렬함
sorted_words = sorted(counter.items(), key=lambda x: x[1], reverse=True)

rs = []
for val in sorted_words:
    k, v = val
    if v == max_count:
        rs.append([k, v])

k, v = sorted(rs)[-1]
print(k, v)

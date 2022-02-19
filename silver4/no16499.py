n = int(input())
word_list = list()
for _ in range(n):
    s = ''.join(sorted(input()))
    if s not in word_list:
        word_list.append(s)
print(len(word_list))

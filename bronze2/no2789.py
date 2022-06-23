s = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = list(input())
for c in s:
    for j in range(len(word)):
        if c == word[j]:
            word[j] = ''
print(''.join(word))


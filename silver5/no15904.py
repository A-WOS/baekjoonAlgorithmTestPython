import sys

context = sys.stdin.readline().rstrip()
chars = ['U', 'C', 'P', 'C']
rs = 'I love UCPC'
for char in chars:
    if char in context:
        char_idx = context.index(char)
        context = context[char_idx+1:]
    else:
        rs = 'I hate UCPC'
        break
print(rs)

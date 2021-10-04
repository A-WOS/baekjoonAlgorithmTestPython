import sys

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    count = 0
    s = sys.stdin.readline().strip()
    if s == "#":
        break
    else:
        for val in vowel:
            count += s.count(val)
        print(count)

def func(word):
    l = list()
    for i in range(len(word)):
        l.append(word[i:])
    l.sort()
    return l


s = input()
for val in func(s): print(val)
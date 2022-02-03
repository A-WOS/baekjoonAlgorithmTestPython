s = input()
tot = 0
for i in range(len(s)):
    if i == 0:
        tot += 10
    else:
        if (s[i-1] == ')' and s[i] == ')') or (s[i-1] == '(' and s[i] == '('):
            tot += 5
        else:
            tot += 10
print(tot)
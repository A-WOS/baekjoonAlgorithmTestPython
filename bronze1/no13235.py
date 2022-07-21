s = input()
left, right = 0, len(s) - 1
rs = 'true'

while left < right:
    if s[left] != s[right]:
        rs = 'false'
        break
    left += 1
    right -= 1
print(rs)

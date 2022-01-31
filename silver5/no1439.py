def func(s):
    count =0
    for val in s:
        if val:
            count += 1
    return count


s1 = input()
s2 = s1.split('0')
s3 = s1.split('1')
print(min(func(s2), func(s3)))
# func(s2)


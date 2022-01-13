n, a, b, c, d = map(int, input().split())
l = []
l.append((n//a + 1)*b) if n % a else l.append((n//a)*b)
l.append((n//c + 1)*d) if n % c else l.append((n//c)*d)
print(min(l))
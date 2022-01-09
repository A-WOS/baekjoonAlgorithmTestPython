def calc_ts(k):
    hour = k // 3600
    k -= 3600 * hour
    minute = k // 60
    k -= 60 * minute
    second = k % 60
    return hour, minute, second


def take_time(h, m, s, h1, m1, s1):
    if (s+s1) // 60:
        m1 += (s+s1) // 60
    ts = (s+s1) % 60
    if (m+m1) // 60:
        h1 += (m+m1) // 60
    tm = (m + m1) % 60
    th = (h+h1) % 24
    return th, tm, ts


h, m, s = map(int, input().split())
ts = int(input())
h1, m1, s1 = calc_ts(ts)
rh, rm, rs = take_time(h, m, s, h1, m1, s1)
print(rh, rm, rs)
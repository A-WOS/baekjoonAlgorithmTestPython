while True:
    a = float(input())
    if a == 0:
        break
    print(f'{1 + a + pow(a,2) + pow(a,3) + pow(a,4):.2f}')
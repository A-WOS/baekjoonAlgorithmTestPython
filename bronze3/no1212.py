# 8진수를 10진수로 변경
octa_n = int(input(), 8)
print(octa_n)
# 10진수를 2진수로 변환 0b라는 string이 붙기때문에 슬라이싱을 통해 잘라줌
print(bin(octa_n))
print(bin(octa_n)[2:])

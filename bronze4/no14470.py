# 고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.
# 고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다.
# 고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.

# 원래의 고기 온도 : A
# 목표 온도 : B
# 얼어 있는 고기를 1도 데우는데 걸리는 시간 : C
# 얼어 있는 고기를 해동하는데 걸리는 시간 : D
# 얼어 있지 않은 고기를 1도 데우는데 걸리는 시간 : E

# -10 20 5 10 3
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

result = 0
if A < 0:
    result = abs(A) * C + D + B*E
else:
    result = (B-A) * E
print(result)


def cost(n):
    return 100 if 1 <= n <= 20 else 270 if 21 <= n <= 30 else 500


a, b = int(input()), int(input())
print(
    "Congratulations, you are within the speed limit!" if b - a <= 0 else f"You are speeding and your fine is ${cost(b - a)}.")

# 숏코딩
# a, b = int(input()), int(input())
# n = b - a
# print("Congratulations, you are within the speed limit!" if n <= 0 else f"You are speeding and your fine is ${100 if 1 <= n <= 20 else 270 if 21 <= n <= 30 else 500}.")

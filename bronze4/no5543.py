burger, drink = [], []
for i in range(5):
    if i < 3:
        burger.append(int(input()))
    else:
        drink.append(int(input()))

print(min(burger) + min(drink) - 50)
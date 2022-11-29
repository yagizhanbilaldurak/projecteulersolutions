sum = 0
for i in range(1, 101):
    sum = sum + i

sum = sum ** 2
sum2 = 0
for i in range(1, 101):
    i = i * i
    sum2 = sum2 + i

print(sum - sum2)
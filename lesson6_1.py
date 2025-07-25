N = int(input("Введите число N: "))
count_zero = 0

for _ in range(N):
    num = int(input())
    if num == 0:
        count_zero += 1

print(count_zero)
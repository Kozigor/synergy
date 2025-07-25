# Ввод чисел A и B
A = int(input())
B = int(input())

# Проходим по всем числам от A до B включительно
for num in range(A, B + 1):
    # Проверяем, является ли число чётным
    if num % 2 == 0:
        print(num, end=' ')
# Считываем последовательность чисел из одной строки, разделённой пробелами
numbers = input().split()

# Множество для хранения уже встреченных чисел
seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
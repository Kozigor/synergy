def count_divisors(x):
    count = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            count += 1
            if i != x // i:
                count += 1
        i += 1
    return count

x = int(input("Введите натуральное число X: "))
print(count_divisors(x))
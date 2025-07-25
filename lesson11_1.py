
def factorial(n):
    # Функция для вычисления факториала числа n
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_list(n):
    # Сначала находим факториал числа n
    fact_n = factorial(n)

    # Создаем список факториалов от n до 1
    result = []
    for i in range(n, 0, -1):
        result.append(factorial(i))
    return result


# Пример использования
n = 3
print(f"Факториал числа {n}: {factorial(n)}")
print(f"Список факториалов от {n} до 1:", factorial_list(n))

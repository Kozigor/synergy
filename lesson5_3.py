def investment_decision(X, A, B):
    if A >= X and B >= X:
        return 2  # оба могут вложиться по отдельности
    elif A + B >= X:
        return 1  # вместе хватает, по отдельности нет
    else:
        return 0  # никто не может вложиться

# Пример использования:
X = int(input("Введите минимальную сумму инвестиций X: "))
A = int(input("Введите сумму у Майкла A: "))
B = int(input("Введите сумму у Ивана B: "))

result = investment_decision(X, A, B)
print(result)
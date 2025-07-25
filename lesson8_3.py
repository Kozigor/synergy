def min_boats(m, n, weights):
    # Сортируем веса рыбаков по убыванию, чтобы сначала грузить тяжелых
    weights.sort(reverse=True)

    boats = 0
    i = 0
    j = n - 1

    while i <= j:
        if i == j:
            # Остался один рыбак
            boats += 1
            break
        # Если два самых тяжелых рыбака помещаются вместе по весу и по количеству (2 человека)
        if weights[i] + weights[j] <= m:
            i += 1
            j -= 1
        else:
            # Иначе тяжелый рыбак идет один
            i += 1
        boats += 1

    return boats


# Чтение входных данных
m = int(input())  # максимальная масса лодки
n = int(input())  # количество рыбаков
weights = [int(input()) for _ in range(n)]

print(min_boats(m, n, weights))
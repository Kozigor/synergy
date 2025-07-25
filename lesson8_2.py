def rearrange_array(arr):
    # Метод изменяет массив так, чтобы первый элемент стал последним,
    # второй — первым, третий — вторым и так далее
    if not arr:
        return arr
    return [arr[-1]] + arr[:-1]

# Чтение входных данных
N = int(input())
arr = list(map(int, input().split()))

# Преобразование массива
result = rearrange_array(arr)

# Вывод результата
print(*result)
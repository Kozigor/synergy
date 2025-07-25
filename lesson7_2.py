def replace_multiple_spaces(s):
    # Разделяем строку по пробелам (любое количество подряд идущих пробелов)
    # и затем соединяем обратно одним пробелом
    return ' '.join(s.split())

# Пример использования
input_str = input("Введите строку: ")
result = replace_multiple_spaces(input_str)
print(result)
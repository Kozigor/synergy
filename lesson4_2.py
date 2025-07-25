def calculate(number):
    # Преобразуем число в строку для удобного доступа к цифрам
    str_num = str(number)

    # Проверяем, что число пятизначное
    if len(str_num) != 5:
        raise ValueError("Число должно быть пятизначным")

    # Извлекаем цифры по позициям
    ten_thousands = int(str_num[0])  # количество десятков тысяч
    thousands = int(str_num[1])  # количество тысяч
    hundreds = int(str_num[2])  # количество сотен
    tens = int(str_num[3])  # количество десятков
    units = int(str_num[4])  # количество единиц

    # Возводим количество десятков в степень количества единиц
    power_result = tens ** units

    # Умножаем на количество сотен
    multiplied = power_result * hundreds

    # Вычисляем разность количества десятков тысяч и количества тысяч
    difference = ten_thousands - thousands

    # Делим полученное число на разность
    result = multiplied / difference

    return result


# Пример из задачи
number = 46275
result = calculate(number)
print(result)  # Выведет: -16807.0
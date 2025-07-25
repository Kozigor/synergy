number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
elif number % 2 != 0:
    print("число не является четным")
else:
    if number > 0:
        print("положительное четное число")
    else:
        print("отрицательное четное число")
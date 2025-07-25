pets = {}

# Запрашиваем у пользователя количество питомцев для ввода
num_pets = int(input("Введите количество питомцев для добавления: "))

for _ in range(num_pets):
    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца (целое число): "))
    owner = input("Введите имя владельца: ")

    pets[name] = {
        "Вид питомца": species,
        "Возраст питомца": age,
        "Имя владельца": owner
    }

# Функция для корректного вывода возраста с правильным склонением
def format_age(age):
    if 11 <= age % 100 <= 14:
        return f"{age} лет"
    elif age % 10 == 1:
        return f"{age} год"
    elif 2 <= age % 10 <= 4:
        return f"{age} года"
    else:
        return f"{age} лет"

# Вывод информации о питомцах
for pet_name, info in pets.items():
    age_str = format_age(info["Возраст питомца"])
    print(f"Это {info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {age_str}. Имя владельца: {info['Имя владельца']}")
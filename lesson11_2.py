import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    # Функция для правильного склонения слова "год"
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

def pets_list():
    if not pets:
        print("Список питомцев пуст.")
        return
    for ID, pet_dict in pets.items():
        for name, info in pet_dict.items():
            suffix = get_suffix(info["Возраст питомца"])
            print(f"ID: {ID} - {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {suffix}. Имя владельца: {info['Имя владельца']}")

def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1

    name = input("Введите кличку питомца: ").strip()
    kind = input("Введите вид питомца: ").strip()
    while True:
        try:
            age = int(input("Введите возраст питомца (целое число): ").strip())
            if age < 0:
                print("Возраст не может быть отрицательным. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Некорректный ввод возраста. Введите целое число.")
    owner = input("Введите имя владельца: ").strip()

    pets[new_id] = {
        name: {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец с ID {new_id} успешно добавлен.")

def read():
    try:
        ID = int(input("Введите ID питомца для просмотра: ").strip())
    except ValueError:
        print("Некорректный ID. Введите целое число.")
        return

    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден.")
        return

    # pet_info - словарь с одним ключом: имя питомца
    for name, info in pet_info.items():
        suffix = get_suffix(info["Возраст питомца"])
        print(f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {suffix}. Имя владельца: {info['Имя владельца']}")

def update():
    try:
        ID = int(input("Введите ID питомца для обновления: ").strip())
    except ValueError:
        print("Некорректный ID. Введите целое число.")
        return

    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден.")
        return

    # Получаем имя питомца (ключ словаря)
    name = list(pet_info.keys())[0]

    print(f"Обновляем информацию для питомца \"{name}\" (оставьте поле пустым, чтобы не менять).")

    new_name = input(f"Введите новую кличку (текущая: {name}): ").strip()
    if not new_name:
        new_name = name

    kind = pet_info[name]["Вид питомца"]
    new_kind = input(f"Введите новый вид питомца (текущий: {kind}): ").strip()
    if not new_kind:
        new_kind = kind

    age = pet_info[name]["Возраст питомца"]
    while True:
        new_age_str = input(f"Введите новый возраст питомца (текущий: {age}): ").strip()
        if not new_age_str:
            new_age = age
            break
        try:
            new_age = int(new_age_str)
            if new_age < 0:
                print("Возраст не может быть отрицательным. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Некорректный ввод возраста. Введите целое число или оставьте поле пустым.")

    owner = pet_info[name]["Имя владельца"]
    new_owner = input(f"Введите имя нового владельца (текущее: {owner}): ").strip()
    if not new_owner:
        new_owner = owner

    # Если имя питомца изменилось, нужно удалить старую запись и создать новую с новым именем
    if new_name != name:
        pets[ID] = {
            new_name: {
                "Вид питомца": new_kind,
                "Возраст питомца": new_age,
                "Имя владельца": new_owner
            }
        }
    else:
        pets[ID][name] = {
            "Вид питомца": new_kind,
            "Возраст питомца": new_age,
            "Имя владельца": new_owner
        }

    print(f"Информация о питомце с ID {ID} обновлена.")

def delete():
    try:
        ID = int(input("Введите ID питомца для удаления: ").strip())
    except ValueError:
        print("Некорректный ID. Введите целое число.")
        return

    if ID in pets:
        del pets[ID]
        print(f"Питомец с ID {ID} удалён из базы данных.")
    else:
        print(f"Питомец с ID {ID} не найден.")

def main():
    print("Ветеринарная база данных питомцев.")
    print("Доступные команды: create, read, update, delete, list, stop")
    while True:
        command = input("Введите команду: ").strip().lower()
        if command == "stop":
            print("Работа программы завершена.")
            break
        elif command == "create":
            create()
        elif command == "read":
            read()
        elif command == "update":
            update()
        elif command == "delete":
            delete()
        elif command == "list":
            pets_list()
        else:
            print("Неизвестная команда. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()

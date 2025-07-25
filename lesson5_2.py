# Ввод слова с маленькими латинскими буквами
word = input("Введите слово из маленьких латинских букв: ")

# Определяем гласные буквы
vowels = ['a', 'e', 'i', 'o', 'u']

# Считаем количество согласных и гласных
vowels_count = 0
consonants_count = 0

# Считаем количество каждой гласной буквы отдельно
vowel_counts = {v: 0 for v in vowels}

for letter in word:
    if letter in vowels:
        vowels_count += 1
        vowel_counts[letter] += 1
    else:
        consonants_count += 1

print(f"Количество гласных букв: {vowels_count}")
print(f"Количество согласных букв: {consonants_count}")

# Для каждой гласной буквы выводим количество или False, если буквы нет
for v in vowels:
    if vowel_counts[v] == 0:
        print(f"{v}: False")
    else:
        print(f"{v}: {vowel_counts[v]}")
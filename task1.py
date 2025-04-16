text = input("Введіть рядок: ")

if not text.strip():
    print("Рядок порожній. Спробуйте ще раз.")
else:
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    letters = [ch for ch in text if ch.isalpha()]

    if not letters:
        print("У рядку немає жодної літери. Спробуйте знову.")
    else:
        only_vowels = [ch for ch in letters if ch in vowels]
        print("Кількість голосних:", len(only_vowels))
        print("Самі голосні:", only_vowels)

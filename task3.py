text = input("Введіть текст: ").strip()

if not text:
    print("Текст порожній. Спробуйте ще раз.")
else:
    symbols = {}

    for ch in text:
        if ch.isalpha():  # враховуємо лише літери
            symbols[ch] = symbols.get(ch, 0) + 1

    if not symbols:
        print("У тексті немає жодної літери.")
    else:
        print("Частота кожної літери:")
        print(symbols)

        print("Унікальні літери (які зустрічаються 1 раз):")
        print([k for k in symbols if symbols[k] == 1])

        print("Повторювані літери (які зустрічаються більше 1 разу):")
        print([k for k in symbols if symbols[k] > 1])

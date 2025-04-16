list1_input = input("Введіть перший список чисел через пробіл: ").split()
list2_input = input("Введіть другий список чисел через пробіл: ").split()

list1 = []
list2 = []

for item in list1_input:
    try:
        list1.append(int(item))
    except ValueError:
        pass  # ігноруємо неправильні значення

for item in list2_input:
    try:
        list2.append(int(item))
    except ValueError:
        pass

if not list1 and not list2:
    print("Обидва списки порожні або містять некоректні значення.")
else:
    if not list1:
        print("Перший список порожній або некоректний.")
    if not list2:
        print("Другий список порожній або некоректний.")

    combined = list1 + list2
    unique = list(set(combined))
    sorted_list = sorted(unique)

    print("Результат:", sorted_list)

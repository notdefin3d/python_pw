baggage = {
    1: (3, 60, "Іван Іваненко"),
    2: (1, 20, "Марія Петренко"),
    3: (2, 50, "Олег Сидоренко"),
    4: (4, 80, "Анна Коваль"),
    5: (1, 30, "Петро Гончар"),
    6: (5, 100, "Наталія Бондар"),
    7: (2, 45, "Віктор Лисенко"),
    8: (3, 75, "Софія Коваленко"),
    9: (1, 23, "Олександр Мельник"),
    10: (2, 55, "Євгенія Романенко")
}

def print_baggage(data):
    print("\nВсі пасажири:")
    for key, (items, weight, name) in sorted(data.items()):
        print(f"Пасажир {key} - {name}, кількість речей: {items}, загальна вага: {weight} кг, вага однієї речі: {weight/items:.2f} кг")

def add_baggage(data):
    try:
        pid = int(input("Введіть номер пасажира: "))
        if pid in data:
            print("Пасажир з таким номером вже існує!")
            return
        name = input("Введіть ім'я пасажира: ")
        items = int(input("Кількість речей: "))
        weight = float(input("Загальна вага багажу: "))
        data[pid] = (items, weight, name)
        print(f"Додано пасажира {name}")
    except ValueError:
        print("Помилка вводу! Номер і кількість речей - ціле число, вага - число.")

def delete_baggage(data):
    try:
        pid = int(input("Введіть номер пасажира для видалення: "))
        removed = data.pop(pid)
        print(f"Видалено пасажира {removed[2]}")
    except KeyError:
        print("Пасажир не знайдений!")
    except ValueError:
        print("Номер пасажира повинен бути цілим числом!")

def passengers_more_than_two_items(data):
    filtered = {k:v for k,v in data.items() if v[0] > 2}
    print(f"\nКількість пасажирів з більше ніж двома речами: {len(filtered)}")
    for key, (items, weight, name) in sorted(filtered.items()):
        print(f"Пасажир {key} - {name}, кількість речей: {items}, загальна вага: {weight} кг, вага однієї речі: {weight/items:.2f} кг")

def passengers_one_item_under_25kg(data):
    filtered = {k:v for k,v in data.items() if v[0]==1 and v[1]<25}
    if filtered:
        print("\nПасажири з однією річчю <25 кг:")
        for key, (items, weight, name) in sorted(filtered.items()):
            print(f"Пасажир {key} - {name}, кількість речей: {items}, загальна вага: {weight} кг")
    else:
        print("\nНемає пасажирів з однією річчю <25 кг")

def passengers_close_to_avg_weight(data):
    total_items = sum(items for items, _, _ in data.values())
    total_weight = sum(weight for _, weight, _ in data.values())
    avg_weight = total_weight / total_items
    filtered = {k:v for k,v in data.items() if abs((v[1]/v[0])-avg_weight)<=0.5}
    print(f"\nСередня вага однієї речі: {avg_weight:.2f} кг")
    if filtered:
        print("Пасажири, вага однієї речі яких близька до середньої:")
        for key, (items, weight, name) in sorted(filtered.items()):
            print(f"Пасажир {key} - {name}, кількість речей: {items}, загальна вага: {weight} кг, вага однієї речі: {weight/items:.2f} кг")
    else:
        print("Немає пасажирів з вагою близькою до середньої.")

# Основне меню
while True:
    print("\nМеню:")
    print("1 - Показати всіх пасажирів")
    print("2 - Додати пасажира")
    print("3 - Видалити пасажира")
    print("4 - Пасажири з >2 речами")
    print("5 - Пасажири з однією річчю <25 кг")
    print("6 - Пасажири з вагою близькою до середньої")
    print("7 - Вихід")
    
    choice = input("Виберіть дію: ")
    if choice=="1":
        print_baggage(baggage)
    elif choice=="2":
        add_baggage(baggage)
    elif choice=="3":
        delete_baggage(baggage)
    elif choice=="4":
        passengers_more_than_two_items(baggage)
    elif choice=="5":
        passengers_one_item_under_25kg(baggage)
    elif choice=="6":
        passengers_close_to_avg_weight(baggage)
    elif choice=="7":
        print("Вихід")
        break
    else:
        print("Невірний вибір")
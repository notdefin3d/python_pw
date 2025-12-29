import json
import os

DATA_FILE = "passengers.json"
RESULT_FILE = "result.json"


def init_data():
    passengers = [
        {"surname": "Ivanenko", "items": 3, "weight": 18},
        {"surname": "Petrenko", "items": 1, "weight": 4},
        {"surname": "Shevchenko", "items": 4, "weight": 27},
        {"surname": "Koval", "items": 2, "weight": 10},
        {"surname": "Bondar", "items": 5, "weight": 30},
        {"surname": "Tkachenko", "items": 1, "weight": 6},
        {"surname": "Moroz", "items": 2, "weight": 24},
        {"surname": "Rudenko", "items": 3, "weight": 8},
        {"surname": "Lysenko", "items": 1, "weight": 3},
        {"surname": "Savchenko", "items": 4, "weight": 26}
    ]
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(passengers, file, indent=4, ensure_ascii=False)



def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(" Файл не знайдено. Створюється новий.")
        init_data()
        return load_data()



def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def show_data():
    data = load_data()
    print("\n Дані про пасажирів:\n")
    for p in data:
        print(f"Прізвище: {p['surname']}, Речей: {p['items']}, Вага: {p['weight']} кг")



def add_passenger():
    data = load_data()
    surname = input("Прізвище: ")
    items = int(input("Кількість речей: "))
    weight = float(input("Загальна вага (кг): "))
    data.append({"surname": surname, "items": items, "weight": weight})
    save_data(data)
    print("Пасажира додано")



def delete_passenger():
    data = load_data()
    surname = input("Введіть прізвище для видалення: ")
    new_data = [p for p in data if p["surname"] != surname]
    save_data(new_data)
    print("Запис видалено (якщо існував)")


def find_passenger():
    data = load_data()
    surname = input("Пошук за прізвищем: ")
    found = [p for p in data if p["surname"].lower() == surname.lower()]
    print("\n Результат пошуку:")
    for p in found:
        print(p)
    if not found:
        print("Нічого не знайдено")



def solve_task():
    data = load_data()

    more_than_two = [p["surname"] for p in data if p["items"] > 2]

    less_5 = sum(1 for p in data if p["weight"] < 5)
    from_5_to_25 = sum(1 for p in data if 5 <= p["weight"] <= 25)
    more_25 = sum(1 for p in data if p["weight"] > 25)

    result = {
        "passengers_with_more_than_2_items": more_than_two,
        "weight_statistics": {
            "less_than_5kg": less_5,
            "from_5_to_25kg": from_5_to_25,
            "more_than_25kg": more_25
        }
    }

    with open(RESULT_FILE, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print("\n Результати:")
    print("Пасажири з більше ніж 2 речами:", more_than_two)
    print(f"Вага < 5 кг: {less_5}")
    print(f"Вага 5–25 кг: {from_5_to_25}")
    print(f"Вага > 25 кг: {more_25}")
    print("\n Результат записано у файл", RESULT_FILE)



def menu():
    init_data()
    while True:
        print("\n МЕНЮ: ")
        print("1 – Переглянути дані")
        print("2 – Додати запис")
        print("3 – Видалити запис")
        print("4 – Пошук за прізвищем")
        print("5 – варіант 20 результати")
        print("0 – Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_data()
        elif choice == "2":
            add_passenger()
        elif choice == "3":
            delete_passenger()
        elif choice == "4":
            find_passenger()
        elif choice == "5":
            solve_task()
        elif choice == "0":
            print(" Вихід з програми")
            break
        else:
            print(" Невірний вибір")


menu()
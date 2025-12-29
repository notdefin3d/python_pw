import csv

input_file = "prakt9.csv"
output_file = "result_prakt9.csv"

years = [f"{y} [YR{y}]" for y in range(2010, 2020)]

try:
    with open(input_file, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        data = []

        for row in reader:
            if row["Series Name"] == "Inflation, consumer prices (annual %)":
                data.append(row)

        if not data:
            print("Дані з інфляції не знайдено!")
            exit()

        print("\n Inflation, consumer prices (annual %)\n")
        for row in data:
            print(row["Country Name"], end=": ")
            for year in years:
                print(row[year], end="  ")
            print()

except FileNotFoundError:
    print("Файл не знайдено!")
    exit()

results = []

print("\nМінімальні та максимальні значення за роками:\n")

for year in years:
    min_country = ""
    max_country = ""
    min_value = float("inf")
    max_value = float("-inf")

    for row in data:
        try:
            value = float(row[year])
        except:
            continue

        if value < min_value:
            min_value = value
            min_country = row["Country Name"]

        if value > max_value:
            max_value = value
            max_country = row["Country Name"]

    results.append([year, min_country, min_value, max_country, max_value])

    print(f"{year}:")
    print(f"Мінімум - {min_country}: {min_value}%")
    print(f"Максимум - {max_country}: {max_value}%\n")

try:
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([
            "Рік",
            "Країна (мін інфляція)",
            "Інфляція мін (%)",
            "Країна (макс інфляція)",
            "Інфляція макс (%)"
        ])
        writer.writerows(results)

    print("Результати збережено у файл:", output_file)

except:
    print("Помилка запису у файл!")
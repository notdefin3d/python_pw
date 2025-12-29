import pandas as pd

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

df = pd.DataFrame.from_dict(
    baggage,
    orient="index",
    columns=["Кількість речей", "Загальна вага", "ПІБ"]
)

df.index.name = "ID пасажира"

df["Середня вага однієї речі"] = df["Загальна вага"] / df["Кількість речей"]

print("Датафрейм:")
print(df)

print("\nПерші 3 рядки:")
print(df.head(3))


print("\nТипи даних:")
print(df.dtypes)


print("\nКількість рядків і стовпців:")
print(df.shape)


print("\nОписова статистика:")
print(df.describe())


filtered_df = df[df["Середня вага однієї речі"] > 25]
print("\nПасажири із середньою вагою речі понад 25 кг:")
print(filtered_df)

sorted_df = df.sort_values(by="Загальна вага", ascending=False)
print("\nСортування за спаданням загальної ваги:")
print(sorted_df)


grouped = df.groupby("Кількість речей")["Загальна вага"].mean()
print("\nСередня загальна вага за кількістю речей:")
print(grouped)


max_weight = df["Загальна вага"].max()
unique_passengers = df["ПІБ"].nunique()

print("\nМаксимальна загальна вага багажу:", max_weight)
print("Кількість унікальних пасажирів:", unique_passengers)
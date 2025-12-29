import json
import matplotlib.pyplot as plt

with open("result.json", "r", encoding="utf-8") as file:
    data = json.load(file)

stats = data["weight_statistics"]

labels = [
    "Менше 5 кг",
    "Від 5 до 25 кг",
    "Більше 25 кг"
]

values = [
    stats["less_than_5kg"],
    stats["from_5_to_25kg"],
    stats["more_than_25kg"]
]

plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Розподіл пасажирів за вагою багажу")

plt.show()
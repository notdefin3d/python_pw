import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

s = input("Введіть рядок: ")

# Вивід плашки з оригінальним рядком
print(f"Введений рядок: {s}")

# Перевірка: кожен 2-й символ від 5-го до середини
if len(s) >= 5:
    print("Кожен 2-й символ від 5-го до середини:", s[4:len(s)//2:2])
else:
    print("Рядок занадто короткий для цієї операції")
arr = list(map(float, input("Введіть елементи масиву через пробіл: ").split()))

negatives = [x for x in arr if x < 0]
if negatives:
    print("Мінімальний від’ємний елемент:", min(negatives))
else:
    print("Від’ємних елементів немає")
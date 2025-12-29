list = input("Введіть елементи списку без пробілів (цифри і літери): ")

digits = [x for x in list if x.isdigit()]
letters = [x for x in list if x.isalpha()]

print("Цифри:", digits)
print("Літери:", letters)
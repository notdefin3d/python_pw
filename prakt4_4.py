lst = list(map(int, input("Введіть список чисел через пробіл: ").split()))
lst = [x if x >= 0 else 0 for x in lst]
print("Результат:", lst)
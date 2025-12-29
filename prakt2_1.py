import math
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
from prakt2_2 import is_perfect_number

def calculate_z(m, n):
    return (math.sqrt(m) - math.sqrt(n)) / m


m = float(input("Введіть число m: "))
n = int(input("Введіть число n: "))

z = calculate_z(m, n)
print("Значення z =", z)

if is_perfect_number(n):
    print(f"Число {n} є досконалим.")
else:
    print(f"Число {n} не є досконалим.")
n = int(input("Введіть ціле число N (1 < N < 9): "))

for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
for i in range(n, 0, -1):
    print("" * (n - i), end="        ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
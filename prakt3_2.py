import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
word = input("введіть слово: ").lower()

golosni = "аеєиіїоуюя"
prygolosni = ""

print("golosni:")
for ch in word:
    if ch in golosni:
        print(ch)

print("prygolosni:")
for ch in word:
    if ch.isalpha() and ch not in golosni:
        print(ch)
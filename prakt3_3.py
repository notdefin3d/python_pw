import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sentence = input("введіть речення: ")

words = sentence.split()

for word in words:
    letters_count = sum(1 for ch in word if ch.isalpha())
    print(word, "-", letters_count)
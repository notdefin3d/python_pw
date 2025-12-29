text = input("Введіть текст(англійська): ")
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

text_set = set(text) 
vowel_count = sum(1 for ch in text.lower() if ch in vowels)

print("Кількість голосних:", vowel_count)
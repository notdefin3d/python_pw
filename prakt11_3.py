import nltk
import matplotlib.pyplot as plt
from nltk.corpus import *
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

# Завантаження необхідних ресурсів NLTK
nltk.download('stopwords')
nltk.download('gutenberg')

# Виведення списку доступних текстів у корпусі Gutenberg
print("Доступні файли в корпусі Gutenberg:")
print(gutenberg.fileids())

# Завантаження тексту "Paradise Lost" Джона Мільтона
words = nltk.corpus.gutenberg.words('milton-paradise.txt')
print("\nКількість слів у тексті:")
print(len(words))

# Частотний аналіз усіх слів
fdist = FreqDist(words)
top_ten = fdist.most_common(10)
print("\nТоп-10 найчастіших слів (без обробки):")
print(top_ten)

# Видалення стоп-слів
stop_words = set(stopwords.words("english"))
without_stop_words = [word for word in words if word.lower() not in stop_words]

print("\nСлова без стоп-слів:")
print(without_stop_words[:20])  # виводимо перші 20 для зручності

# Частотний аналіз без стоп-слів
fdist = FreqDist(without_stop_words)
top_ten = fdist.most_common(10)
print("\nТоп-10 слів без стоп-слів:")
print(top_ten)

# Видалення розділових знаків
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in without_stop_words if w.translate(table) != ""]

fdist = FreqDist(stripped)
top_ten = fdist.most_common(10)
print("\nТоп-10 слів без стоп-слів і розділових знаків:")
print(top_ten)

# Підготовка даних для графіка
words_plot = [item[0] for item in top_ten]
frequencies = [item[1] for item in top_ten]

# Побудова стовпчикової діаграми
plt.figure(figsize=(12, 6))
plt.bar(words_plot, frequencies)
plt.title('Топ-10 найчастіших слів (без стоп-слів і розділових знаків)', fontsize=15)
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()
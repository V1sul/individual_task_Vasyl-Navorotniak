from collections import Counter
import re

def word_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_count = Counter(words)
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

        for word, count in sorted_word_count:
            print(f'Слово: {word}, Частота: {count}')

word_frequency('consoleAndWordsText.txt')

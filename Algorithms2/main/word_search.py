#Задача 2
import re

def count_word_occurrences(word, mode, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
    except FileNotFoundError:
        return f"Файл {file_path} не знайдено."

    if mode == 1:
        pattern = word
    elif mode == 2:
        pattern = r'\b' + word + r'\b'
    else:
        return "Невірний режим роботи. Виберіть 1 для пошуку часткових співпадінь або 2 для пошуку точних співпадінь."

    occurrences = len(re.findall(pattern, text))
    return f"Слово '{word}' згадується {occurrences} разів у файлі."

print(count_word_occurrences('зуб', 2, 'text.txt'))

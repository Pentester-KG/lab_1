import os
import re
from collections import Counter


def read_file():
    with open('text2.txt', 'r', encoding='utf-8') as f:
        return f.read()

"""
Функция для очистки для очистки и разделения
"""

def clean_and_split_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

def write_word_count_report(words):
    word_count = Counter(words)

    report_file = os.path.join('result', 'text2_words.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
        for word, count in word_count.most_common():
            f.write(f"{word}: {count}\n")


def write_statistics_report(words):
    word_lengths = Counter(len(word) for word in words)
    unique_words = len(set(words))
    punctuation_count = len(re.findall(r'[^\w\s]', ' '.join(words)))

    report_file = os.path.join('result', 'text1_stat.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"Уникальные слова: {unique_words}\n")
        f.write(f"Количество знаков препинания: {punctuation_count}\n")
        for length, count in word_lengths.items():
            f.write(f"Слова с {length} буквами: {count}\n")


def main():
    if not os.path.exists('result'):
        os.makedirs('result')
    text = read_file()
    words = clean_and_split_text(text)
    write_word_count_report(words)
    write_statistics_report(words)



if __name__ == "__main__":
    main()
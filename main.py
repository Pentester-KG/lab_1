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






if __name__ == "__main__":
    main()
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





if __name__ == "__main__":
    main()
'''This code develop a program that counts the occurrence of each word. '''
from collections import Counter

with open('file.txt', 'r') as f:
    words = f.read().split()

count = Counter(words)

for word, c in count.items():
    print(f"{word}: {c}")
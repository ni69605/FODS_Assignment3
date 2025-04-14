'''Write a program to find and replace a specific word in a file with another word.'''
old_word = 'Hi'
new_word = 'Nilima'

with open('file.txt', 'r') as f:
    text = f.read()

text = text.replace(old_word, new_word)

with open('file.txt', 'w') as f:
    f.write(text)

print("Word replaced successfully.")
'''This is a program to copy the content from one file to another file.'''
with open('source.txt', 'r') as src, open('destination.txt', 'w') as dst:
    dst.write(src.read())
print("Hello World! My name is Nilima.")

'''This program implement a program to read a CSV file and display its contents.'''
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print('\t'.join(row))
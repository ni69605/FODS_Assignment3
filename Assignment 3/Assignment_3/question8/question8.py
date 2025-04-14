'''This program is created by Nilima to implement a basic library book management system.'''
import csv
import os

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def to_list(self):
        return [self.book_id, self.title, self.author, 'Available']

class Library:
    def __init__(self, file='library.csv'):
        self.file = file
        if not os.path.exists(file):
            with open(file, 'w', newline='') as f:
                csv.writer(f).writerow(['ID', 'Title', 'Author', 'Status'])

    def add_book(self, book):
        with open(self.file, 'a', newline='') as f:
            csv.writer(f).writerow(book.to_list())
        print("📚 Book added successfully!")

    def issue_return(self, book_id, new_status):
        rows, updated = [], False
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[0] == book_id and row[3] != new_status:
                    row[3] = new_status
                    updated = True
                rows.append(row)
        with open(self.file, 'w', newline='') as f:
            csv.writer(f).writerow(header)
            csv.writer(f).writerows(rows)
        if updated:
            print(f"✅ Book {book_id} has been {'returned' if new_status == 'Available' else 'issued'}.")
        else:
            print("❌ Book not found or already in that status.")

    def search(self, keyword):
        found = False
        with open(self.file, 'r') as f:
            for row in csv.reader(f):
                if keyword.lower() in ' '.join(row).lower():
                    print(' | '.join(row))
                    found = True
        if not found:
            print("❌ No matching books found.")

def main():
    print("📖 Welcome to Nilima's Library System 📖")
    lib = Library()
    while True:
        print("\nMenu:\n1. Add Book\n2. Issue Book\n3. Return Book\n4. Search Book\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            b = Book(input("Book ID: "), input("Title: "), input("Author: "))
            lib.add_book(b)
        elif choice == '2':
            lib.issue_return(input("Enter Book ID to issue: "), 'Issued')
        elif choice == '3':
            lib.issue_return(input("Enter Book ID to return: "), 'Available')
        elif choice == '4':
            lib.search(input("Enter keyword to search: "))
        elif choice == '5':
            print("👋 Goodbye from Nilima's Library!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


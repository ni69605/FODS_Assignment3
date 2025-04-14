"""This program implements a class called Employee that stores and saves employee data to a CSV file."""
import csv
import os

# Employee Class
class Employee:
    def __init__(self):
        self.empid = input("Enter Employee ID: ")
        self.name = input("Enter Name: ")
        self.address = input("Enter Address: ")
        self.contact = input("Enter Contact Number: ")
        self.spouse = input("Enter Spouse Name: ")
        self.children = input("Enter Number of Children: ")
        self.salary = input("Enter Salary: ")

    def to_list(self):
        return [self.empid, self.name, self.address, self.contact, self.spouse, self.children, self.salary]

# Main Program
def main():
    employees = []

    try:
        n = int(input("How many employees do you want to enter? "))
        for _ in range(n):
            print("\nEnter details for employee", _ + 1)
            emp = Employee()
            employees.append(emp.to_list())

        file_name = 'employee.csv'
        file_exists = os.path.exists(file_name)

        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists or os.path.getsize(file_name) == 0:
                writer.writerow(['ID', 'Name', 'Address', 'Contact', 'Spouse', 'Children', 'Salary'])
            writer.writerows(employees)

        print("\nEmployee data saved to employee.csv\n")

        # Display Data
        print("Employee Data:")
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print('\t'.join(row))

    except Exception as e:
        print("Error:", e)

# Run the program
if __name__ == "__main__":
    main()

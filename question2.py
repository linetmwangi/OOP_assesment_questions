class Employee:
    def __init__(self, name, salary):
        self.name = name  # Set name directly without underscores
        self.salary = salary
        self.dateofreg = "10-31-2024"  # Default date of registration

    def display_employee(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}, Date of Registration: {self.dateofreg}"

    def update_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary updated by ${amount}. New Salary: ${self.salary}")
        else:
            print("Salary update amount must be positive.")

# Create an object
emp1 = Employee("John", 5000)

# Display employee details
print(emp1.display_employee())

# Access name directly (since it's not private)
print(emp1.name)

# Update the name attribute
emp1.name = "Alice A"

# Update salary
emp1.update_salary(10000)

# Display updated employee details
print(emp1.display_employee())

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        print(f"{self.name}'s salary: ${self.base_salary}")

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.base_salary + self.bonus
        print(f"{self.name}'s salary with bonus: ${total_salary}")

employee = Employee("Alice", 3000)
manager = Manager("Bob", 5000, 2000)

employee.calculate_salary()
manager.calculate_salary()

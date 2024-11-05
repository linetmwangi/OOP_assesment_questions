class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

result1 = Calculator.add(5, 10)
print("Result of first addition:", result1)
print("Addition count:", Calculator.count)

result2 = Calculator.add(3, 7)
print("Result of second addition:", result2)
print("Addition count:", Calculator.count)

result3 = Calculator.add(12, 8)
print("Result of third addition:", result3)
print("Addition count:", Calculator.count)

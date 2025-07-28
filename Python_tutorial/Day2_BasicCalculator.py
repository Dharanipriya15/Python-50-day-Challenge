# Day 2 - Basic Calculator 🧮

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "❌ Cannot divide by zero"
        return num1 / num2
    else:
        return "❌ Invalid operator. Please use +, -, *, or /"

if __name__ == "__main__":
    print("Welcome to the Basic Calculator!")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose an operator (+, -, *, /): ")

        result = calculate(a, b, op)
        print(f"Result: {result}")
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

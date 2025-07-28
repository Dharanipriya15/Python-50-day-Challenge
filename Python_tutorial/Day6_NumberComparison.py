# Day 6 - Number Comparison 🔍

def compare_numbers(a, b):
    if a > b:
        return f"{a} is larger than {b}"
    elif a < b:
        return f"{a} is smaller than {b}"
    else:
        return f"Both numbers are equal: {a} = {b}"

if __name__ == "__main__":
    print("🔢 Welcome to Day 6: Number Comparison")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = compare_numbers(num1, num2)
        print("✅ Result:", result)

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

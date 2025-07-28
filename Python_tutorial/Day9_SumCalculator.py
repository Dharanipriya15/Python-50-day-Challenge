# Day 9 - Sum Calculator using Loop ➕

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    print("➕ Welcome to Day 9: Sum Calculator")

    try:
        number = int(input("Enter a positive integer: "))
        if number < 1:
            print("❌ Please enter a number greater than 0.")
        else:
            result = calculate_sum(number)
            print(f"✅ The sum of numbers from 1 to {number} is: {result}")
    except ValueError:
        print("❌ Invalid input. Please enter a valid integer.")

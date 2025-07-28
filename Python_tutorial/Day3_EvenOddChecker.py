# Day 3 - Even or Odd Checker 🔍

def is_even(number):
    return number % 2 == 0

def check_single_number():
    try:
        num = int(input("Enter a number to check if it's even or odd: "))
        if is_even(num):
            print(f"{num} is Even ✅")
        else:
            print(f"{num} is Odd 🔵")
    except ValueError:
        print("❌ Please enter a valid integer.")

def check_list_of_numbers():
    try:
        numbers_input = input("Enter a list of numbers (comma-separated): ")
        numbers = [int(n.strip()) for n in numbers_input.split(",")]

        print("\nResult:")
        for num in numbers:
            type_of_num = "Even ✅" if is_even(num) else "Odd 🔵"
            print(f"{num} is {type_of_num}")
    except ValueError:
        print("❌ Invalid input. Make sure you enter numbers only.")

if __name__ == "__main__":
    print("🔢 Welcome to Day 3: Even or Odd Checker!")

    check_single_number()
    print("\n--- Now check a list of numbers ---")
    check_list_of_numbers()

# Day 8 - Count Positive, Negative, and Zero Numbers 🔢

def count_numbers(numbers):
    positive = sum(1 for n in numbers if n > 0)
    negative = sum(1 for n in numbers if n < 0)
    zero = sum(1 for n in numbers if n == 0)
    return positive, negative, zero

if __name__ == "__main__":
    print("📊 Welcome to Day 8: Count Positive, Negative & Zero")

    try:
        input_str = input("Enter numbers (comma-separated): ")
        number_list = [int(n.strip()) for n in input_str.split(",")]

        pos, neg, zero = count_numbers(number_list)

        print(f"\n✅ Count Results:")
        print(f"Positive Numbers: {pos}")
        print(f"Negative Numbers: {neg}")
        print(f"Zeros: {zero}")

    except ValueError:
        print("❌ Invalid input. Please enter integers only, separated by commas.")

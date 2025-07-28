# Day 5 - Shopping Bill Calculator 🛒

def calculate_total(item_prices, tax_percentage):
    subtotal = sum(item_prices)
    tax_amount = subtotal * (tax_percentage / 100)
    total = subtotal + tax_amount
    return subtotal, tax_amount, total

if __name__ == "__main__":
    print("🛍️ Welcome to Day 5: Shopping Bill Calculator")

    try:
        prices = []
        for i in range(1, 4):
            price = float(input(f"Enter price of item {i}: ₹"))
            prices.append(price)

        tax = float(input("Enter tax percentage: "))

        subtotal, tax_amt, total = calculate_total(prices, tax)

        print("\n🧾 Bill Summary")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax (@{tax}%): ₹{tax_amt:.2f}")
        print(f"Total: ₹{total:.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")

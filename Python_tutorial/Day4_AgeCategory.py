# Day 4 - Age Category Classifier 👨‍👩‍👧‍👦

def classify_age(age):
    if age < 0:
        return "❌ Invalid age"
    elif age <= 12:
        return "👶 Child"
    elif age <= 19:
        return "🧒 Teenager"
    elif age <= 59:
        return "🧑 Adult"
    else:
        return "👴 Senior"

if __name__ == "__main__":
    print("📆 Welcome to Day 4: Age Category Checker")

    try:
        age = int(input("Enter your age: "))
        category = classify_age(age)
        print(f"You are classified as: {category}")
    except ValueError:
        print("❌ Please enter a valid number.")

# Day 7 - Simple Password Checker 🔐

def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

if __name__ == "__main__":
    print("🔐 Welcome to Day 7: Simple Password Validator")

    password = input("Enter your password: ")

    if is_valid_password(password):
        print("✅ Password is valid (meets minimum length).")
    else:
        print("❌ Password is too short! Must be at least 8 characters.")

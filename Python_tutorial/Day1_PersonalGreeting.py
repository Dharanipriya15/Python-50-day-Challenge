# Day 1 - Personal Greeting Program

def personal_greeting():
    print("👋 Welcome to Day 1 of the Python Challenge!")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("What is your favorite color? ")

    message = f"\nHello {name}! You're {age} years young and love the color {color}. That's awesome! 🎉"
    print(message)

if __name__ == "__main__":
    personal_greeting()

# Day 10 - Store and Display Names with Lengths 👥

def collect_names(count=5):
    names = []
    for i in range(1, count + 1):
        name = input(f"Enter name {i}: ")
        names.append(name)
    return names

def display_name_lengths(names):
    print("\n📋 Name List with Lengths:")
    for name in names:
        print(f"{name} - {len(name)} characters")

if __name__ == "__main__":
    print("👥 Welcome to Day 10: Names and Lengths Checker")

    names_list = collect_names()
    display_name_lengths(names_list)

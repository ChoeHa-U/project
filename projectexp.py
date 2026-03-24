def add_expense():
    category = input("Enter category (Food/Travel/Shopping/etc.): ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    file = open("expenses.txt", "a")
    file.write(category + "," + str(amount) + "\n")
    file.close()
    print("Expense added successfully!")


def view_expenses():
    try:
        file = open("expenses.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No expenses found! Add some expenses first.")
        return

    if len(lines) == 0:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'No.':<5} {'Category':<15} {'Amount':>10}")
    print("-" * 32)

    count = 1
    for line in lines:
        line = line.strip()
        parts = line.split(",")
        category = parts[0]
        amount = parts[1]
        print(f"{count:<5} {category:<15} {float(amount):>10.2f}")
        count = count + 1

    print("-" * 32)


def calculate_total():
    try:
        file = open("expenses.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No expenses found! Add some expenses first.")
        return

    if len(lines) == 0:
        print("No expenses recorded yet.")
        return

    total = 0
    for line in lines:
        line = line.strip()
        parts = line.split(",")
        amount = float(parts[1])
        total = total + amount

    print("\n--- Total Expense ---")
    print(f"Total amount spent: Rs. {total:.2f}")


def category_wise_count():
    try:
        file = open("expenses.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No expenses found! Add some expenses first.")
        return

    if len(lines) == 0:
        print("No expenses recorded yet.")
        return

    category_count = {}

    for line in lines:
        line = line.strip()
        parts = line.split(",")
        category = parts[0]

        if category in category_count:
            category_count[category] = category_count[category] + 1
        else:
            category_count[category] = 1

    print("\n--- Category-wise Count ---")
    print(f"{'Category':<15} {'Count':>8}")
    print("-" * 25)
    for category in category_count:
        print(f"{category:<15} {category_count[category]:>8}")
    print("-" * 25)


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category-wise Count")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        category_wise_count()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

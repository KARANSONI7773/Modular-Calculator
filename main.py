# main.py

import calc_operations
import user_input

print("=== Modular Calculator ===")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

while True:
    choice = input("\nEnter choice (1-5): ")

    if choice == "5":
        print("Exiting... Bye 👋")
        break

    a, b = user_input.get_numbers()

    if choice == "1":
        print("Result:", calc_operations.add(a, b))
    elif choice == "2":
        print("Result:", calc_operations.sub(a, b))
    elif choice == "3":
        print("Result:", calc_operations.mul(a, b))
    elif choice == "4":
        print("Result:", calc_operations.div(a, b))
    else:
        print("Invalid choice! Try again.")


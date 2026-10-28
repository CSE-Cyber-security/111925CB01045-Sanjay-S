
def calculator():
    print("===== Simple Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        choice = input("\nChoose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = num1 + num2
                operator = "+"

            elif choice == "2":
                result = num1 - num2
                operator = "-"

            elif choice == "3":
                result = num1 * num2
                operator = "*"

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
                operator = "/"

            print(f"Result: {num1:g} {operator} {num2:g} = {result:g}")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    calculator()

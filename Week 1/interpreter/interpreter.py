def main():
    try:
        user_input = input("Enter an arithmetic expression (x y z): ")
        x, operator, z = user_input.split()

        # Convert x and z to integers
        x = int(x)
        z = int(z)

        # Perform the arithmetic operation based on the operator
        if operator == '+':
            result = x + z
        elif operator == '-':
            result = x - z
        elif operator == '*':
            result = x * z
        elif operator == '/':
            result = x / z
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            return

        # Format the result to one decimal place
        formatted_result = f"{result:.1f}"
        print(f"Result: {formatted_result}")
    except ValueError:
        print("Invalid input. Please follow the format: x y z")


if __name__ == "__main__":
    main()

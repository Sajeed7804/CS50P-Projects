user_input = input("What is the answer to the Great Question? ").strip()
# Convert the input to lowercase for case-insensitive comparison
user_input_lower = user_input.lower()

# Check if the input matches 42, "forty-two", or "forty two"
if user_input_lower == "42" or user_input_lower == "forty-two" or user_input_lower == "forty two":
    print("Yes")
else:
    print("No")

user_greeting = input("Enter your greeting: ").strip().lower()

if user_greeting.startswith("hello"):
    print("$0")
elif user_greeting.startswith("h"):
    print("$20")
else:
    print("$100")

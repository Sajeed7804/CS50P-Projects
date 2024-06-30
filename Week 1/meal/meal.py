def main():
    try:
        user_input = input("Enter the time (24-hour format, e.g., 7:30): ")
        converted_time = convert(user_input)

        if 7.0 <= converted_time <= 8.0:
            print("Breakfast time")
        elif 12.0 <= converted_time <= 13.0:
            print("Lunch time")
        elif 18.0 <= converted_time <= 19.0:
            print("Dinner time")
        # No output if it's not mealtime

    except ValueError:
        print("Invalid input. Please use the format HH:MM (24-hour time).")


def convert(time):
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(":"))
    # Convert minutes to hours (e.g., 30 minutes = 0.5 hours)
    return hours + minutes / 60


if __name__ == "__main__":
    main()

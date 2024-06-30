def convert(text):
    # replace :) with 🙂
    text = text.replace(":)", "🙂")
    # replace :( with 🙁
    text = text.replace(":(", "🙁")
    # return the modified string
    return text


def main():
    # Promt user for input
    user_input = input("Put your text here: ").strip()
    # Modify input
    converted_text = convert(user_input)
    # Show output
    print(converted_text)


main()

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    if match := re.search(regex, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():

    print(greetings('Alexandra'))
    print(greetings('Wil'))
    print(greetings())
    print(greetings(42))


def greetings(s = "noble stranger"):

    if not isinstance(s, str):
        return "Error! It was not a name."

    return f"hello, {s}."


if __name__ == "__main__":
    main()

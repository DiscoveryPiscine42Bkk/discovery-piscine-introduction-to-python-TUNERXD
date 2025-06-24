#!/usr/bin/env python3

def main():

    persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
    print(array_of_names(persons))


def array_of_names(dict):
    array = []

    for key in dict:
        array.append(f"{key.capitalize()} {dict[key].capitalize()}")
    return array
    

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():

    dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
    print(find_the_redheads(dupont_family))


def find_the_redheads(dict):
    array = []

    for key in dict:
        if dict[key] == "red":
            array.append(key)
    return array
    

if __name__ == "__main__":
    main()


#!/usr/bin/env python3

def main():

    women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)

def famous_births(dict):

    sorted_dict = sorted(dict.items(), key=lambda item: item[1]["date_of_birth"])

    for key,value in sorted_dict:
        print(f"{value["name"]} is a great scientist born in {value["date_of_birth"]}.")


if __name__ == "__main__":
    main()


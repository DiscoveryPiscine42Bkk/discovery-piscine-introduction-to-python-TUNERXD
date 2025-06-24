#!/usr/bin/env python3

def main():

    women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")


def average(dict):

    
    total = 0
    for key in dict:
        total += dict[key]

    avg = total / len(dict)
    return avg
    

if __name__ == "__main__":
    main()


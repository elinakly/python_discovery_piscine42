#!/usr/bin/env python3

def array_of_names(persons):
    names = []
    for first, last in persons.items():
        full = f"{first.capitalize()} {last.capitalize()}"
        names.append(full)
    return (names)

if __name__ == "__main__":
    persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }
    print(array_of_names(persons))
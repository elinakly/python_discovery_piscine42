#!/usr/bin/env python3

def find_the_redheads(persons):
    redheads = filter(lambda name: persons[name] == 'red', persons.keys())
    return list(redheads)

if __name__ == "__main__":
    dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
    }
    print(find_the_redheads(dupont_family))
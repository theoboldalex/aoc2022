import os
import requests
from dotenv import load_dotenv

def process_data(sample: str) -> list:
    result = []
    items = [s for s in sample.strip().split("\n")]
    for i in items:
        first_compartment, second_compartement = i[:len(i)//2], i[len(i)//2:]
        result.append([first_compartment, second_compartement])

    return result

def get_dupe_item(bag: list) -> str:
    return [item for item in bag[0] if item in bag[1]][0]

def encode_char_to_int(char: str) -> int:
    if ord(char) >= 97:
        return ord(char) - 96
    return ord(char) - 38

def main():
    load_dotenv()
    r = requests.get("https://adventofcode.com/2022/day/3/input", cookies={"session": os.environ["COOKIE"]})
    data = process_data(r.text)
    print(f"part 1: {sum([encode_char_to_int(get_dupe_item(i)) for i in data])}")
    # read from input file
    # get the dupe for each bag
    # encode them all
    # sum the resulting list

if __name__ == "__main__":
    main()

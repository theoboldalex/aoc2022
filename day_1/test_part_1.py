import os
import requests
from dotenv import load_dotenv

def process_data(data: str) -> list:
    elves = [l.split("\n") for l in data.strip().split("\n\n")]
    return [sum([int(i) for i in x]) for x in elves]

def get_top(data: list, limit: int) -> list:
    data.sort(reverse=True)
    return data[:limit]

def main():
    load_dotenv()
    cookies = {"session": os.environ["COOKIE"]}
    r = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookies)
    print(f"part 1: {max(process_data(r.text))}")
    print(f"part 2: {sum(get_top(process_data(r.text), 3))}")

########## TESTS ############
sample_data = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
def test_max_calories():
    assert process_data(sample_data) == 24000


if __name__ == "__main__":
    main()

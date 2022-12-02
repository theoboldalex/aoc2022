import os
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    cookies = {"session": os.environ["COOKIE"]}
    r = requests.get("https://adventofcode.com/2022/day/2/input", cookies=cookies)
    print(f"part 1: {}")
    print(f"part 2: {}")

if __name__ == "__main__":
    main()

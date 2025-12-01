import sys
import time
import argparse

def read_input(day, is_test):
    suffix = ""
    if is_test:
        suffix = "-test"

    with open(f"puzzles/day{day}/data{suffix}.txt", "r+") as dataFile:
        print(f"****** DAY {day} ******")
        return dataFile.readlines()

def run_part(day, part, input):
    print(f"--- Executing part {part} ---")

    fnc_part_one = 'execute_part_one'
    fnc_part_two = 'execute_part_two'
    importlib = __import__('importlib')
    mod = importlib.import_module(f"puzzles.day{day}.program")

    func_one = getattr(mod, fnc_part_one)
    func_two = getattr(mod, fnc_part_two)

    func_one(input) if part == 1 else func_two(input)

def main():

    parser = argparse.ArgumentParser(description="AoC 2025 solutions")
    parser.add_argument('day', type=int, help="Number of day")
    parser.add_argument('-t', '--test', action="store_true", help="Run on test data")
    args = parser.parse_args()

    input_data = read_input(args.day, args.test)

    print(f"{args}")
    
    start_time = time.time()
    run_part(args.day, 1, input_data)
    print("--- Solved in %s seconds ---\n" % (time.time() - start_time))

    start_time = time.time()
    run_part(args.day, 2, input_data)
    print("--- Solved in %s seconds ---\n" % (time.time() - start_time))

if __name__ == "__main__":
    main()

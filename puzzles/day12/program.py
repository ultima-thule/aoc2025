import itertools

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []

    for row, line in enumerate(input):
        data.append(list(line.strip()))

    return data

def execute_part_one(input: list[str]) -> None:
    data = extract_data(input)

    count = 0

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    data = extract_data(input)

    count = 0

    print(f"Solved 2: {count}")

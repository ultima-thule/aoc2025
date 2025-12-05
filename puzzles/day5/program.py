def extract_data(input: list[str]):
    '''Extract and transform text data'''

    data = set()

    for row, line in enumerate(input):
        for col, item in enumerate(line):
            if item == "@":
                data.add((row, col))

    return data

def execute_part_one(input: list[str]) -> None:
    count = 0


    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    print(f"Solved 2: {count}") 

def extract_data(input: list[str]):
    '''Extract and transform text data'''

    data = set()

    for row, line in enumerate(input):
        for col, item in enumerate(line):
            if item == "@":
                data.add((row, col))

    return data

def check_if_can_remove(r, c, rolls):
    if (r, c) in rolls:
        to_check = {(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)}
        if len(rolls & to_check) < 4:
            return True

    return False


def execute_part_one(input: list[str]) -> None:
    count = 0

    rolls = extract_data(input)

    for r in rolls:
        if check_if_can_remove (r[0], r[1], rolls):
            count += 1

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    rolls = extract_data(input)

    while True:
        removed = 0
        rolls_to_remove = set()
        for r in rolls:
            if check_if_can_remove (r[0], r[1], rolls):
                removed += 1
                rolls_to_remove.add((r[0], r[1]))
        
        rolls = rolls.difference(rolls_to_remove)
        
        count += removed
        if removed == 0:
            break


    print(f"Solved 2: {count}") 

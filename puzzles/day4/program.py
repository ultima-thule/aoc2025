def extract_data(input: list[str]):
    '''Extract and transform text data'''

    row = 0
    max_row = -1
    max_col = -1

    ret = set()

    for line in input:
        col = 0
        max_col = len(line.strip())
        for pos in line:
            if pos == "@":
                ret.add((row, col))
            col += 1
        row += 1

    max_row = row

    return ret, max_row, max_col


def print_shelf(rolls, max_row, max_col):
    # print(rolls)

    print(f"{max_row} x {max_col}")
    for r in range(max_row):
        for c in range (max_col):
            if (r, c) in rolls:
                print("@", end='')
            else:
                print(".", end='')
        print("\n")

def check_if_can_remove(r, c, rolls, max_row, max_cols):
    if (r, c) in rolls:
        to_check = {(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)}
        if len(rolls & to_check) < 4:
            return True

    return False


def execute_part_one(input: list[str]) -> None:
    count = 0

    rolls, max_row, max_col = extract_data(input)

    for r in range(max_row):
        for c in range (max_col):
            if check_if_can_remove (r, c, rolls, max_row, max_col):
                count += 1

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    rolls, max_row, max_col = extract_data(input)

    while True:
        removed = 0
        rolls_to_remove = set()
        for r in range(max_row):
            for c in range (max_col):
                if check_if_can_remove (r, c, rolls, max_row, max_col):
                    removed += 1
                    rolls_to_remove.add((r, c))
        
        rolls = rolls.difference(rolls_to_remove)
        
        count += removed
        if removed == 0:
            break


    print(f"Solved 2: {count}") 

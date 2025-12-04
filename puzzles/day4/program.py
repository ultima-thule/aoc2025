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


def execute_part_one(input: list[str]) -> None:
    count = 0

    rolls, max_row, max_col = extract_data(input)

    # print(rolls)
    # print(f"{max_row} x {max_col}")
    # for r in range(max_row):
    #     for c in range (max_col):
    #         if (r, c) in rolls:
    #             print("@", end='')
    #         else:
    #             print(".", end='')
    #     print("\n")

    for r in range(max_row):

        for c in range (max_col):
            cnt = 0
            if (r, c) in rolls:
                if (r-1, c) in rolls:
                    cnt += 1
                if (r+1, c) in rolls:
                    cnt += 1
                if (r, c-1) in rolls:
                    cnt += 1
                if (r, c+1) in rolls:
                    cnt += 1
                if (r-1, c-1) in rolls:
                    cnt += 1
                if (r-1, c+1) in rolls:
                    cnt += 1
                if (r+1, c-1) in rolls:
                    cnt += 1
                if (r+1, c+1) in rolls:
                    cnt += 1
                # print(f"{(c, r)} has {cnt}")
                if cnt < 4:
                    count += 1

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    rolls, max_row, max_col = extract_data(input)
    
    print(f"Solved 2: {count}") 

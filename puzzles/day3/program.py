def extract_data(input: list[str]):
    '''Extract and transform text data'''

    for line in input:
            yield [int(x) for x in line.strip()]


def get_max_rating(bank):
    if len(bank) < 2:
        return 0
     
    if len(bank) == 2:
        return 10 * bank[0] + bank[1]

    idx_i = len(bank) - 2
    idx_j = len(bank) - 1

    max_i = bank[idx_i]
    max_j = bank[idx_j]

    for i in range (len(bank)-2, -1, -1):
        # print(f"{i}: {bank[i]}, {bank[i+1]} (max: {max_i}, {max_j})")
        if bank[i] >= max_i:
            max_i = bank[i]
            idx_i = i
        
    for j in range (len(bank)-1, idx_i, -1):
        # print(f"{i}: {bank[i]}, {bank[i+1]} (max: {max_i}, {max_j})")
        if bank[j] >= max_j:
            max_j = bank[j]
            idx_j = j

    return 10 * max_i + max_j
     

def execute_part_one(input: list[str]) -> None:
    count = 0

    for bank in extract_data(input):
        count += get_max_rating(bank)

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
        count = 0

        for line in extract_data(input):
            continue

        print(f"Solved 2: {count}")

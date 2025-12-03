def extract_data(input: list[str]):
    '''Extract and transform text data'''

    for line in input:
            yield [int(x) for x in line.strip()]

def get_max_rating(bank, length):
    if len(bank) < length:
        return 0
     
    if len(bank) == length:
        return int(str(bank))

    max_nums = bank[len(bank)-length:]
    max_idx = [x for x in range(len(bank)-length, len(bank))]

    for i in range (len(bank)-length, -1, -1):
        if bank[i] >= max_nums[0]:
            max_nums[0] = bank[i]
            max_idx[0] = i

    for r in range(1, length):
        for j in range (max_idx[r]-1, max_idx[r-1], -1):
            if bank[j] >= max_nums[r]:
                max_nums[r] = bank[j]
                max_idx[r] = j

    num_list_string = map(str, max_nums)
    ret = "".join(num_list_string)

    return int(ret)
     

def execute_part_one(input: list[str]) -> None:
    count = 0

    for bank in extract_data(input):
        count += get_max_rating(bank, 2)

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    for bank in extract_data(input):
        count += get_max_rating(bank, 12)   

    print(f"Solved 2: {count}")

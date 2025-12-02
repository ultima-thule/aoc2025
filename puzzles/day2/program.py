def extract_data(input: list[str]):
    '''Extract and transform text data'''

    for r in input[0].strip().split(","):
        ret = r.split("-")
        yield (ret[0].lstrip('0'), ret[1].lstrip('0'))

def execute_part_one(input: list[str]) -> None:
    count = 0

    invalid_nums = []

    for line in extract_data(input):
        left = line[0]
        right = line[1]

        for num in range (int(left), int(right) + 1):
            s = str(num)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                if s[:mid] == s[mid:]:
                    invalid_nums.append(num)

    count = sum(invalid_nums)

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    print(f"Solved 2: {count}")

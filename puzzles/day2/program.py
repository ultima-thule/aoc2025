def extract_data(input: list[str]):
    '''Extract and transform text data'''

    for r in input[0].strip().split(","):
        ret = r.split("-")
        yield (int(ret[0].lstrip('0')), int(ret[1].lstrip('0')))


def execute_part_one(input: list[str]) -> None:
    count = 0

    invalid_nums = []

    for line in extract_data(input):
        left = line[0]
        right = line[1]

        for num in range (left, right + 1):
            full_num = str(num)
            # is even number
            if len(full_num) % 2 == 0:
                mid = len(full_num) // 2
                # compare both parts
                if full_num[:mid] == full_num[mid:]:
                    invalid_nums.append(num)

    count = sum(invalid_nums)

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    invalid_nums = set()

    for line in extract_data(input):
        left = line[0]
        right = line[1]

        for num in range (left, right + 1):
            full_num = str(num)

            # consider dividing into repeats of lenght from 1 to half of the string len
            for repeat_len in range(1, len(full_num) // 2 + 1):
                # get repeat pattern
                part_num = full_num[:repeat_len]
                # num can be divided into equal parts of repeat_len
                if len(full_num) % repeat_len == 0:
                    # calculate number of repeats
                    repeat = len(full_num) // repeat_len
                    # generate string and compare
                    if part_num * repeat == full_num:
                        invalid_nums.add(num)

    count = sum(invalid_nums)

    print(f"Solved 2: {count}")

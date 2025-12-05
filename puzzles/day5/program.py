def extract_data(input: list[str]):
    '''Extract and transform text data'''

    ranges = []
    data = []

    for line in input:
        s = line.strip().split("-")
        # print(s)
        if len(s) == 2:
            diff = int(s[1]) - int(s[0])
            ranges.append((int(s[0]), diff))
        elif len(s) ==1 and s[0] != '':
            data.append(int(s[0]))
    return ranges, data

def execute_part_one(input: list[str]) -> None:
    count = 0

    ranges, data = extract_data(input)

    # print(ranges)
    # print(data)

    ranges.sort(key=lambda x: x[0])

    for d in data:
        for r in ranges:
            if d >= r[0] and d <= r[0] + r[1]:
                count += 1
                break

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    print(f"Solved 2: {count}") 

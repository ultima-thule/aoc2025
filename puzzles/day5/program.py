def extract_data(input: list[str]):
    '''Extract and transform text data'''

    ranges = []
    data = []

    for line in input:
        s = line.strip().split("-")
        if len(s) == 2:
            ranges.append((int(s[0]), int(s[1])))
        elif s[0] != '':
            data.append(int(s[0]))
    return ranges, data

def execute_part_one(input: list[str]) -> None:
    count = 0

    ranges, data = extract_data(input)

    for d in data:
        for r in ranges:
            if d >= r[0] and d <= r[1]:
                count += 1
                break

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    ranges, _ = extract_data(input)

    ranges.sort(key=lambda x: (x[0], x[1]))

    new_ranges = [ranges.pop(0)]

    while len(ranges) > 0:
        r_prev = new_ranges[-1]
        r_next = ranges.pop(0)

        # ranges not overlapping
        if r_prev[1] < r_next[0]:
            new_ranges.append(r_next)
        # ranges overlapping
        else:
            new_ranges[-1] = (min(r_prev[0], r_next[0]), max(r_prev[1], r_next[1]))

    for r in new_ranges:
        count += r[1] - r[0] + 1

    print(f"Solved 2: {count}") 

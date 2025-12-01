def extract_data(input: list[str]):
    '''Extract and transform text data'''
    for line in input:
        direction = line[0]
        clicks = int(line[1:].strip())
        yield (direction, clicks)

def execute_part_one(input: list[str]) -> None:
    count = 0

    arrow = 50
    dial_len = 100

    for line in extract_data(input):
        direction = line[0]
        dist = line[1]

        if direction == "L":
            arrow = (arrow - dist) % dial_len
            # print(f"L <= by {dist} to {arrow}")
        elif direction == "R":
            arrow = (arrow + dist) % dial_len
            # print(f"P => by {dist} to {arrow}")

        if arrow == 0:
            count += 1

    print(f"Solved 1: {count}")


def execute_part_two(input: list[str]) -> None:
    count = 0

    arrow = 50
    dial_len = 100

    for line in extract_data(input):
        direction = line[0]
        dist = line[1]
        passes = 0

        start_pos = arrow

        if direction == "L":
            arrow = (arrow - dist) % dial_len
            passes = (arrow + dist) // dial_len
            
            if start_pos == 0:
                passes = max(0, passes - 1)
            elif arrow == 0:
                passes += 1
            # print(f"L from {start_pos} - {dist} = {arrow}, passes: {passes}")

        elif direction == "R":
            arrow = (arrow + dist) % dial_len
            passes = (start_pos + dist) // dial_len

            # print(f"R from {start_pos} + {dist} = {arrow}, passes: {passes}")

        count += passes

    print(f"Solved 2: {count}")

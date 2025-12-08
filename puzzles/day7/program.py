from collections import defaultdict

def extract_data(input: list[str]):
    '''Extract and transform text data'''

    data = []

    for row, line in enumerate(input):
        l = line.strip()
        if len(l) > 0:
            data.append(list(l))

    return data

def bounce(data):

    beams = defaultdict(int)
    c = data[0].index('S')
    beams[c] = 1
    splits = 0

    for r in range (len(data)-1):
        for c, count in list(beams.items()):
            tile = data[r + 1][c]
            if tile == "^":
                splits += 1

                beams[c-1] += count
                beams[c+1] += count
                del beams[c]
    
    return splits, beams

def execute_part_one(input: list[str]) -> None:
    data = extract_data(input)
    splits, _ = bounce(data)

    print(f"Solved 1: {splits}")

def execute_part_two(input: list[str]) -> None:
    data = extract_data(input)
    _, beams = bounce(data)

    print(f"Solved 2: {sum(beams.values())}") 

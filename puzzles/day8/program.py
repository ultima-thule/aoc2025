import math

def extract_data(input: list[str]):
    '''Extract and transform text data'''
    data = []

    for row, line in enumerate(input):
        data.append([int(x) for x in line.strip().split(',')])

    return data

def calc_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def get_key(item):
    return f"{item[0]}-{item[1]}-{item[2]}"

def get_key_double(item1, item2):
    first_first = True
    if item1[0] < item2[0]:
        first_first = True
    elif item2[0] < item1[0]:
        first_first = False
    else:
        if item1[1] < item2[1]:
            first_first = True
        elif item2[1] < item1[1]:
            first_first = False
        else:
            if item1[2] < item2[2]:
                first_first = True
            elif item2[2] < item1[2]:
                first_first = False

    if first_first:
        return f"{get_key(item1)}:{get_key(item2)}"
    return f"{get_key(item2)}:{get_key(item1)}"

def calc_all_dist(data):
    distances = {}

    while len(data) > 0:
        next_elem = data.pop()
        for elem in data:
            dist = calc_distance(next_elem[0], next_elem[1], next_elem[2], elem[0], elem[1], elem[2])

            key1 = get_key_double(next_elem, elem)
            if key1 not in distances:
                distances[key1] = dist
    
    return distances

def build_circuits(distances, limit, is_part_one):

    circuits = []
    cnt = 0

    last_added = ""
    do_break = False

    while not do_break:
        min_key = min(distances, key=distances.get)
        last_added = min_key

        splitted = min_key.split(":")

        found_1 = found_2 = False
        circ_1 = circ_2 = -1

        p_1 = splitted[0]
        p_2 = splitted[1]
       
        for i, c in enumerate(circuits):
            if p_1 in c and p_2 in c:
                found_1 = found_2 = True
                circ_1 = circ_2 = i
                break
            elif p_1 in c and p_2 not in c:
                found_1 = True
                circ_1 = i
            elif p_1 not in c and p_2 in c:
                found_2 = True
                circ_2 = i

        if not found_1 and not found_2:
            circuits.append({p_1, p_2})
        else:
            if found_1 and not found_2:
                circuits[circ_1].add(p_2)
            elif not found_1 and found_2:
                circuits[circ_2].add(p_1)
            elif found_1 and found_2 and circ_1 != circ_2:
                circuits[circ_1] = circuits[circ_1].union(circuits[circ_2])
                circuits.pop(circ_2)

        del distances[min_key]
        cnt += 1

        if is_part_one:
            do_break = cnt >= limit
        else:
            do_break = (len(circuits) == 1 and len(circuits[0]) == limit)

    return circuits, last_added

def execute_part_one(input: list[str]) -> None:
    data = extract_data(input)

    distances = calc_all_dist(data)
    #test data
    circuits, _ = build_circuits(distances, 10, True)
    # real data
    # circuits, _ = build_circuits(distances, 1000, True)

    circuits.sort(key=lambda x: len(x))

    count = 1
    for i in range (len(circuits) - 1, len(circuits) - 4, -1):
        count *= len(circuits[i])

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    data = extract_data(input)
    distances = calc_all_dist(data)

    _, last_added = build_circuits(distances, len(data), False)

    splitted = last_added.split(':')
    point_1 = splitted[0].split('-')
    point_2 = splitted[1].split('-')

    count = int(point_1[0]) * int(point_2[0])

    print(f"Solved 2: {count}")

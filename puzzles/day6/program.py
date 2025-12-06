import math

def extract_data_1(input: list[str]):
    '''Extract and transform text data'''

    data_tmp = []

    for row, line in enumerate(input):
        tmp = line.strip().split()
        if tmp[0] == "*" or tmp[0] == "+":
            operations = tmp
        else:
            data_tmp.append([int(x) for x in tmp])

    data = [[data_tmp[j][i] for j in range(len(data_tmp))] for i in range(len(data_tmp[0]))]

    return data, operations

def extract_data_2(input: list[str]):
    tmp_data = []

    for row, line in enumerate(input):
        if line[0] == "*" or line[0] == "+":
            operations = line.strip().split()
        else:
            tmp_data.append(list(line.replace('\n', '')))

    transpose = [[tmp_data[j][i] for j in range(len(tmp_data))] for i in range(len(tmp_data[0]))]

    data = []
    for i in range(len(transpose)):
        data.append("".join(transpose[i]))
    data.append('   ')

    return data, operations

def execute_part_one(input: list[str]) -> None:
    count = 0

    data, operations = extract_data_1(input)

    for i, oper in enumerate(operations):
        if oper == "+":
            count += sum(data[i])
        elif oper == "*":
            count += math.prod(data[i])

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
    count = 0

    data, operations = extract_data_2(input)

    while len(operations) > 0:
        oper = operations.pop(0)
        num = data.pop(0)
        tmp_counter = 1 if oper == "*" else 0

        while num.strip() != '' and len(num) >= 0:
            if oper == "+":
                tmp_counter += int(num)
            elif oper == "*":
                tmp_counter *= int(num)
            if len(data) > 0:
                num = data.pop(0)

        count += tmp_counter

    print(f"Solved 2: {count}") 

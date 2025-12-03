def extract_data(input: list[str]):
    '''Extract and transform text data'''

    for line in input:
            yield [int(x) for x in line.strip()]


def get_max_rating(bank):
     if len(bank) < 2:
          return 0
     if len(bank) == 2:
          return 10 * bank[0] + bank[1]
     
     i = 0
     j = 2

    max_voltage = 10 * bank[i] + bank[j]

    while i < j:
        tmp_voltage = 10 * bank[i] + bank[j]
        while tmp_voltage > max_voltage and j < len(bank) - 1:
             max_voltage = tmp_voltage
             j += 1

     

def execute_part_one(input: list[str]) -> None:
    count = 0

    for line in extract_data(input):
        print(line)
        continue

    print(f"Solved 1: {count}")

def execute_part_two(input: list[str]) -> None:
        count = 0

        for line in extract_data(input):
            continue

        print(f"Solved 2: {count}")

import string

ALPHABET = string.ascii_letters
vals = [i for i in range(1, 53)]
ALPHABET_VALS = dict(zip(ALPHABET, vals))


def find_matching_items(rucksack: str) -> str:
    """
    The function takes a string "rucksack as input and checks
    what character of the string is repeated both in the first and 
    second half of the full string and returns the character.
    """

    half1 = rucksack[:len(rucksack)//2]
    half2 = rucksack[len(rucksack)//2:]

    unique_items = []  # unique items in list 1
    for item in half1:
        if item in unique_items:
            continue
        else:
            unique_items.append(item)
            if item in half2:
                return item


def calculate_sum_of_priorities(rucksacks: list[str]) -> int:
    """
    Given the list of rucksacks, calculare the sum of the priorities of
    the item types repeated across rucksack halves.
    """

    acc = 0
    for rucksack in rucksacks:
        matching_item = find_matching_items(rucksack)
        acc += ALPHABET_VALS[matching_item]

    return acc


if __name__ == '__main__':

    # read file and separate each line
    with open('problem3/input3.txt') as input:
        rucksacks = [line.rstrip('\n') for line in input]

    print(calculate_sum_of_priorities(rucksacks=rucksacks))

import string

ALPHABET = string.ascii_letters
vals = [i for i in range(1, 53)]
ALPHABET_VALS = dict(zip(ALPHABET, vals))


def find_matching_items(group: list[str]) -> str:
    """
    The function takes a list of string which correspon to the three 
    rucksacks in a elves grop as input and checks
    what character is repeated in each of the strings in the list.
    """

    unique_items = []  # unique items in list 1
    for item in group[0]:
        if item in unique_items:
            continue
        else:
            unique_items.append(item)
            matched_rucksacks = 0
            for rucksack in group[1:]:
                if item not in rucksack:
                    break

                matched_rucksacks += 1
                if matched_rucksacks == (len(group)-1):
                    return item


def calculate_sum_of_priorities(rucksacks: list[str], elves_in_group: int) -> int:
    """
    Given the list of rucksacks, calculare the sum of the priorities of
    the item types repeated across groups.
    """

    acc = 0
    group = []
    for rucksack in rucksacks:
        group.append(rucksack)
        if len(group) == elves_in_group:
            matching_item = find_matching_items(group)
            print(matching_item)
            acc += ALPHABET_VALS[matching_item]
            group.clear()
    return acc


if __name__ == '__main__':

    # read file and separate each line
    with open('problem3/input3.txt') as input:
        rucksacks = [line.rstrip('\n') for line in input]

    test = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

    print(calculate_sum_of_priorities(rucksacks, 3))

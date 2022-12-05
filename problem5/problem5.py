import string

# I thought it was fun to add all the types


def get_cartes_and_orders(input: list[str], max_height: int) -> tuple[list[list[int]], list[str]]:
    """
    Given the input of the problem: separate the section with the crates diagram
    and the section with the orders.

    Returns:
        - List with list of strings. Each sublist represents a stack of crates (in order)
        and each string a crate.
        - List of strings corresponding with each order (in order)
    """
    # sectio of the input with the crates diagram
    crates = input[:max_height]
    crates.reverse()

    #   indexes of the columns with the crates letters
    indexes = [i for i, char in enumerate(
        crates[0]) if char in string.ascii_uppercase]

    setup = []
    for i in range(len(indexes)):
        setup.append([row[indexes[i]] for row in crates])

    return setup, input[max_height+2:]


if __name__ == '__main__':
    with open('problem5/input5.txt') as input:
        lines = [line.rstrip('\n') for line in input]

    crates, orders = get_cartes_and_orders(lines, 8)
    print(orders)

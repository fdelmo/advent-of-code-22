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

    setup = trim_stacks(setup)

    return setup, input[max_height+2:]


def orders_to_tuple(order: str) -> tuple[int]:
    """
    From a written order of the type move 7 from 6 to 8 return a tuple with the
    values of move, from an to: (7,6,8)
    """
    separated = order.split(' ')
    return tuple([int(str) for str in separated if str.isdigit()])


def move_crates(crates: list[list[str]], orders: list[str]) -> list[list[str]]:
    """
    Given the initial crates setup and the orders, perform the permutations and
    return the final crate state.
    """
    for line in orders:
        order = orders_to_tuple(line)
        print(order)

        for moves in range(order[0]):
            crate_moved = crates[order[1]-1].pop()
            crates[order[2]-1].append(crate_moved)

    return crates


def get_top_crates(crates: list[list[str]]) -> str:
    """
    Given the crates setup, return the leters of the crates on top of each stack.
    """
    top = ''
    for stack in crates:
        for i in range(1, len(stack)+1):
            last = stack[-i]

            if last != '':
                top += last
                break

    return top


def trim_stacks(crates_input: list[list[str]]) -> list[list[str]]:
    """
    Given a initial setup of crates, trim each sublist so there are no
    empty strings at the end. e.g. from['A','B',''] to ['A','B']
    """
    for j in range(len(crates_input)):
        while crates_input[j][-1] == ' ':
            crates_input[j].pop()

    return crates_input


if __name__ == '__main__':
    with open('problem5/input5.txt') as input:
        lines = [line.rstrip('\n') for line in input]

    crates, orders = get_cartes_and_orders(lines, 8)

    final_crates = move_crates(crates, orders)

    print(final_crates)
    print(get_top_crates(final_crates))

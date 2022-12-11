from rope import Rope


def get_tail_movements(orders: list[str], body_length: int) -> list[frozenset[int]]:
    """
    Given a list of orders of movements and steps, update
    the position of the head and tail of the rope and 
    return a list with the positions the tail has visited.
    """

    rope = Rope(body_length)

    for order in orders:
        # get direction and steps to take
        direction = order[0]
        steps = int(order.split(' ')[-1])

        # move the rope
        rope.move(direction=direction, steps=steps)

    return rope.visited_by_tail


if __name__ == '__main__':

    # parse the input file into the variable "orders"
    with open('problem9/input9.txt', 'r') as input_file:
        orders = [line.rstrip('\n') for line in input_file]

    visited_by_tail = get_tail_movements(orders=orders, body_length=10)

    print(len(visited_by_tail))

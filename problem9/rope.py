from math import trunc

DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),

}


class Rope(object):
    """
    Class for the rope object. It contains all the
    logic of movement of the head and tail.
    """

    def __init__(self, body_length: int) -> None:
        """
        Class initialization with the starting position
        of the rope.
        """
        self.head = [0, 0]
        self.body = [[0, 0] for _ in range(1, body_length)]
        self.visited_by_tail = [tuple(self.body[-1])]

    def _update_head(self, direction: str) -> None:
        """
        Update the head position in the direction specified
        by one movement step.
        """
        self.head[0] += DIRECTIONS[direction.upper()][0]
        self.head[1] += DIRECTIONS[direction.upper()][1]

    def _update_body(self) -> None:
        """
        Updates the positions of the tail depending n the position
        of the head.
        """
        for i, part in enumerate(self.body):
            if i == 0:
                prev_part = self.head
            else:
                prev_part = self.body[i-1]

            move_h = trunc((prev_part[0]-part[0])/2)
            move_v = trunc((prev_part[1]-part[1])/2)

            part[0] += move_h
            part[1] += move_v

            if (part[0] != prev_part[0]) & (part[1] != prev_part[1]) & (abs(move_h) != abs(move_v)):
                part[0] += (move_v*(prev_part[0]-part[0])
                            * (prev_part[1]-part[1]))
                part[1] += (move_h*(prev_part[1]-part[1])
                            * (prev_part[0]-part[0]))

            if (i == (len(self.body)-1)) and (tuple(part) not in self.visited_by_tail):
                self.visited_by_tail.append(tuple(part))

    def move(self, direction: str, steps: int) -> None:
        """
        Move the rope: update the head and tail of the
        rope given the direction and steps in that direction
        to be taken by the head. The logic of the tail movement
        is calculated internally as specified by the problem
        statement.
        """
        for _ in range(steps):
            self._update_head(direction)
            self._update_body()

        print(direction, steps)
        print(self.head)
        print(self.body)
        print('-'*50)


if __name__ == '__main__':
    # testing purposes
    rope = Rope(10)
    while True:
        order = str(input("Move to:"))
        print(order)
        rope.move(order, 1)
        print(rope.head)
        print(rope.body)

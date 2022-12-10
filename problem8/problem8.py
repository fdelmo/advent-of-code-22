import numpy as np


def check_visible_trees_sides(trees: list[str]) -> list[tuple[int]]:
    """
    Given a list of list of trees heighs return the trees that are
    visible either from the left or the right.
    """
    visible_trees = []
    # loop over rows (except edges)
    for i in range(1, len(trees)-1):
        row = trees[i]
        # visible_trees.append([])
        left_reference, right_reference = int(row[0]), int(row[-1])

        # loop over trees in row (or cols) (except edges)
        len_row = len(row)  # used several times, so better store it in mem
        for j in range(1, len_row - 1):

            # visible from the left
            if int(row[j]) > left_reference and ((i, j) not in visible_trees):
                visible_trees.append((i, j))
                left_reference = int(row[j])

            # check visibility from right
            if int(row[-(j+1)]) > right_reference and ((i, (len_row - (j+1))) not in visible_trees):
                visible_trees.append((i, (len_row - (j+1))))
                right_reference = int(row[-(j+1)])

    return visible_trees


def check_visible_trees_veritcal(trees: list[str]) -> list[tuple[int]]:
    """
    Given a list of list of trees heighs return the trees that are
    visible either from the top or the bottom.
    """
    l_str = [[int(tree) for tree in row] for row in trees]
    transposed = np.array(l_str).T.tolist()

    visible_trees = []
    # loop over rows (except edges)
    for i in range(1, len(transposed)-1):
        row = transposed[i]
        # visible_trees.append([])
        left_reference, right_reference = int(row[0]), int(row[-1])

        # loop over trees in row (or cols) (except edges)
        len_row = len(row)  # used several times, so better store it in mem
        for j in range(1, len_row - 1):

            # visible from the left
            if (int(row[j]) > left_reference) and ((j, i) not in visible_trees):
                visible_trees.append((j, i))
                left_reference = int(row[j])

            # check visibility from right
            if int(row[-(j+1)]) > right_reference and (((len_row - (j+1)), i) not in visible_trees):
                visible_trees.append(((len_row - (j+1)), i))
                right_reference = int(row[-(j+1)])

    return visible_trees


def count_visible_trees(vis_h: list[tuple[int]], vis_v: list[tuple[int]]) -> int:
    """
    Given the trees visible from left-right and top-bottom. count how many
    non repeated trees we can see.
    """
    acc = 0
    for tree in vis_h:
        if tree not in vis_v:
            acc += 1

    return acc+len(vis_v)


if __name__ == '__main__':
    with open('problem8/input8.txt', 'r') as input:
        lines = [line.rstrip('\n') for line in input]

    vis_h = check_visible_trees_sides(lines)
    vis_v = check_visible_trees_veritcal(lines)

    print(count_visible_trees(vis_h, vis_v) +
          2*len(lines) + 2*len(lines[0]) - 4)

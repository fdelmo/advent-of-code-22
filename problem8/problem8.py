def count_visible_trees(trees: list[str]) -> int:
    """
    Given a list of list of trees heighs return the sum of the 
    visible trees as defined in the problem statement.
    """
    top_reference = trees[0]
    bottom_reference = []

    visible_trees = []
    # loop over rows (except edges)
    for i, row in enumerate(trees[1:-1]):
        # visible_trees.append([])
        left_reference, right_reference = int(row[0]), int(row[-1])

        # loop over trees in row (or cols) (except edges)
        len_row = len(row)  # used several times, so better store it in mem
        for j in range(1, len_row - 1):

            # visible from the left
            if int(row[j]) > left_reference:
                visible_trees.append((i, j))
                left_reference = int(row[j])

            # check visibility from right
            if int(row[-(j+1)]) > right_reference:
                visible_trees.append((i, (len_row - (j+1))))
                right_reference = int(row[-(j+1)])

    return visible_trees


if __name__ == '__main__':
    with open('problem8/example.txt', 'r') as input:
        lines = [line.rstrip('\n') for line in input]

    vis = count_visible_trees(lines)
    stop = 34

import numpy as np


def calc_max_scenic_score(trees: list[str]) -> int:
    """

    """
    trees_int = [[int(tree) for tree in row] for row in trees]
    transposed = np.array(trees_int).T.tolist()
    max_score = 0
    for i, row in enumerate(trees_int):
        for j, tree in enumerate(row):
            col = transposed[j]

            # check right:
            r_score = 0
            for neighbor in row[j+1:]:
                r_score += 1
                if neighbor >= tree:
                    break

            # check left:
            l_score = 0
            for neighbor_ind in range(len(row[:j])):
                l_score += 1
                if row[:j][-(neighbor_ind+1)] >= tree:
                    break

            # check down:
            d_score = 0
            for neighbor in col[i+1:]:
                d_score += 1
                if neighbor >= tree:
                    break

            # check up:
            u_score = 0
            for neighbor_ind in range(len(col[:i])):
                u_score += 1
                if col[:i][-(neighbor_ind+1)] >= tree:
                    break

            score_tup = (u_score, r_score, d_score, l_score)
            score = u_score*d_score*l_score*r_score

            if score > max_score:
                max_score = score

    return max_score


if __name__ == '__main__':
    with open('problem8/input8.txt', 'r') as input:
        lines = [line.rstrip('\n') for line in input]

    print(calc_max_scenic_score(lines))

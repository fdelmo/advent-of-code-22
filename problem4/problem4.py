
def check_if_pair_is_contained(pair: str) -> bool:
    """
    Given a pair of the type '2-3,2-5', return True if one of the segments
    fully contain the other. In this example the result should be True
    since 2-5 fully contain 2-3.
    """
    seg1, seg2 = pair.split(',')

    seg1 = tuple(map(int, seg1.split('-')))
    seg2 = tuple(map(int, seg2.split('-')))

    seg1_range = seg1[-1]-seg1[0]
    seg2_range = seg2[-1]-seg2[0]

    # case in which seg1 can fully contain seg2
    if seg1_range >= seg2_range:
        if (seg2[0] < seg1[0]) or (seg2[1] > seg1[1]):
            return False
        else:
            return True

    else:
        if (seg1[0] < seg2[0]) or (seg1[1] > seg2[1]):
            return False
        else:
            return True


def count_total_contained_pairs(pairs: list['str']) -> int:
    """
    Given an input with multiple segment pairs, count how many pairs have
    one segment fully contained in the other
    """

    acc = 0
    for pair in pairs:
        acc += check_if_pair_is_contained(pair)

    return acc


if __name__ == '__main__':

    with open('problem4/input4.txt') as input:
        pairs = [line.rstrip('\n') for line in input]

    test = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8'
    ]

    print(count_total_contained_pairs(pairs))

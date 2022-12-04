import time


def check_if_pair_is_contained(seg1: tuple[int], seg2: tuple[int]) -> bool:
    """
    Given a pair of the type '2-3,2-5', return True if one of the segments
    fully contain the other. In this example the result should be True
    since 2-5 fully contain 2-3.
    """

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


def check_if_overlap(seg1: tuple[int], seg2: tuple[int]) -> bool:
    """
    Given a pair of the type '2-4,3-5', return True if one of the segments
    overlap. In this example the result should be True since 3-4 are 
    contained in both segments.

    # NOTE: We don't care what segments overlap, only if there is any that does.
    """

    if (seg1[0] >= seg2[0]) & (seg1[0] <= seg2[1]):
        return True
    elif (seg1[1] >= seg2[0]) & (seg1[1] <= seg2[1]):
        return True

    return check_if_pair_is_contained(seg1, seg2)


def count_total_contained_and_overlaped_pairs(pairs: list['str']) -> int:
    """
    Given an input with multiple segment pairs, count how many pairs have
    one segment fully contained in the other
    """

    contained = 0
    overlaped = 0
    for pair in pairs:
        # separate the pair and transfor the str into int
        seg1, seg2 = pair.split(',')
        seg1 = tuple(map(int, seg1.split('-')))
        seg2 = tuple(map(int, seg2.split('-')))

        # compute the problem answers
        contained += check_if_pair_is_contained(seg1, seg2)
        overlaped += check_if_overlap(seg1, seg2)
    return contained, overlaped


if __name__ == '__main__':

    with open('problem4/input4.txt') as input:
        pairs = [line.rstrip('\n') for line in input]

    print(count_total_contained_and_overlaped_pairs(pairs=pairs))

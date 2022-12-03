
ENCRIPTION = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scisors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scisors'
}

VALUES = {
    'Rock': 1,
    'Paper': 2,
    'Scisors': 3
}


def calculate_score_round(game: str) -> int:
    """
    Calculate the score of a single game given by a string payr of the form 'A X'
    """

    if VALUES[ENCRIPTION[game[-1]]] == VALUES[ENCRIPTION[game[0]]]:  # tie
        score = 3
    elif (VALUES[ENCRIPTION[game[-1]]]-1) == (VALUES[ENCRIPTION[game[0]]] % 3):  # victory
        score = 6
    else:  # loss
        score = 0

    # add the value of the shape you chose
    return score + VALUES[ENCRIPTION[game[-1]]]


def calculate_score_tournament(strategy: list[str]) -> int:
    """
    Calculate the total score of the tournament. The results of each game are 
    entered as a list of string pairs.
    """

    score = 0
    for round in strategy:
        score += calculate_score_round(round)

    return score


if __name__ == '__main__':
    with open('problem2/input2.txt') as input:
        strategy = [line.rstrip("\n") for line in input]

    # part 1
    print(calculate_score_tournament(strategy=strategy))


ENCRIPTION = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scisors',
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

    value_oponent = VALUES[ENCRIPTION[game[0]]]

    if game[-1] == 'Y':  # tied
        result = 3
        value_played = value_oponent
    elif game[-1] == 'Z':  # win
        result = 6
        value_played = value_oponent % 3 + 1
    else:  # loss
        result = 0
        value_played = value_oponent - 1
        if value_played == 0:
            value_played = 3

    return result + value_played


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

    print(calculate_score_tournament(strategy=strategy))

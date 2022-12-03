from typing import List


def calculate_max_total_calories(calories: List[str | int], elves_to_consider: int) -> int:
    """
    Calculate the total calories carried by the n elves with the most calories carried.
    """
    # make sure that we have an end block at the end of the list
    calories.append('')

    max_calories = []
    sum_cal = 0
    for value in calories:
        # if there is a value, aggregate it to the sum of calories, if not it means we are
        # switching to the next elve and the sum needs to be reset to 0
        if value:
            sum_cal += int(value)

        # logic to check if the elve carries enough calories to be considered one of the top elves
        elif len(max_calories) < elves_to_consider:
            max_calories.append(sum_cal)
            sum_cal = 0

        elif sum_cal > min(max_calories):
            max_calories.remove(min(max_calories))
            max_calories.append(sum_cal)
            sum_cal = 0

        else:
            sum_cal = 0

    # return the sum of the calories carried by the top elves
    return sum(max_calories)


if __name__ == '__main__':

    with open('problem1/input1.txt') as input:
        calories = [line.rstrip('\n') for line in input]

    # Part 1
    print(calculate_max_total_calories(calories=calories, elves_to_consider=1))

    # Part 2
    print(calculate_max_total_calories(calories=calories, elves_to_consider=3))

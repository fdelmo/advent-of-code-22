def calculate_register_in_cycle(lines: list[str]) -> list[int]:
    """
    Given the input of the problem, return a list with the value
    of the register X DURING that register (first value in list is
    register 1).
    """
    register_in_cycle = [1]
    for line in lines:
        # both if noop or addx we need to wait one cycle
        register_in_cycle.append(register_in_cycle[-1])

        # if the order is not noop the the value gets changed after 2 cycles
        if line != 'noop':
            value = int(line.split(' ')[1])
            register_in_cycle.append(value + register_in_cycle[-1])

    return register_in_cycle


def sum_signal_strengths(register_vals: list[int], cycles: list[int]) -> int:
    """
    Given the register of X during each cycle and the cycles to consider,
    calculate the sum of the signal strength during those cycles.
    """
    strength = 0
    for cycle in cycles:
        adjusted_cycle = cycle-1  # to adjust to base 0 indexing
        strength += (cycle*register_vals[adjusted_cycle])

    return strength


with open('problem10/input10.txt', 'r') as input_file:
    lines = [line.rstrip('\n') for line in input_file]

    registers = calculate_register_in_cycle(lines)
    print(sum_signal_strengths(registers, [20, 60, 100, 140, 180, 220]))

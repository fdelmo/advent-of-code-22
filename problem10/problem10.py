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


def determine_draw_pixel(register_value: int, sprite_position: int) -> str:
    """
    Given the sprite position at a certain cycle and the register value at
    that cycle, determine if the sprite should draw the pixel or leave it blank.
    """
    return ("#" if (sprite_position in range(register_value-1, register_value + 2)) else ".")


def draw_screen(register_values: list[int]) -> list[str]:
    """
    Given the value of the register X at each cycle, return a list of strings
    (the screen rendered) with values "#" if the pixel is drawn or "." if it is not.
    """
    screen = [[]]
    j = 0
    i = 0
    for value in register_values:
        pixel = determine_draw_pixel(value, i)
        screen[j].append(pixel)
        i += 1
        if (i % 40) == 0:
            screen.append([])
            j += 1
            i = 0

    screen.pop()
    return screen


with open('problem10/input10.txt', 'r') as input_file:
    lines = [line.rstrip('\n') for line in input_file]

    registers = calculate_register_in_cycle(lines)
    print(sum_signal_strengths(registers, [20, 60, 100, 140, 180, 220]))

    screen_render = draw_screen(register_values=registers)
    print(*screen_render, sep='\n')

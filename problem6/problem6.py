from collections import deque


def detect_start_of_packet_position(stream: str, packet_len: int) -> int:
    """
    Given a stream of characters, the function return the position of the
    first element whose previous n characters are different to it and between then,
    where n is the packet length passed as packet_len argument.
    """
    marker = deque(stream[:packet_len-1], maxlen=packet_len)

    for i, char in enumerate(stream[packet_len-1:]):
        marker.append(char)
        if len(set(marker)) == packet_len:
            return i + packet_len


if __name__ == '__main__':
    # read input file
    with open('problem6/input6.txt', 'r') as input:
        streams = [line.rstrip('\n') for line in input]

    print(detect_start_of_packet_position(stream=streams[0], packet_len=4))

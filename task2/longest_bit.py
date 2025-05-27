from scipy import special
from work_with_json_files import *



def longest_bit_test(seq: str, pi_values: list) -> float:
    """
    The function checks sequence using test for the longest sequence in block
    :param seq: our sequence
    :param pi_values: const pi values
    :return: result
    """
    settings = read_json_file("settings.json")
    n = len(seq)
    m = settings["m"]

    if n == 0:
        raise ValueError("Sequence must not be empty")

    v = [0, 0, 0, 0]

    for i in range(0, len(seq), m):
        block = []
        for j in range(m):
            if i + j < len(seq):
                block.append(seq[i + j])
            else:
                break
        max_len = current = 0

        for bit in block:
            if bit == "1":
                current = current + 1
            else:
                current = 0
            max_len = max(max_len, current)

        match max_len:
            case max_len if max_len <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1

    xi_square = sum(
        ((v[i] - 16 * pi_values[i]) ** 2) / (16 * pi_values[i]) for i in range(len(v))
    )
    pi = special.gammainc((3 / 2), (xi_square / 2))

    return pi

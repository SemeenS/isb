import math


def bitwise_frequency_test(sequence: str) -> float:
    """
    The function checks sequence using frequency bit test
    :param sequence:
    :return: result
    """

    n = len(sequence)

    if n == 0:
        raise ValueError("Empty sequence")
    res = 0
    for bit in sequence:
        if bit == "1":
            res += 1
        elif bit == "0":
            res -= 1
        else:
            raise ValueError("Sequence must contain only '0' and '1'")

        s_n = res / math.sqrt(n)
        return math.erfc(abs(s_n) / math.sqrt(2))

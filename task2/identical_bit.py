import math


def identical_bit_test(sequence: str) -> float:
    """
    The function checks sequence using identical bit test
    :param sequence: our sequence
    :return: result
    """
    if not sequence:
        raise ValueError("Sequence must not be empty")

    n = len(sequence)
    res = 0

    for bit in sequence:
        if bit == "1":
            res += 1
        elif bit == "0":
            res += 0
        elif bit != "0":
            raise ValueError(f"Invalid symbol '{bit}' in sequence.")

    zeta = res / n

    if abs(zeta - 0.5) >= (2 / math.sqrt(n)):
        return 0.0

    v_n = 0
    for i in range(n - 1):
        if sequence[i] != sequence[i + 1]:
            v_n += 1

    p_value = math.erfc(
        abs(v_n - 2 * n * zeta * (1 - zeta))
        / (2 * math.sqrt(2 * n) * zeta * (1 - zeta))
    )

    return p_value
